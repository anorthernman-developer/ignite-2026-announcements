# Metadata schema

Every announcement carries the fields below, in this order, in the spreadsheet, CSV and JSON. The machine-readable version is [schema.json](schema.json) (JSON Schema 2020-12). Allowed values for enum fields are in [../taxonomy/taxonomy.md](../taxonomy/taxonomy.md).

| Field | Type | Required | Meaning | Example |
| --- | --- | --- | --- | --- |
| id | string | Yes | Stable identifier IGN26-<FAMILY>-<NNN>. Never reused. | IGN26-SEC-005 |
| title | string | Yes | Short plain title in sentence case. | Microsoft Perception generally available |
| announced_date | date (YYYY-MM-DD) | No | Date announced at Ignite; blank for adjacent items. | 2026-11-17 |
| event | string | Yes | Event name. | Microsoft Ignite 2026 |
| ignite_scope | enum | Yes | Ignite 2026 or an Adjacent value. See taxonomy. | Ignite 2026 |
| product_family | enum | Yes | Taxonomy level 1. | Security, identity and compliance |
| product | string | Yes | Taxonomy level 2, Microsoft's product name. | Microsoft Defender |
| capability_area | string | Yes | Taxonomy level 3. | Attack disruption |
| announcement_type | enum | Yes | Kind of news. See taxonomy. | New capability |
| status | string | Yes | Release stage in Microsoft's own words, including mixed stages. | GA; SIEM breadth preview |
| status_category | enum | Yes | Normalised stage for filtering. | Mixed |
| availability | string | Yes | Stated availability date or window; 'Not stated' when absent. | GA December 2026 |
| audience | enum | Yes | Primary audience. | Security teams |
| industry | enum | Yes | Industry focus or Cross-industry. | Healthcare |
| licensing | string | No | Licence, SKU, credit or price conditions where stated. | Microsoft 365 E5 or E7 |
| region | string | Yes | Region availability or 'Not stated'. | 14 regions incl. UK South |
| tags | string (semicolon list) | No | Free keywords for search. | dlp;copilot |
| summary | string | Yes | One or two plain sentences on what was announced. |  |
| source_url | url | Yes | Primary official source. Every row must have one. | https://news.microsoft.com/events/ignite/2026/book-of-news/ |
| secondary_source | url | No | Second official source, usually the product blog. |  |
| verification | enum | Yes | Kind of source the row rests on. | Book of News |
| related | string (semicolon list of ids) | No | Other rows for the same product. | IGN26-SEC-006;IGN26-SEC-007 |
| first_seen | date | Yes | Run date the row was first captured. | 2026-11-18 |
| last_updated | date | Yes | Run date the row last changed. | 2026-11-18 |

## Quality rules

1. No row without a `source_url` on an official Microsoft, GitHub or Microsoft AI page.
2. `status` keeps Microsoft's wording; `status_category` is the filterable value.
3. Unknown values are written as 'Not stated', never guessed.
4. `first_seen` never changes; `last_updated` changes when any field changes, and CHANGELOG.md says what changed.
5. Rows found only by Parallel research are marked in `verification` until re-read on a Microsoft page.