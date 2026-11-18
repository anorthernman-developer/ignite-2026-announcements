# Change log

All dates and times are UK time (GMT).

## 18 November 2026, 13:30 GMT: run 1, first build

Added
- Created the repository with README, taxonomy, ontology, metadata schema, spreadsheet, CSV, JSON, LLM.TXT, search terms and Parallel research outputs.
- Captured 120 announcements: 112 from Ignite 2026 and 8 adjacent licensing, partner and pre-Ignite items.
- Sources read: Ignite 2026 live news blog, the Book of News, and the official Microsoft, Azure, Windows, Dynamics 365, Microsoft AI, Tech Community, GitHub changelog and Partner Center pages they lead to.

Parallel runs
- 3 test runs (Copilot and agents; Azure, data and GitHub; security, Microsoft 365, Windows and business apps) and 1 deep research run on gaps, licensing and industry. Outputs saved in research/parallel/2026-11-18/.
- Deep research at high effort timed out twice at the connector; completed at medium effort.

Format changes made after reviewing the Parallel runs
- Added `status_category` (normalised) alongside `status` (Microsoft's wording), with a Mixed value for announcements whose parts sit at different stages.
- Added `ignite_scope` to separate stage announcements from adjacent November partner and licensing news.
- Added `licensing` because several items carry licence prerequisites.
- Added `secondary_source` and `verification` so each row shows what kind of page it rests on.
- Replaced one third-party citation with the official Office blog.
- LLM.TXT lines now start with the status in square brackets, grouped by product family, and end with the source URL and id.
- Spreadsheet gained Summary and Sources tabs.

Known gaps
- No official Ignite announcements found yet for Power Apps, Power Automate or Security Copilot; Teams Ignite post and most industry news still to read.
