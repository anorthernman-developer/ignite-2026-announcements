# Parallel runs, 18 November 2026

Four Parallel runs fed the first build: three test runs split by area and one deep research run aimed at gaps.

| Run | Focus | Items returned | File |
| --- | --- | --- | --- |
| Test run 1 | Copilot, Copilot Studio, Agent 365, Microsoft IQ, Foundry and MAI models | 53 | [test-run-1-copilot-agents-models.md](test-run-1-copilot-agents-models.md) |
| Test run 2 | Azure infrastructure, Foundry, Fabric, databases, GitHub, Azure Local and sovereign cloud | 63 | [test-run-2-azure-data-github.md](test-run-2-azure-data-github.md) |
| Test run 3 | Security, Microsoft 365 apps, Windows and Windows 365, Dynamics 365, Power Platform, partnerships | 49 | [test-run-3-security-m365-windows.md](test-run-3-security-m365-windows.md) |
| Deep research | Power Platform, Teams, SharePoint, Purview, Intune, Edge, licensing, partner programme, retirements, industry | 51 (including flagged gaps) | [deep-research-gaps-licensing-industry.md](deep-research-gaps-licensing-industry.md) |

## What the review found

1. The live news blog alone covers about 15 headline items. The Book of News and the product blogs it links to hold the detail, so the Book of News is now the primary index for every run.
2. The three test runs overlapped on about 10 items (Perception, Agent 365, Microsoft IQ, Windows 365 for Agents). These were merged into one row each, with a secondary source.
3. Several runs mixed in news published before Ignite (for example GitHub Enterprise including Copilot, 28 October 2026) and Partner Center items from November. These are kept but marked with `ignite_scope` so they can be filtered out.
4. Many announcements have parts at different stages (for example ISOC: core GA, SIEM breadth in preview). A single status column hid this, so a normalised `status_category` with a Mixed value was added, and the free-text `status` keeps Microsoft's words.
5. Licence prerequisites came up often (Agent 365 Business Analytics needs at least one Microsoft 365 Copilot licence; ISOC opt-in needs Defender Suite, E5 or E7). A `licensing` column was added.
6. Runs 3 and the deep research could not find official Ignite announcements for Power Apps, Power Automate, Security Copilot, retail, manufacturing or public sector. These are listed as gaps, not rows.
7. One run cited a third-party site (windowsreport.com) for Copilot in OneNote. That row cites the official Office blog instead.

## Deep research note

The deep research run was asked for at high effort. Two attempts at high effort timed out at the Parallel MCP connector (the connector waits synchronously). The run completed at medium effort with the same prompt. For a true high-effort run, use the Parallel web app or API with the prompt in [../../../search-terms/parallel-search-terms.md](../../../search-terms/parallel-search-terms.md).

## Gaps to check on the next run

- Power Apps and Power Automate Ignite news
- Security Copilot Ignite news
- Teams, Teams Phone and Teams Rooms Ignite post ("What's new in Microsoft Teams | Microsoft Ignite 2026")
- Industry announcements beyond Dragon Copilot
- Region lists for GA items
