# Texas: law history in git

The statute law of Texas as a git repository: one file per section, committed with the official publisher named as author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the State of Texas (516 sections) | 1 | One version: the current text as the Texas Legislative Council published it, dated 2026-07-31 |
| `penal-code/` | Texas Penal Code (467 sections) | 1 | One version: the current text as the Texas Legislative Council published it, dated 2026-04-10 |
| `property-code/` | Texas Property Code (1782 sections) | 1 | One version: the current text as the Texas Legislative Council published it, dated 2026-04-10 |
| `business-organizations-code/` | Texas Business Organizations Code (1362 sections) | 1 | One version: the current text as the Texas Legislative Council published it, dated 2026-04-10 |

Nothing else of Texas's law is in it yet.

## Where the text comes from

The text is read from the per-code HTML zips that the **Texas Legislative Council** lists for download at <https://statutes.capitol.texas.gov/> (`StatuteCodeDownloads.json`; files at `tcss.legis.texas.gov/resources/Zips/`). Four files were fetched, one at a time. Only statute text and the Council's source note for each section (the "Acts 1973, 63rd Leg., ... eff. ..." line) are kept; chapter and article headings between sections are left out.

## Dates

- Each act has **one version**, dated the day the Council last modified its zip (the Constitution 31 July 2026; the three codes 10 April 2026). It is the oldest version available: the Council publishes no past versions online.
- The first commit of each act is credited to the Texas Legislative Council as "oldest version available".
- The effective dates in each section's source note are part of its text, not the commit dates.

## What it does not show

- Any amendment history: the text before the Council's 2026 files is not here.
- Text that takes effect in the future: the Council's current file prints both texts of some sections; the second keeps the key suffix `-dup2`. Files the Council keeps for the pre-amendment text of a chapter (`*_old.htm`) are left out.
- The other 27 Texas codes, Vernon's Civil Statutes, session laws and regulations.
- Nothing here is an official publication.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- Each source file is identified by its sha256, in `data/versions.json`.

## What "author" means

Each commit is authored by the publisher (the Texas Legislative Council) because this first build holds one version of each act, the oldest version available. The committer is always Lexifina.
