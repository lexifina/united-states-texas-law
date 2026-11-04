"""Write the Texas source and coverage summary from the current corpus."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
corpus = json.loads((HERE / 'corpus.json').read_text(encoding='utf8'))
rows = []
for act in corpus['acts']:
    version = act['versions'][0]
    rows.append(f"| `{act['slug']}/` | {act['title']} | {len(version['units']):,} | {version['from']} |")

readme = """# Texas: law history in git

This repository holds all 31 download groups listed by the Texas Legislative Council, including the Constitution and Vernon's Civil Statutes. Each has one version of the Council's current text, with one file per section. Earlier versions, session laws and regulations are outside this record.

| Folder | Act | Sections | Version date |
| --- | --- | ---: | --- |
""" + '\n'.join(rows) + """

## Source and dates

The Texas Legislative Council publishes the Constitution and statutes at <https://statutes.capitol.texas.gov/>. The text here comes from its per-code HTML downloads, including the Council's section source notes. Article and chapter headings between sections are outside this section-level record.

Each act has one version, the oldest available here. For the first four acts, the version date is the source file's Last-Modified day. For the other acts, it is the latest effective day in the Council's section source notes on or before 3 November 2026, or the retrieval day if no such day appears. These dates describe a current-text snapshot; they do not reconstruct the act's earlier history. The Council is credited as publisher.

Sections that the source says take effect after 3 November 2026 are excluded. Some subsection-level future variants remain as the Council prints them. Files that the Council names `*_old.htm` are outside the current-text record.

The source's punctuation is preserved, including curly quotation marks and dashes. This is an unofficial reproduction; consult the Council's publication for legal use.
"""
(HERE / 'repo' / 'README.md').write_text(readme, encoding='utf8', newline='\n')
path = HERE / 'repo' / 'jurisdiction.json'
j = json.loads(path.read_text(encoding='utf8'))
j['build'] = 'built: Texas Constitution and all 30 listed codes, current text only (one version each)'
path.write_text(json.dumps(j, indent=2) + '\n', encoding='utf8', newline='\n')
