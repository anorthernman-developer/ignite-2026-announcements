# Parallel runs, 24 November 2026

Run 4 of the tracker: one Parallel deep research run and one monitor-style sweep, compared with data/announcements.xlsx (144 rows before this run).

| Run | Effort or mode | Status | Items returned | Files |
| --- | --- | --- | --- | --- |
| Deep research (prompt from search-terms section 2, plus the LLM.TXT exclusion line) | `parallel-cli research run --processor pro --text --no-wait`, then a bounded poll. Run id `trun_249f1a154b18481793415ee62232ff0b` | Completed at pro (high effort) in about 6 minutes. No fallback needed | 15 candidate rows, all already in the data | [deep-research-pro.md](deep-research-pro.md), [deep-research-pro.json](deep-research-pro.json) |
| Monitor sweep (query from search-terms section 1) | `parallel-cli search`, mode advanced, `--after-date 2026-11-17`, 5 keyword queries, 20 results | Completed | 20 official pages, 6 not cited before | [monitor-sweep.md](monitor-sweep.md), [monitor-sweep.json](monitor-sweep.json) |
| Verification fetches | `parallel-cli extract` of 7 official pages and the Book of News | Completed | Release status checked on each page | verification-fetch-*.json |

## What was added (15 rows, total now 159)

Each row was checked on the official page named, read on 24 November 2026.

| Title | Status | Source |
| --- | --- | --- |
| Frontier Tuning private preview expands, with tools for makers and experts | Private preview (expanded) | Microsoft 365 Developer Blog, 18 Nov 2026 |
| Dynamics 365 ERP and Copilot Cowork in Business Applications in Work IQ | Public preview | Dynamics 365 blog, 18 Nov 2026 |
| Foundry Toolboxes: skills, Web IQ web search and new catalogue partners | Mixed: public preview; GA coming soon | Microsoft Foundry Blog, 18 Nov 2026 |
| Voice agents in Foundry Agent Service generally available, with new speech-to-speech models | Mixed: GA and preview | Microsoft Foundry Tech Community post, 18 Nov 2026 |
| Azure Managed Redis migration tooling, keyspace notifications, shard metrics and IP filtering | Mixed: GA and public preview | Azure Managed Redis Ignite post, 17 Nov 2026 |
| SharePoint Governance Hub for admins and site owners | Mixed: GA December 2026; public preview | SharePoint content governance post, 17 Nov 2026 |
| SharePoint restricted access for apps and agents and agentic user collaboration limits | Mixed: GA; public preview December 2026 | As above |
| SharePoint App Intelligence and Content Events | Mixed: GA December 2026; private preview | As above |
| Automated file-level archive and inactive file policy in SharePoint | Mixed: GA and public preview | As above |
| SharePoint storage pay-as-you-go meter and tenant-wide version trimming | Mixed: public preview; GA January 2027 | As above |
| Multi-Geo default geo move for SharePoint and OneDrive | Public preview | As above |
| Agent rewind for Microsoft 365 | Private preview | As above |
| Teams Channel Backup and longer backup retention in Microsoft 365 Backup | Mixed: private preview; GA | As above |
| Microsoft Entra Backup and Recovery Premium | Public preview | As above |
| Information Barriers: Teams Explicit Mode and Agent Builder sharing | Mixed: public preview and GA | As above |

## Status changes and corrections to existing rows

- Business applications in Work IQ (IGN26-BIZ-005): public preview to GA on 18 Nov 2026. Source: [Dynamics 365 blog](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/11/18/business-applications-work-iq-generally-available/).
- SharePoint Admin Agent (IGN26-COP-017): Announced to GA; Agent Access Heatmap GA December 2026. Source: SharePoint content governance post.
- Azure Managed Redis previews Redis 8 and an agent kit (IGN26-DATA-005): preview stage confirmed as public preview.
- Confidential computing expansion and the Foundry/AKS infrastructure row: summaries now include Azure Confidential Clean Room and Flex nodes for AKS, both in the Book of News but missing from the summaries.

## What the review found

1. The deep research run at pro said itself that it could not complete the comparison with LLM.TXT. Its 15 candidates (Chaos Studio, confidential computing, Azure Monitor, Azure Copilot, Workload Center, Foundry on AKS, Agent Grid, Agent Sandbox, Flex nodes, Windows Server 2028) were all already in the data; two were missing from summaries and are now included.
2. The sweep gave every new row. One SharePoint content governance post on Tech Community carried 10 of them, including Teams Channel Backup, which was a known gap (third-party only) until now.
3. Pages in the sweep already covered by existing rows: Foundry hosted agents, Copilotforce (news.microsoft.com URL variant), Azure AI Gateway GA post.

## Gaps still open

- Security Copilot: no Ignite-dated official post found by either run.
- Industry solutions beyond Dragon Copilot: none verified.
- Teams real-time transcripts: still third-party only.
- Region lists for most GA items are not published.
