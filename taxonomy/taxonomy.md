# Taxonomy

How every announcement is classified. The machine-readable version is [taxonomy.json](taxonomy.json). Values in the spreadsheet and JSON come only from this list.

## Product hierarchy

Three levels: product family > product > capability area.

### Microsoft Copilot

Microsoft 365 Copilot, the Copilot app, Office in Copilot, Cowork, Code, Autopilot, SharePoint, OneDrive, Teams and Viva Engage experiences.

- Autopilot: Autonomous agents
- Copilot Code: App building
- Copilot Cowork: Agentic work
- Copilot Managed Runtime: Agent building, App hosting
- Copilot Pages: Content creation
- Copilot for Sales: Role skills
- Copilot in OneDrive: Content
- Copilot in OneNote: Content creation
- Copilot plugins: Extensibility
- Microsoft Copilot app: Collaboration, Copilot experience, Office apps, Proactive assistance
- Microsoft Teams: Agent experiences, Agent identity, Meeting security
- SharePoint: Content governance
- Viva Engage: Communities, Community Agent, Copilot and Cowork, Employee communications

### Agents and agent governance

Building, running, governing and paying for agents: Agent 365, Copilot Studio, Windows 365 for Agents.

- Microsoft Agent 365: Adoption, Connected platforms, Discovery, FinOps for AI, Governance, Observability, Risk
- Microsoft Copilot Studio: Agent building
- Windows 365 for Agents: Computer use

### Microsoft IQ

Enterprise context layer: Microsoft IQ, Work IQ, Fabric IQ, Foundry IQ, Web IQ.

- Fabric IQ: Business context
- Foundry IQ: Knowledge retrieval
- Microsoft IQ: Enterprise context
- Web IQ: Web grounding
- Work IQ: Context and actions

### AI models and Microsoft Foundry

Models (MAI, OpenAI, Meta, Microsoft-Decision), Microsoft Foundry platform services and AI silicon.

- Dragon Copilot: Clinical documentation
- MAI models: Coding models, Image models, Model access, Productivity models, Security models, Speech models
- Maia: AI silicon
- Microsoft Foundry: Agent harness, Continuous improvement, Model catalogue, Model routing
- Microsoft-Decision-1.1: Decision models

### Azure infrastructure and operations

Azure compute, operations, migration, AI infrastructure, Azure Local, sovereign cloud and Windows Server.

- Azure AI infrastructure: AI infrastructure
- Azure Catalyst: Migration and modernisation
- Azure Chaos Studio: Resilience
- Azure Copilot: Agentic operations
- Azure Local: Confidential computing, Sovereign and hybrid
- Azure Monitor: Observability
- Azure Resource Manager: Agentic operations
- Azure SRE Agent: Agentic operations
- Azure Virtual Machines: Compute
- Azure Workload Center: SAP and Oracle
- Azure confidential computing: Confidential computing
- Microsoft Sovereign Cloud: Sovereignty
- Windows Server: Server OS

### Data and databases

Microsoft Fabric, Power BI and Azure databases (HorizonDB, SQL, Cosmos DB, DocumentDB, PostgreSQL, Redis).

- Azure Cosmos DB: Databases
- Azure Database for PostgreSQL: Databases
- Azure DocumentDB: Databases
- Azure HorizonDB: Databases
- Azure Managed Redis: Databases
- Azure SQL: Databases
- Microsoft Fabric: App development, Database management, Databases
- Power BI: Data apps

### Developer tools and GitHub

GitHub Copilot, GitHub Enterprise, Copilot SDK and developer tooling.

- GitHub Copilot: Code review, Copilot app, Models, Modernisation, Quality
- GitHub Enterprise: Licensing
- Microsoft Copilot SDK: Agent runtime

### Security, identity and compliance

Microsoft Perception, Defender, Sentinel, Entra, Purview, Baseline Security Mode, MDASH and responsible AI.

- Codename MDASH: Code security
- Microsoft Agent 365: Security partnerships
- Microsoft Baseline Security Mode: Secure by default
- Microsoft Defender: Agent security, Attack disruption, Endpoint security, On-premises security, Security operations
- Microsoft Entra: Access control, Agent identity, Authentication, Platform
- Microsoft Perception: Agentic security
- Microsoft Purview: Classification, Data security for AI, Network DLP
- Microsoft Sentinel: SIEM connectors
- Responsible AI: AI governance

### Windows, Windows 365 and endpoint management

Windows 11, Windows 365, Intune and endpoint management.

- Microsoft Intune: Endpoint management
- Windows 11: Agent containment, Copilot on Windows, Platform security
- Windows 365: Cloud PC

### Microsoft Edge

Edge for Business security and governed AI browsing.

- Edge for Business: Browser security, Governed AI

### Business applications

Dynamics 365, Power Apps, Power Platform and contact centre.

- Dynamics 365: Copilot plugins, Migration
- Dynamics 365 Contact Center: Contact centre
- Power Apps: Copilot in apps
- Power Platform: Agentic authoring, Platform quality, Work IQ

### Partnerships and ecosystem

Strategic partnerships announced at Ignite (for example Salesforce).

- Salesforce: Partnership

### Licensing, pricing and partner programme

Licensing, pricing, billing, retirements and partner programme changes.

- AI Builder: Retirement
- Business Central: Bundles
- Copilot Business: Billing
- Microsoft 365 Copilot: Licensing
- Microsoft AI Cloud Partner Program: Partner programme
- Microsoft Purview: Retirement

### Industry solutions

Industry-specific solutions (healthcare, financial services, public sector and others).


## Announcement type

What kind of news it is.

| Value | Definition |
| --- | --- |
| New product | A product or service that did not exist before. |
| New capability | A new feature in an existing product. |
| New model | A new AI model or model family. |
| New version | A new major version of an existing product. |
| Status change | A move between release stages, usually preview to GA. |
| Update | A bundle of improvements to an existing product. |
| Mixed | One announcement with parts at different stages. |
| Default change | A change to default settings or behaviour. |
| Pricing / licensing | Price, SKU, billing or licence terms. |
| Retirement | End of sale, end of support or removal. |
| Partnership | A named commercial or technical partnership. |
| Industry initiative | A multi-organisation effort or standard. |
| New programme | A customer or partner programme. |
| Milestone | A usage or scale figure shared on stage. |

## Status category

Normalised release stage used for filtering. The free-text status column keeps Microsoft's own wording.

| Value | Definition |
| --- | --- |
| GA | Generally available for production use. |
| Public preview | Open preview, any eligible customer can try it. |
| Private or limited preview | Invitation, eligibility or limited-access preview. |
| Preview (stage not stated) | Microsoft says preview without saying public or private. |
| Frontier | Microsoft's early-access programme for Copilot and agents. |
| Coming soon | Announced with no current access. |
| Mixed | Parts of the announcement sit at different stages; see the status column. |
| Licensing change | A dated licensing or billing change. |
| Retirement | Being retired or removed. |
| Announced | Announced with no stage given. |
| Milestone | A figure, not a product change. |

## Audience

Primary reader the announcement is aimed at.

| Value | Definition |
| --- | --- |
| Business decision makers | Budget holders and leaders deciding on spend and value. |
| IT pros and admins | People who deploy, manage and govern. |
| Security teams | SOC, identity, data security and compliance. |
| Developers | People who build apps, agents and integrations. |
| Data professionals | Analysts, data engineers and BI developers. |
| End users | Everyday users of Copilot and Microsoft 365. |
| Partners | Microsoft partners, CSPs and MSPs. |

## Industry

Industry focus where stated; most items are cross-industry.

| Value | Definition |
| --- | --- |
| Cross-industry | No specific industry. |
| Healthcare | Clinical and health organisations. |
| Financial services | Banks, insurers, capital markets. |
| Public sector | Government, defence, sovereign requirements. |
| Retail | Retail and consumer goods. |
| Manufacturing | Manufacturing and industrial. |

## Ignite scope

Whether the item was announced at Ignite or is adjacent news from the same period.

| Value | Definition |
| --- | --- |
| Ignite 2026 | Announced at Ignite 2026 (live news, Book of News or Ignite-dated official blogs). |
| Adjacent (November partner announcements) | Partner Center or licensing news published in November 2026. |
| Adjacent (28 Oct 2026, pre-Ignite) | Published before Ignite but directly relevant. |
| Ignite window (docs) | Documented in product docs during the Ignite window. |

## Verification

Which kind of source the row rests on.

| Value | Definition |
| --- | --- |
| Book of News | Confirmed in the Ignite 2026 Book of News. |
| Live news + official blog | Confirmed on the live news blog and an official blog. |
| Official blog | Confirmed on an official Microsoft, Azure, Windows, Dynamics 365 or Tech Community blog. |
| Microsoft AI blog | Confirmed on microsoft.ai news. |
| Book of News + Microsoft AI blog | Confirmed in the Book of News and on microsoft.ai. |
| Live news + Microsoft AI blog | Confirmed on the live news blog and on microsoft.ai. |
| Live news + Microsoft Source | Confirmed on the live news blog and Microsoft Source. |
| GitHub changelog | Confirmed on the GitHub changelog. |
| Partner Center announcements | Confirmed on Microsoft Learn Partner Center announcements. |
| Official docs (Defender for Office 365 what's new) | Confirmed in Microsoft Learn docs. |
| Parallel deep research (official blog) | Found by Parallel deep research citing an official blog; to be re-read on the next run. |

## Region

Region availability where Microsoft states it; otherwise 'Not stated'.

| Value | Definition |
| --- | --- |
| Not stated | Microsoft did not give regions. |
| Named regions | See the region column. |
