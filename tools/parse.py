"""Read the cached Texas code HTML into corpus.json (no network; deterministic).

    python parse.py
Each code (Constitution, Penal, Property, Business Organizations) is one act with one version: the current text
published by the Texas Legislative Council (the zip's Last-Modified day), credited to the publisher as the oldest
version available. Each section is one unit; one paragraph per line, with the Council's source note (the "Acts ..., eff."
line) kept as the last line.
"""
import json, os, re, sys
from email.utils import parsedate_to_datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'world-law'))
from state_corpus import clean, unit_key, add_unit, sha256_file, write  # noqa: E402

CACHE = os.path.join(HERE, '.cache')
LOG = json.load(open(os.path.join(CACHE, 'fetch-log.json')))
CODES = [('CN', 'constitution', 'Constitution of the State of Texas', 'TX Const.'),
         ('PE', 'penal-code', 'Texas Penal Code', 'Penal Code'),
         ('PR', 'property-code', 'Texas Property Code', 'Property Code'),
         ('BO', 'business-organizations-code', 'Texas Business Organizations Code', 'Bus. Orgs. Code')]
MARK = re.compile(r'<a name="([^"]+)"></a><a name="[^"]*"></a></p>')
PARA = re.compile(r'<p\b([^>]*)>(.*?)</p>', re.S)
SEC = re.compile(r'^(Sec\.|Secs\.|Section)\s+(\S+?)\.?\s+(.*)$')
LINK = re.compile(r'^<a [^>]*>(.*?)</a>(.*)$', re.S)


def numkey(f):
    return [int(x) if x.isdigit() else x for x in re.split(r'(\d+)', f)]


def parse_code(code):
    d = os.path.join(CACHE, 'htm', code)
    units = {}
    files = sorted((f for f in os.listdir(d) if f.lower().endswith('.htm') and '_old' not in f.lower()), key=numkey)
    for f in files:
        raw = open(os.path.join(d, f), encoding='utf-8', errors='replace').read()
        parts = MARK.split(raw)
        for i in range(1, len(parts), 2):
            anchor, body = parts[i], parts[i + 1]
            lines, head = [], None
            for attrs, inner in PARA.findall(body):
                if 'class="center"' in attrs:   # chapter / article headings between sections
                    continue
                lm = LINK.match(inner.strip())
                if lm and head is None and SEC.match(clean(lm.group(1)) + ' x'):
                    head = clean(lm.group(1))
                    inner = lm.group(2)
                t = clean(inner)
                if t:
                    lines.append(t)
            if head is None and not lines:
                continue
            if head:
                hm = SEC.match(head + ' x')
                label_no = hm.group(2)
                head_text = re.sub(r'^(Sec\.|Secs\.|Section)\s+\S+?\.?\s+', '', head)
                heading_line = f'# Sec. {label_no}. {head_text}'.rstrip()
                label = 'Sec. ' + label_no if code != 'CN' else 'Art. ' + anchor.replace('.', ', Sec. ', 1)
            else:
                heading_line = f'# {anchor}'
                label = anchor
            unit = {'label': label, 'kind': 'section', 'text': '\n'.join([heading_line] + lines) + '\n'}
            add_unit(units, unit_key(anchor), unit)
    return units


def main():
    acts = []
    for code, slug, title, short in CODES:
        units = parse_code(code)
        z = os.path.join(CACHE, f'{code}.htm.zip')
        lm = parsedate_to_datetime(LOG[code]['last_modified']).date().isoformat()
        print(code, len(units), 'units', lm)
        acts.append({'slug': slug, 'short': short, 'title': title,
                     'url': f'https://statutes.capitol.texas.gov/Docs/{code}/htm/{code}.1.htm',
                     'first_law': None, 'earlier_laws': [],
                     'versions': [{'from': lm, 'source_url': LOG[code]['url'], 'sha256': sha256_file(z), 'units': units,
                                   'note': 'Current text as published by the Texas Legislative Council; earlier versions are not published online.'}]})
    corpus = {
        'country': {'code': 'US-TX', 'name': 'Texas', 'slug': 'united-states-texas', 'lang': 'en', 'tz': 'America/Chicago',
                    'future_branch': 'future',
                    'publisher': {'name': 'Texas Legislative Council', 'email': 'tlc@statutes-texas.invalid'},
                    'default_in_force_rule': {'text': "Tex. Gov't Code 311.025 and each session law's own effective date; this first build holds only the current text, dated by the Council's publication of it",
                                              'source': 'https://statutes.capitol.texas.gov/'},
                    'licence_note': 'Texas Legislative Council, https://statutes.capitol.texas.gov/ (statutory text; no annotations).'},
        'sources': [{'name': 'Texas Constitution and Statutes (Texas Legislative Council)', 'url': 'https://statutes.capitol.texas.gov/',
                     'retrieved': '2026-10-30', 'requests': 4,
                     'licence': "Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020). No annotations are taken.",
                     'notes': 'Per-code HTML zips listed in assets/StatuteCodeDownloads.json; tcss.legis.texas.gov and statutes.capitol.texas.gov publish no robots.txt.'}],
        'laws': {}, 'acts': acts, 'applies': [],
        'decisions': ['First build: only the current text of the Constitution, Penal Code, Property Code and Business Organizations Code is published, so each act has one version, dated the day the Council last modified its zip and credited to the publisher as the oldest version available.',
                      'Chapter files named *_old.htm (the text a section has until a future amendment takes effect) are left out so each section appears once; where the Council prints two texts of one section in the current file, the second gets the key suffix -dup2.',
                      "Article and chapter headings between sections are left out; each section keeps the Council's source note."],
        'ai_use': ['none']}
    write(os.path.join(HERE, 'corpus.json'), corpus)


if __name__ == '__main__':
    main()
