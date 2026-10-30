# How this repository was made (Texas)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Texas Constitution and Statutes (Texas Legislative Council) | <https://statutes.capitol.texas.gov/> | 2026-10-30 | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020). No annotations are taken. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the State of Texas | 1 | 2026-07-31 to 2026-07-31 |
| `penal-code` | Texas Penal Code | 1 | 2026-04-10 to 2026-04-10 |
| `property-code` | Texas Property Code | 1 | 2026-04-10 to 2026-04-10 |
| `business-organizations-code` | Texas Business Organizations Code | 1 | 2026-04-10 to 2026-04-10 |

The build made 4 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Tex. Gov't Code 311.025 and each session law's own effective date; this first build holds only the current text, dated by the Council's publication of it https://statutes.capitol.texas.gov/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `f3a5e34d54a85636b40d7097388089d86d25709163dae1060c451ab52e5ccc4c` (6153746 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- First build: only the current text of the Constitution, Penal Code, Property Code and Business Organizations Code is published, so each act has one version, dated the day the Council last modified its zip and credited to the publisher as the oldest version available.
- Chapter files named *_old.htm (the text a section has until a future amendment takes effect) are left out so each section appears once; where the Council prints two texts of one section in the current file, the second gets the key suffix -dup2.
- Article and chapter headings between sections are left out; each section keeps the Council's source note.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
