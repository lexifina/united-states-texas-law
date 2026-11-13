# How this repository was made (Texas)

This file is written by the build on 2026-11-13, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Texas Constitution and Statutes (Texas Legislative Council) | <https://statutes.capitol.texas.gov/> | 2026-10-30 | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020). No annotations are taken. |
| Texas Legislative Council: every code, one HTML zip each | <https://statutes.capitol.texas.gov/assets/StatuteCodeDownloads.json> | 2026-11-03 | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020). No annotations are taken. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the State of Texas | 1 | 2025-11-04 to 2025-11-04 |
| `penal-code` | Texas Penal Code | 1 | 2025-12-04 to 2025-12-04 |
| `property-code` | Texas Property Code | 1 | 2026-01-01 to 2026-01-01 |
| `business-organizations-code` | Texas Business Organizations Code | 1 | 2026-01-01 to 2026-01-01 |
| `agriculture-code` | Texas Agriculture Code | 1 | 2025-09-01 to 2025-09-01 |
| `alcoholic-beverage-code` | Texas Alcoholic Beverage Code | 1 | 2025-09-01 to 2025-09-01 |
| `auxiliary-water-laws` | Texas Auxiliary Water Laws | 1 | 1989-09-01 to 1989-09-01 |
| `business-and-commerce-code` | Texas Business & Commerce Code | 1 | 2026-09-01 to 2026-09-01 |
| `civil-practice-and-remedies-code` | Texas Civil Practice and Remedies Code | 1 | 2025-12-04 to 2025-12-04 |
| `code-of-criminal-procedure` | Texas Code of Criminal Procedure | 1 | 2026-04-01 to 2026-04-01 |
| `education-code` | Texas Education Code | 1 | 2026-09-01 to 2026-09-01 |
| `election-code` | Texas Election Code | 1 | 2025-12-04 to 2025-12-04 |
| `estates-code` | Texas Estates Code | 1 | 2026-01-01 to 2026-01-01 |
| `family-code` | Texas Family Code | 1 | 2025-12-04 to 2025-12-04 |
| `finance-code` | Texas Finance Code | 1 | 2026-01-01 to 2026-01-01 |
| `government-code` | Texas Government Code | 1 | 2026-10-01 to 2026-10-01 |
| `health-and-safety-code` | Texas Health and Safety Code | 1 | 2026-09-01 to 2026-09-01 |
| `human-resources-code` | Texas Human Resources Code | 1 | 2026-09-01 to 2026-09-01 |
| `insurance-code` | Texas Insurance Code | 1 | 2026-01-01 to 2026-01-01 |
| `insurance-code-not-codified` | Texas Insurance Code - Not Codified | 1 | 2011-09-01 to 2011-09-01 |
| `labor-code` | Texas Labor Code | 1 | 2026-01-01 to 2026-01-01 |
| `local-government-code` | Texas Local Government Code | 1 | 2026-06-01 to 2026-06-01 |
| `natural-resources-code` | Texas Natural Resources Code | 1 | 2025-09-01 to 2025-09-01 |
| `occupations-code` | Texas Occupations Code | 1 | 2026-09-01 to 2026-09-01 |
| `parks-and-wildlife-code` | Texas Parks and Wildlife Code | 1 | 2025-09-01 to 2025-09-01 |
| `special-district-local-laws-code` | Texas Special District Local Laws Code | 1 | 2026-01-01 to 2026-01-01 |
| `tax-code` | Texas Tax Code | 1 | 2026-09-01 to 2026-09-01 |
| `transportation-code` | Texas Transportation Code | 1 | 2026-09-01 to 2026-09-01 |
| `utilities-code` | Texas Utilities Code | 1 | 2026-09-01 to 2026-09-01 |
| `water-code` | Texas Water Code | 1 | 2026-09-01 to 2026-09-01 |
| `vernon-s-civil-statutes` | Texas Vernon's Civil Statutes | 1 | 2025-10-01 to 2025-10-01 |

The build made 53 commits:

| Commits | Kind |
| ---: | --- |
| 31 | baseline texts where the record starts |
| 0 | named laws, court decisions and treaties |
| 0 | changes no amendment note explains, credited to the publisher |
| 22 | corrections to the existing record |
| 0 | printing or layout changes |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-13.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 31 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Tex. Gov't Code 311.025 and each session law's own effective date; this first build holds only the current text, dated by the Council's publication of it https://statutes.capitol.texas.gov/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `73534e2b1770cd127dd7016f4b54a298949a4e3c37a8b924c4fe65f005386e4b` (140243919 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `63170edd89e92292ac248dae17d79e486e4e9f19`, `check.py` `e340718c28cd5b0edbe37bdeab1aac31427ada66`, `on.py` `4a8aa1c9a5e6bd8cc831b90a6e68c5a6f448a13c`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- First build: only the current text of the Constitution, Penal Code, Property Code and Business Organizations Code is published, so each act has one version, dated the day the Council last modified its zip and credited to the publisher as the oldest version available.
- Chapter files named *_old.htm (the text a section has until a future amendment takes effect) are left out so each section appears once; where the Council prints two texts of one section in the current file, the second gets the key suffix -dup2.
- Article and chapter headings between sections are left out; each section keeps the Council's source note.
- Wave 3 (2026-11-03): every other Texas code is added from the Council's HTML zips, one act per code, parsed as in the first build (one unit per section, the source note kept, *_old.htm files left out).
- Each new code's single version is dated by the latest in-force day ("eff. <date>") its source notes give on or before the retrieval day (2026-11-03), so the current wording is never dated before its latest amendment took effect; with no such day, the retrieval day. It is credited to the publisher as the oldest version available.
- A section whose every source note gives an in-force day after 2026-11-03, or that the Council heads "Text of section effective on <a later day>", is left out as not yet in force (342 sections). Subsection-level "Text of subsection effective ..." variants are kept as printed.
- The Constitution, Business Organizations Code, Penal Code and Property Code current-text dates use the latest applicable dates in the Council section source notes, not download ZIP Last-Modified days.
- Property Code Section 5.008 retains the Council's complete four-table seller disclosure form, rendered from the official HTML table cells in source order.

## What AI did and did not do

The source readers and builders were developed under Lexifina's direction with coding assistants, including Claude Code and Codex.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- A model identified the source-date findings and scoped this correction. A deterministic HTML parser rendered Property Code Section 5.008 from the Council ZIP; its words and punctuation were checked in source order. No legal wording was authored or corrected by a model.
