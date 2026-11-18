# Test run 2: Azure, data, GitHub and sovereign cloud

- Run date: 18 November 2026 (Europe/London)
- Tool: Parallel web_research via MCP
- Reasoning effort: medium
- Response id: resp_62a185c1-9e69-4a47-b2bb-d6def4f73fb6
- Prompt: List every Ignite 2026 announcement about Azure infrastructure and compute, Microsoft Foundry, Microsoft Fabric, Azure databases, GitHub and developer tools, Azure Local and sovereign cloud, with status, availability or regions and official source URL.

Output below is unedited Parallel output. Treat it as research input, not a source. Rows in the spreadsheet cite the Microsoft pages, not this file.

---

## Microsoft Ignite 2026 announcements in the requested scope

**Scope note.** The list below includes announcements explicitly tied to Microsoft Ignite 2026, held November 17–20, 2026. Items announced before Ignite are excluded unless Microsoft’s Ignite materials introduced a distinct Ignite status or capability. The official Microsoft Ignite Book of News is the primary index.

### Azure infrastructure, compute and operations

- **Azure Cobalt 200 virtual machines** — General availability of Arm-based Cobalt 200 VMs, with up to 50% better CPU performance than Cobalt 100; new Mpsv4 high-memory and Lpsv5 storage-optimized families, including up to 23 TB of local storage. **Status:** GA. **Availability:** 14 regions at announcement, expanding to 23 regions by the end of 2026; named existing regions include Australia East, Central US, East US, Indonesia Central, Italy North, South Central US, Spain Central, Sweden Central, UK South, West US 2 and West US 3. **Official source:** https://azure.microsoft.com/en-us/blog/azure-cobalt-200-vms-now-available-proven-on-real-workloads-and-built-for-the-agentic-era

- **Cobalt 200 compute for Azure Database for PostgreSQL Flexible Server** — Microsoft-designed Arm64 compute was added alongside Intel and AMD x64 options. **Status:** GA. **Availability:** November 2026; specific regions were not stated in the cited Ignite announcement. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Maia 300** — Microsoft announced its next-generation custom AI accelerator, claiming 40% more tokens per watt than leading GPU systems. **Status:** coming soon. **Availability:** production deployments begin in 2027; no customer region list was stated. **Official source:** https://blogs.microsoft.com/blog/2026/11/17/ignite-2026-building-the-frontier-ecosystem

- **Azure AI infrastructure foundation** — New infrastructure for production AI spanning agent networking, security, isolation, confidentiality, context and state; Foundry-to-AKS deployment lets customers choose GPUs and regions based on cost, latency and data residency. **Status:** preview unless otherwise specified; the Book of News states that Cobalt 200 is the exception and is GA. **Availability:** no specific regions or date stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Agent Grid** — Secure, policy-controlled networking among agents, models, tools and Azure services. **Status:** preview. **Availability:** not stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Agent Sandbox extension for AKS** — VM-level isolation for agent-generated code, including pre-warmed pools and a serverless option. **Status:** preview. **Availability:** not stated. **Official source:** https://azure.microsoft.com/en-us/blog/introducing-azure-catalyst-agentic-modernization-and-new-ai-infrastructure-innovations

- **Flex nodes for AKS** — Extends an AKS cluster with worker capacity in other Azure regions, on-premises or at the edge under one control plane. **Status:** public preview. **Availability:** available at announcement; no region list was stated. **Official source:** https://blog.aks.azure.com/2026/09/22/flex-nodes-for-aks

- **Foundry models and agents on AKS** — Customers can deploy open-weight models and agents from Microsoft Foundry to their own AKS clusters, with Foundry handling setup and governance. **Status:** preview. **Availability:** customers choose supported GPUs and regions; no fixed region list was stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Azure confidential computing** — VR72 multi-GPU confidential computing, Azure Confidential Enclaves and AKS Kata CoCo confidential containers. **Status:** preview. **Availability:** no regions or date stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Azure Chaos Studio Workspaces and AKS extension** — Workspaces and the AKS extension became generally available for organizing and running resilience tests, including controlled disruption of Kubernetes pods. **Status:** GA. **Availability:** no region list stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Azure Monitor health models** — GA health models turn telemetry into application-health context tied to architecture, dependencies and business impact. **Status:** GA. **Availability:** not stated. **Official source:** https://techcommunity.microsoft.com/blog/azureinfrastructureblog/advancing-agentic-operations-on-azure-at-ignite-2026/4573831

- **Azure Copilot deployment agent** — Translates natural-language requirements into infrastructure and deployment code. **Status:** GA. **Availability:** not stated. **Official source:** https://techcommunity.microsoft.com/blog/azureinfrastructureblog/advancing-agentic-operations-on-azure-at-ignite-2026/4573831

- **Azure Copilot spaces and custom skills** — Persistent context and organization-specific operational knowledge for Azure operations. **Status:** public preview. **Availability:** not stated. **Official source:** https://techcommunity.microsoft.com/blog/azureinfrastructureblog/advancing-agentic-operations-on-azure-at-ignite-2026/4573831

- **Azure Workload Center for Oracle and SAP** — Agentic workload-health monitoring and configuration validation. **Status:** limited/private preview. **Availability:** not stated. **Official source:** https://techcommunity.microsoft.com/blog/azureinfrastructureblog/advancing-agentic-operations-on-azure-at-ignite-2026/4573831

- **Azure SRE Agent** — New enterprise controls, Microsoft Entra Agent ID, Microsoft Agent 365 integration, cross-agent communication and Teams/multicloud investigations. **Status:** public preview for the new capabilities. **Availability:** November 17, 2026; no region list stated. **Official source:** https://techcommunity.microsoft.com/blog/azureinfrastructureblog/advancing-agentic-operations-on-azure-at-ignite-2026/4573831

- **Azure Resource Manager MCP Server** — Agents can take governed action across Azure, with requests evaluated under Azure Policy. **Status:** GA for the deployment/action capability described at Ignite. **Availability:** not stated. **Official source:** https://techcommunity.microsoft.com/blog/azureinfrastructureblog/advancing-agentic-operations-on-azure-at-ignite-2026/4573831

- **Azure Catalyst** — A unified Azure-and-GitHub experience for AI-assisted discovery, planning, migration, modernization and code intelligence across infrastructure, applications and data. **Status:** GA; the Azure Catalyst agent is also GA, while deeper modernization and execution capabilities are in preview. **Availability:** no regions stated. **Official source:** https://azure.microsoft.com/en-us/blog/introducing-azure-catalyst-agentic-modernization-and-new-ai-infrastructure-innovations

### Microsoft Foundry / Azure AI Foundry

- **Microsoft Foundry continuous-improvement loop** — Establish, identify, optimize and validate workflows for improving agents using production observations; cost optimization is in preview and Programmed Training lets engineers write Python training recipes executed on serverless GPUs. **Status:** cost optimization and Programmed Training public preview; Voice agents GA; hosted-agent deployment to AKS coming soon/in preview. **Availability:** no regions stated. **Official source:** https://azure.microsoft.com/en-us/blog/continuous-improvement-comes-to-microsoft-foundry/

- **Microsoft-Decision-1.1 in Foundry** — Fast, cost-effective decision model for routing, classification, prioritization, verification and workflow control, also usable as a judge in Foundry Evaluations. **Status:** GA. **Availability:** available at Ignite; no regions stated. **Official source:** https://azure.microsoft.com/en-us/blog/continuous-improvement-comes-to-microsoft-foundry/

- **MAI Code 2 and MAI Code 2 Flash in Foundry** — Agentic coding models for complex repository-wide work and high-volume everyday coding. **Status:** MAI Code 2 GA in GitHub Copilot; Code 2 Flash private preview in Foundry. **Availability:** available at Ignite for eligible access; no region list stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Microsoft Copilot harness in Foundry** — Managed harness with reusable skills and sub-agents. **Status:** preview. **Availability:** not stated. **Official source:** https://azure.microsoft.com/en-us/blog/continuous-improvement-comes-to-microsoft-foundry/

- **Agent service on Azure Local through Foundry Local** — Build and orchestrate agents in fully disconnected environments; guardrails can use a customer-selected guardrail model. **Status:** agent service and guardrails public preview. **Availability:** on Azure Local in connected or disconnected environments; no regions stated. **Official source:** https://techcommunity.microsoft.com/blog/azurearcblog/whats-new-with-sovereign-private-cloud-at-microsoft-ignite-2026/4573886

### Microsoft Fabric

- **Fabric HorizonDB** — Serverless, Fabric-native PostgreSQL for applications, analytics and AI; it can automatically provision, pause after inactivity and resume on demand, and serve as the backend for Fabric apps. **Status:** public preview. **Availability:** no regions stated. **Official source:** https://azure.microsoft.com/en-us/blog/microsoft-ignite-2026-whats-new-in-azure-the-platform-purpose-built-for-ai

- **Database Hub in Fabric** — Unified discovery, monitoring and management of databases across Azure, Fabric, on-premises environments and supported multicloud environments. **Status:** GA. **Availability:** November 2026; no regions stated. **Official source:** https://learn.microsoft.com/en-us/fabric/fundamentals/whats-new?pivots=fabric

- **Database agents in Fabric** — AI-assisted SQL and PostgreSQL investigation, recommendations and approved operational actions in Database Hub and the PostgreSQL VS Code extension. **Status:** preview. **Availability:** not stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Rayfin and Fabric apps** — Application-development stack combining data, APIs, authentication, hosting, governance and observability, with SQL database or Fabric HorizonDB as backend choices. **Status:** GA. **Availability:** no regions stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Fabric IQ integrations** — Integrations across Microsoft Copilot, Fabric apps, Excel, GitHub Copilot, ChatGPT and Claude bring governed business context into applications and agents. **Status:** GA for the Copilot/Fabric apps integrations; preview for Excel, GitHub Copilot ontologies and ChatGPT/Claude connectors. **Availability:** no regions stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Copilot Managed Runtime with Fabric backend** — GA hosting and governance for apps built with Microsoft Copilot and compatible third-party development tools, with an optional Fabric data backend. **Status:** GA. **Availability:** no regions stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

### Databases

- **Azure HorizonDB** — Fully managed PostgreSQL-compatible database for mission-critical and AI-powered applications, with vector search, AI Functions, AI Pipelines and model management. **Status:** GA; AI model management, AI Functions and AI Pipelines are preview capabilities. **Availability:** no regions stated. **Official source:** https://techcommunity.microsoft.com/blog/azuresqlblog/whats-new-in-databases-at-microsoft-ignite-2026-ai-ready-data-for-apps-and-agent/4570764

- **Azure HorizonDB mirroring into Fabric** — Makes operational HorizonDB data available for Fabric analytics alongside other business data. **Status:** preview. **Availability:** not stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Azure Cosmos DB Shell** — Interactive query, management, import/export and MCP-enabled workflows in the terminal, VS Code and Azure portal. **Status:** GA. **Availability:** those three surfaces; no regions stated. **Official source:** https://devblogs.microsoft.com/cosmosdb/whats-new-azure-cosmos-db-ignite-2026/

- **Azure Cosmos DB extension for VS Code with AI-assisted data modeler** — Account insights, partition-key and container recommendations, hot-partition analysis and configuration generation. **Status:** public preview. **Availability:** VS Code; no regions stated. **Official source:** https://devblogs.microsoft.com/cosmosdb/whats-new-azure-cosmos-db-ignite-2026/

- **Azure Cosmos DB Rust SDK** — Native Rust client with retries, partition-level failover, circuit breaking and efficient binary encoding. **Status:** GA. **Availability:** no regions stated. **Official source:** https://devblogs.microsoft.com/cosmosdb/whats-new-azure-cosmos-db-ignite-2026/

- **Managed MCP Server for Azure Cosmos DB** — Microsoft-managed endpoint for agents to discover schemas, retrieve documents and use full-text, vector and hybrid search with Azure identity and RBAC. **Status:** public preview. **Availability:** not stated. **Official source:** https://devblogs.microsoft.com/cosmosdb/whats-new-azure-cosmos-db-ignite-2026/

- **Automatic embedding generation and Microsoft.Embedding-1 for Cosmos DB** — Embeddings can be generated where the data resides; Microsoft.Embedding-1 supports multimodal single- and multi-vector matching. **Status:** automatic embedding generation public preview; model available through the Cosmos DB embedding-generation service. **Availability:** no regions stated. **Official source:** https://devblogs.microsoft.com/cosmosdb/whats-new-azure-cosmos-db-ignite-2026/

- **Azure Backup for Cosmos DB** — Independent vault-based protection layer with centralized backup policies, monitoring, retention and recovery. **Status:** GA. **Availability:** no regions stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Azure DocumentDB VS Code extension** — Connect to clusters, browse databases and collections, inspect documents, query and analyze query plans in VS Code. **Status:** GA. **Availability:** no regions stated. **Official source:** https://devblogs.microsoft.com/documentdb/vscode-extension-ga/

- **Near-instant Azure DocumentDB cluster provisioning** — Faster provisioning for M10–M30 clusters. **Status:** GA. **Availability:** M10 through M30 tiers; no regions stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **DocumentDB enabled by Azure Arc** — Extends Azure DocumentDB to hybrid and multicloud environments. **Status:** preview. **Availability:** hybrid and multicloud; no regions stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **DocumentDB on Azure Local** — MongoDB-compatible document workloads running on customer-controlled Azure Local infrastructure. **Status:** preview. **Availability:** Azure Local; no regions stated. **Official source:** https://techcommunity.microsoft.com/blog/azurearcblog/whats-new-with-sovereign-private-cloud-at-microsoft-ignite-2026/4573886

- **Azure SQL Managed Instance link for multi-database Always On availability groups** — Near-real-time replication from SQL Server to Azure SQL Managed Instance for migration and disaster recovery. **Status:** GA. **Availability:** supported Azure availability zones/regions as applicable; no specific region list stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Azure SQL Database container** — Run the Azure SQL Database engine locally without an Azure subscription, shared cloud instance or credit card, using the same engine, T-SQL dialect, protocols and driver behavior. **Status:** public preview. **Availability:** local development is free; cloud database and model usage remains chargeable; no region requirement stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Azure SQL Database Hyperscale cross-database querying** — Native cross-database queries across databases in the same Hyperscale elastic pool. **Status:** public preview. **Availability:** no regions stated. **Official source:** https://azure.microsoft.com/en-us/updates/

- **Azure Database Migration Service for Oracle-to-PostgreSQL migration and PostgreSQL-to-HorizonDB migration** — Oracle-to-PostgreSQL migration and managed migration of existing Azure Database for PostgreSQL workloads to Azure HorizonDB. **Status:** preview. **Availability:** no regions stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Azure Database for PostgreSQL Flexible Server compute options** — GA Cobalt 200 Arm64 compute, GA Intel and AMD v6 compute with local temporary disk, and preview Burstable v2 compute. **Status:** mixed: GA for Cobalt 200 and Intel/AMD v6; preview for Burstable v2. **Availability:** November 2026; specific regions were not stated. **Official source:** https://azure.microsoft.com/en-us/updates/

### GitHub and developer tools

- **GitHub Copilot modernization updates** — Agent governance rulebooks and bring-your-own-model support in command-line interfaces and IDEs. **Status:** GA; additional integrated application/database modernization and BizTalk-to-Azure Logic Apps migration scenarios are preview. **Availability:** no regions stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **Microsoft Copilot SDK 2.0** — Production harness based on a native Rust runtime for secure, scalable agent deployments, supported in six languages. **Status:** GA. **Availability:** six programming languages; no regions stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **GitHub Copilot app: Azure DevOps repositories** — Clone repositories, create branches, modify code, open pull requests, address review comments and optionally complete merges after checks and policies pass. **Status:** public preview. **Availability:** the Azure DevOps integration is in the Copilot app; cloud sessions are unavailable for Azure DevOps repositories. **Official source:** https://github.blog/changelog/2026-11-17-github-copilot-app-microsoft-ignite-releases

- **GitHub Copilot app: browser use** — Controlled browser automation in Chromium-based browsers through the Copilot extension. **Status:** public preview. **Availability:** Chrome and Microsoft Edge; also available in Copilot CLI, VS Code and JetBrains IDEs. **Official source:** https://github.blog/changelog/2026-11-17-github-copilot-app-microsoft-ignite-releases

- **GitHub Enterprise Server support in the Copilot app** — Work with GHES repositories, issues and pull requests from the Copilot app. **Status:** GA. **Availability:** app version 1.2.0 or later; cloud sessions are unavailable for GHES. **Official source:** https://github.blog/changelog/2026-11-17-github-copilot-app-microsoft-ignite-releases

- **MAI Code 2 and MAI Code 2 Flash in GitHub Copilot** — MAI Code 2 targets deep debugging, multi-file implementation, refactoring and repository-wide reasoning; Flash targets explanations, targeted edits and routine fixes. **Status:** available to eligible annual-plan Copilot subscribers; the Book of News describes both as GA in GitHub, while Code 2 Flash is private preview in Foundry. **Availability:** Code 2: Pro, Pro+, Max, Business and Enterprise; Code 2 Flash: Free, Student, Pro, Pro+, Max, Business and Enterprise, across listed Copilot clients. **Official source:** https://github.blog/changelog/2026-11-17-mai-code-2-and-mai-code-2-flash-in-github-copilot

- **GitHub Copilot Evals** — Repeatable tests for Copilot skills, agents and MCP tools. **Status:** public preview. **Availability:** Copilot Individual, Business and Enterprise plans. **Official source:** https://github.blog/changelog/2026-11-17-github-copilot-evals-is-now-in-public-preview

- **GitHub Copilot code review updates** — Adaptive review effort, secret detection, cross-repository context, local CLI/app reviews and repository insights. **Status:** preview for the new review capabilities; individual availability varies by capability. **Availability:** no regions stated. **Official source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

- **GitHub Copilot CLI Microsoft Entra sign-in** — Enterprise authentication for the CLI. **Status:** preview. **Availability:** no regions stated. **Official source:** https://github.blog/changelog/

- **GitHub Copilot Fusion updates** — Expanded availability, additional models and benchmark information for the multi-model coding experience. **Status:** availability expanded; the cited official Ignite index does not assign a single GA or preview label. **Availability:** github.com, Visual Studio and GitHub Mobile beta are identified in the official release index. **Official source:** https://github.blog/changelog/

### Hybrid, Azure Local and sovereign cloud

- **Foundry Local on Azure Local** — Local model catalog, agentic retrieval, MCP server and chat experience for connected and fully disconnected environments. **Status:** GA; agent service and guardrails are preview. **Availability:** Azure Local connected and disconnected operations; no region list stated. **Official source:** https://techcommunity.microsoft.com/blog/azurearcblog/whats-new-with-sovereign-private-cloud-at-microsoft-ignite-2026/4573886

- **Confidential VMs on Azure Local** — AMD SEV-SNP confidential VMs with memory encryption and attestation became generally available; Intel TDX-based confidential VMs entered preview. **Status:** GA for supported AMD EPYC processors; preview for Intel Xeon TDX. **Availability:** supported Azure Local hardware; no region list stated. **Official source:** https://techcommunity.microsoft.com/blog/azurearcblog/whats-new-with-sovereign-private-cloud-at-microsoft-ignite-2026/4573886

- **GitHub Enterprise Local** — GitHub Enterprise Server as a prebuilt Azure Local virtual appliance, keeping repositories, CI/CD workflows and development artifacts within customer-controlled boundaries. **Status:** GA. **Availability:** connected and disconnected Azure Local environments; no regions stated. **Official source:** https://techcommunity.microsoft.com/blog/azurearcblog/whats-new-with-sovereign-private-cloud-at-microsoft-ignite-2026/4573886

- **SQL Server on Azure Local** — Run enterprise SQL Server workloads on customer-controlled infrastructure in connected or disconnected environments. **Status:** GA. **Availability:** connected and disconnected Azure Local deployments; no regions stated. **Official source:** https://techcommunity.microsoft.com/blog/azurearcblog/whats-new-with-sovereign-private-cloud-at-microsoft-ignite-2026/4573886

- **Blob Storage on Azure Local** — Local cloud-native object storage for unstructured data. **Status:** preview. **Availability:** Azure Local; no regions stated. **Official source:** https://techcommunity.microsoft.com/blog/azurearcblog/whats-new-with-sovereign-private-cloud-at-microsoft-ignite-2026/4573886

- **Connected-to-disconnected operations for Azure Local** — Transition existing Azure-connected deployments to locally managed disconnected environments. **Status:** public preview. **Availability:** Azure Local; no regions stated. **Official source:** https://techcommunity.microsoft.com/blog/azurearcblog/whats-new-with-sovereign-private-cloud-at-microsoft-ignite-2026/4573886

- **Sovereign Control Panel** — Unified Azure portal experience to assess sovereignty posture, identify affected resources and gaps, review continuity posture and support remediation. **Status:** public preview. **Availability:** entering public preview at Ignite; no regions stated. **Official source:** https://blogs.microsoft.com/blog/2026/10/20/advancing-digital-sovereignty-with-greater-control-and-choice

- **Microsoft Sovereign Private Cloud specialization** — Azure Local for Hybrid and Sovereign Private Cloud specialization launched in the Microsoft Cloud Partner Program. **Status:** launched at Ignite. **Availability:** partner-program availability; no regions stated. **Official source:** https://techcommunity.microsoft.com/blog/azurearcblog/whats-new-with-sovereign-private-cloud-at-microsoft-ignite-2026/4573886

### Not examined

- **Other Microsoft Ignite 2026 announcements outside the requested Azure infrastructure, compute, Foundry, Fabric, database, GitHub, developer-tools, hybrid/Azure Local and sovereign-cloud categories:** not examined here.