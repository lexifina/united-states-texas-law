import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'world-law'))
from state_docs import write_docs

c = json.load(open(os.path.join(HERE, 'corpus.json'), encoding='utf-8'))
acts = []
folders = {'constitution': 'Constitution of the State of Texas', 'penal-code': 'Texas Penal Code',
           'property-code': 'Texas Property Code', 'business-organizations-code': 'Texas Business Organizations Code'}
for a in c['acts']:
    v = a['versions'][0]
    acts.append({'folder': a['slug'], 'title': a['title'] + f" ({len(v['units'])} sections)", 'versions': 1,
                 'history': f"One version: the current text as the Texas Legislative Council published it, dated {v['from']}"})
write_docs(HERE, {
    'name': 'Texas', 'code': 'TX', 'slug': 'united-states-texas', 'date': '2026-10-30', 'domain': 'statutes-texas',
    'publisher': 'the Texas Legislative Council',
    'acts': acts,
    'build': 'built: Texas Constitution, Penal Code, Property Code and Business Organizations Code, current text only (one version each, Council zips of 2026)',
    'source': ("The text is read from the per-code HTML zips that the **Texas Legislative Council** lists for download at "
              "<https://statutes.capitol.texas.gov/> (`StatuteCodeDownloads.json`; files at `tcss.legis.texas.gov/resources/Zips/`). "
              "Neither host publishes a robots.txt. Four files were fetched, one at a time. Only statute text and the Council's source "
              "note for each section (the \"Acts 1973, 63rd Leg., ... eff. ...\" line) are kept; chapter and article headings between "
              "sections are left out."),
    'dates': ("- Each act has **one version**, dated the day the Council last modified its zip (the Constitution 31 July 2026; the "
              "three codes 10 April 2026). It is the oldest version available: the Council publishes no past versions online.\n"
              "- The first commit of each act is credited to the Texas Legislative Council as \"oldest version available\".\n"
              "- The effective dates in each section's source note are part of its text, not the commit dates."),
    'limits': ("- Any amendment history: the text before the Council's 2026 files is not here.\n"
              "- Text that takes effect in the future: the Council's current file prints both texts of some sections; the second keeps the key suffix `-dup2`. Files the Council keeps for the pre-amendment text of a chapter (`*_old.htm`) are left out.\n"
              "- The other 27 Texas codes, Vernon's Civil Statutes, session laws and regulations.\n"
              "- Nothing here is an official publication."),
    'licence': ("The legal text is the Constitution and statutes of Texas as published by the Texas Legislative Council at "
                "https://statutes.capitol.texas.gov/. Statutes are not copyrightable (Georgia v. Public.Resource.Org, Inc., 590 U.S. 255 (2020)); "
                "no annotations are taken. The text is republished unaltered in its wording, with credit to the Texas Legislative Council as its publisher."),
})
