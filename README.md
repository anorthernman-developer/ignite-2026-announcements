# Microsoft Ignite 2026 announcements tracker

A public, sourced record of the product and service news from Microsoft Ignite 2026 (17-20 November 2026, San Francisco and online). Built for consultants, partners and IT leaders who need to know what was announced, what stage it is at and where Microsoft said it.

Primary source: the [Ignite 2026 live news blog](https://news.microsoft.com/events/ignite/2026/live-news/), then the [Book of News](https://news.microsoft.com/events/ignite/2026/book-of-news/) and the official Microsoft blogs they link to. Every row cites an official page. Nothing is added without one.

Last build: 23 November 2026, 09:00 GMT. Announcements captured: 131 (123 from Ignite itself, 8 adjacent licensing and partner items, marked as such).

## Start here

| If you want | Open |
| --- | --- |
| The full list in Excel, filterable | [data/announcements.xlsx](data/announcements.xlsx) |
| One text file to paste into an LLM | [LLM.TXT](LLM.TXT) |
| What changed on each run | [CHANGELOG.md](CHANGELOG.md) |
| Search terms for Parallel Monitor and deep research | [search-terms/parallel-search-terms.md](search-terms/parallel-search-terms.md) |

## Files

| File | What it holds |
| --- | --- |
| [README.md](README.md) | This page |
| [LLM.TXT](LLM.TXT) | Key announcements as plain text, grouped by product family, one line each: status, title, availability, summary, source URL, id |
| [CHANGELOG.md](CHANGELOG.md) | Dated entries for every update run |
| [data/announcements.xlsx](data/announcements.xlsx) | Central spreadsheet. Tabs: Announcements (one row each, filterable table), Taxonomy - products, Taxonomy - lookups, Summary, Change log, Sources |
| [data/announcements.csv](data/announcements.csv) | Same rows as CSV |
| [data/announcements.json](data/announcements.json) | Same rows as JSON |
| [taxonomy/taxonomy.md](taxonomy/taxonomy.md) | Product hierarchy (family > product > capability) and every classification list |
| [taxonomy/taxonomy.json](taxonomy/taxonomy.json) | Machine-readable taxonomy |
| [ontology/ontology.md](ontology/ontology.md) | Entities and relations explained |
| [ontology/ontology.ttl](ontology/ontology.ttl) | OWL ontology in Turtle |
| [ontology/ontology.jsonld](ontology/ontology.jsonld) | JSON-LD context mapping the JSON data to the ontology |
| [metadata/schema.md](metadata/schema.md) | Every metadata field, its type and rules |
| [metadata/schema.json](metadata/schema.json) | JSON Schema used to validate each row |
| [search-terms/parallel-search-terms.md](search-terms/parallel-search-terms.md) | Monitor queries, a deep research prompt and keyword lists by category |
| [research/parallel/2026-11-18/](research/parallel/2026-11-18/README.md) | Raw output of the 3 Parallel test runs and the deep research run, with the review notes |
| [scripts/data.py](scripts/data.py) | The source list of announcements |
| [scripts/build.py](scripts/build.py) | Rebuilds the spreadsheet, CSV, JSON and LLM.TXT from data.py |
| [scripts/taxonomy_gen.py](scripts/taxonomy_gen.py) | Rebuilds the taxonomy files |

## How it is structured

Each announcement is one row with 24 metadata fields (see [metadata/schema.md](metadata/schema.md)). The taxonomy has three product levels (family, product, capability area) and separate lists for announcement type, release status, audience, industry, Ignite scope and verification. The ontology links announcements to products, statuses, audiences, licences, partners and sources.

Status is kept twice: Microsoft's own wording in `status`, and a normalised `status_category` for filtering. Where one announcement has parts at different stages, the category is Mixed and the wording explains each part.

### Announcements by product family

| Product family | Count |
| --- | --- |
| Microsoft Copilot | 25 |
| Security, identity and compliance | 19 |
| Azure infrastructure and operations | 15 |
| Agents and agent governance | 14 |
| AI models and Microsoft Foundry | 13 |
| Data and databases | 10 |
| Business applications | 7 |
| Developer tools and GitHub | 7 |
| Licensing, pricing and partner programme | 7 |
| Windows, Windows 365 and endpoint management | 6 |
| Microsoft IQ | 5 |
| Microsoft Edge | 2 |
| Partnerships and ecosystem | 1 |

### Announcements by status

| Status category | Count |
| --- | --- |
| GA | 35 |
| Mixed | 25 |
| Public preview | 19 |
| Preview (stage not stated) | 18 |
| Announced | 10 |
| Frontier | 8 |
| Private or limited preview | 6 |
| Coming soon | 3 |
| Licensing change | 3 |
| Retirement | 3 |
| Milestone | 1 |

## Update cadence

During Ignite week (17-20 November 2026) the tracker is rebuilt 3 times a day. Each run re-reads the live news blog and the Book of News, adds new rows, updates any status changes, logs them in CHANGELOG.md and regenerates the spreadsheet and LLM.TXT. After the event the cadence drops to once a day to catch December GA dates.

## Rebuild locally

```
pip install openpyxl
python scripts/taxonomy_gen.py
python scripts/build.py
```

## Caveats

- Microsoft's Book of News notes its instant summaries are AI-generated. Rows are written from the full item text and product blogs.
- Rows marked with a verification value other than Book of News or an official blog are re-read on the next run.
- Known gaps: Security Copilot (no Ignite-dated official post found yet), Power Automate (only covered through the Power Platform Ignite post), the Teams Ignite what's-new post for end users, Teams Channel Backup (private preview, only third-party coverage found so far) and most industry news. See [research/parallel/2026-11-18/README.md](research/parallel/2026-11-18/README.md).

Maintained for Craig Stanley. Not affiliated with Microsoft.
