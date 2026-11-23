# Parallel runs, 23 November 2026

Run 3 of the tracker: one Parallel deep research run and one monitor-style sweep, compared with data/announcements.xlsx (131 rows before this run).

| Run | Effort or mode | Status | Items returned | Files |
| --- | --- | --- | --- | --- |
| Deep research (prompt from search-terms section 2) | High requested, timed out at the Parallel MCP connector; medium used | Completed at medium (`effort_used: medium`) | 37 catalogue rows plus flagged gaps | [deep-research-medium.md](deep-research-medium.md), [deep-research-medium.json](deep-research-medium.json) |
| Monitor sweep (query from search-terms section 1) | Parallel web_search, 5 queries | Completed | 10 official pages | [monitor-sweep.md](monitor-sweep.md), [monitor-sweep.json](monitor-sweep.json) |
| Verification fetches | Parallel web_fetch of 7 official pages | Completed | Release status checked on each page | verification-fetch-*.json |

## What was added (13 rows, total now 144)

Each row was checked on the official page named, read on 23 November 2026.

| Title | Status | Source |
| --- | --- | --- |
| Foundry Agent Service browser automation, computer use and A2A tool generally available | Mixed: GA and preview | Microsoft Foundry Blog, 18 Nov 2026 |
| Foundry hosted agents scale and enterprise controls | Mixed: GA and public preview | Microsoft Foundry Blog, 18 Nov 2026 |
| Azure AI Gateway generally available as a standalone service | GA | Azure API Management Ignite post, 17 Nov 2026 |
| Agent 365 integration with Azure API Management and Azure AI Gateway | GA | Azure API Management Ignite post |
| API Management Premium v2 in 35 Azure regions | Available | Azure API Management Ignite post |
| Managed Connectors in Azure Functions generally available | GA | Azure Functions Ignite post, 17 Nov 2026 |
| Durable Task Scheduler and Durable Extension for Microsoft Agent Framework | Mixed: GA and public preview | Azure Functions Ignite post |
| Azure Functions hosted skills, agent bindings, Canvas and Skills | Public preview | Azure Functions Ignite post |
| Azure Functions runtimes: Go and .NET 11 GA, Python 3.15 and Node.js 26 preview | Mixed | Azure Functions Ignite post |
| Intune Vulnerability Remediation Agent | Limited public preview | Intune Ignite post |
| SharePoint Work IQ context enhancements | Public preview, rolling out from November | SharePoint and OneDrive Ignite post |
| Edge for Business writing assistance and Journeys | Preview | Edge for Business Ignite post, 17 Nov 2026 |
| Sentinel automation audit logs, ingest-time normalisation and Connector Builder Agent | Mixed: public preview; GA end of November | Sentinel Ignite post, 16 Nov 2026 |

## What the review found

1. Most of the deep research catalogue (about 30 of 37 rows) matched rows already in the data. It added 4 candidates: Intune Vulnerability Remediation Agent, SharePoint Work IQ context enhancements, Edge Cowork agentic browsing and Entra MCP Server for IT admins.
2. Edge Cowork agentic browsing is already covered by "Copilot Cowork updates" (Cowork in Edge for Business GA). Entra MCP Server for IT admins matches "Microsoft MCP Server for Enterprise". Neither was added.
3. SharePoint Knowledge Base (Frontier, October) and Copilot in SharePoint GA (October) were released before Ignite. Not added.
4. The sweep found 4 official product posts not cited before (Foundry Agent Service, API Management, Azure Functions, Sentinel). These gave 10 of the 13 new rows. Product-level "what's new at Ignite 2026" posts on Tech Community and devblogs are the richest remaining source.
5. No status changes were found for existing rows (no preview to GA moves since 18 November).
6. Not added because status was not stated on the page: Edge interactive brief, Microsoft 365 Resources for Agents in Foundry.

## Deep research note

High effort timed out at the Parallel MCP connector again (third time across runs). Medium completed in about 65 seconds. For a true high-effort run, use the Parallel web app or the asynchronous Task API.

## Gaps still open

- Security Copilot: no Ignite-dated official post found by either run.
- Industry solutions beyond Dragon Copilot: none verified.
- Teams Channel Backup and Teams real-time transcripts: still third-party only.
- Region lists for most GA items are not published.
