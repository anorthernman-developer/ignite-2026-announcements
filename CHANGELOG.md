# Change log

All dates and times are UK time (GMT).

## 23 November 2026, 09:45 GMT: run 3, Parallel deep research and monitor sweep

Added (13 announcements, total now 144)
- Microsoft Foundry (2): browser automation, computer use and A2A tool GA, with Work IQ and Fabric IQ integrations in preview; hosted agents scale and enterprise controls (shared subnet IPs GA, other controls in public preview). Source: Microsoft Foundry Blog, 18 Nov 2026.
- Azure API Management (3): Azure AI Gateway GA as a standalone service; Agent 365 integration with API Management and AI Gateway GA; Premium v2 in 35 Azure regions. Source: Azure API Management Ignite post, 17 Nov 2026.
- Azure Functions (4): Managed Connectors GA; Durable Task Scheduler and Durable Extension for Microsoft Agent Framework (GA and preview); hosted skills, agent bindings, Canvas and Skills (public preview); Go and .NET 11 GA, Python 3.15 and Node.js 26 in preview. Source: Azure Functions Ignite post, 17 Nov 2026.
- Microsoft Intune (1): Vulnerability Remediation Agent (limited public preview). Source: Intune Ignite post.
- SharePoint (1): Work IQ context enhancements (public preview from November). Source: SharePoint and OneDrive Ignite post.
- Edge for Business (1): writing assistance and Journeys (preview). Source: Edge for Business Ignite post, 17 Nov 2026.
- Microsoft Sentinel (1): automation audit logs and Data and Connectors overview (public preview), ingest-time normalisation (public preview December 2026), Connector Builder Agent (GA by end of November). Source: Sentinel Ignite post, 16 Nov 2026.

How the run went
- Deep research was requested at high effort and timed out at the Parallel MCP connector. It completed at medium effort with the same prompt.
- The monitor sweep (Parallel web search with the monitor query) returned 10 official pages; 4 had not been cited before and gave 10 of the new rows.
- Every new row was checked on its official page on 23 November 2026. Raw outputs are in research/parallel/2026-11-23/.

Checked and unchanged
- No status changes found for existing rows.
- Edge Cowork agentic browsing and the Entra MCP Server for IT admins were already covered by existing rows. SharePoint Knowledge Base and Copilot in SharePoint GA were released in October, before Ignite, so they were not added.

Known gaps
- Security Copilot and industry solutions beyond Dragon Copilot: still no official Ignite announcement found.
- Edge interactive brief and Microsoft 365 Resources for Agents in Foundry: no release status on the official page, so not added.

## 23 November 2026, 09:00 GMT: run 2, post-event update

Added (11 announcements, total now 131)
- Microsoft Teams (3): Agentic Users (public preview); agent threads, plans and steps, HTML widgets and socket mode (public preview); streaming and extended Markdown for agents (available now). Source: Microsoft 365 Developer Blog, 17 Nov 2026.
- Viva Engage (4): Community Agent updates (public preview); Communities in Teams (GA); communication plans (private preview); Engage plugin and 17 skills for Copilot Cowork. Source: Viva Engage Tech Community post, 17 Nov 2026.
- Power Platform (4): Copilot in canvas apps (GA, November 2026); business applications in Work IQ (public preview); hybrid authoring with agents through MCP servers; quality and maker improvements. Source: Power Platform blog, 18 Nov 2026, and the October/November feature update.

Checked and unchanged
- The live news blog (shows the keynote entries only) and the Book of News: every Book of News item was already in the data. No status changes found.

Fixes
- Ids and first_seen dates are now carried over from the previous data/announcements.json, so adding rows no longer renumbers existing ids.
- README count tables refreshed; taxonomy product lists regenerate from data.py (new products: Viva Engage, Power Apps, Power Platform).
- Spreadsheet is rebuilt by the GitHub Actions workflow (build.yml) on push to scripts/.

Known gaps
- No Ignite-dated official post found for Security Copilot. The Learn what's-new page has no Ignite entries yet.
- Teams Channel Backup (private preview) and Teams real-time transcripts are reported only by third parties so far; not added.
- Power Platform Studio is mentioned only in third-party posts; not added.
- The two earlier scheduled runs left no trace in the repository (no commits, and the only recorded workflow run succeeded), so they failed before pushing anything. The exact error is not visible from here.

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
