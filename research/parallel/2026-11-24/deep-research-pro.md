# Ignite 2026 Announcements: Verified Candidates and Outstanding Exclusions

## Executive Summary

- **Important Completeness Limitation**: This is a **partial, officially sourced candidate catalogue**, not a completed net-new catalogue. I could not reliably finish the comparison against every entry in the exclusion file, which identifies itself as containing **144 announcements**. The rows below must not be treated as confirmed additions to that file. [1]
- **Resilience Testing**: Azure Chaos Studio Workspaces and its AKS extension are generally available -> consider them together when evaluating repeatable application-resilience testing. [3]
- **Confidential Computing**: Microsoft announces previews spanning multi-GPU confidential computing, enclaves, confidential containers and clean rooms -> evaluate the individual capabilities rather than assuming a single availability commitment covers the whole portfolio. [3]
- **Operations Availability**: Azure Monitor's natural-language capabilities and health models are generally available, while Azure Copilot customization and Azure Workload Center extensions are in preview -> separate production adoption decisions from preview evaluations. [3]
- **Infrastructure Flexibility**: Foundry-to-AKS deployment and new agent-infrastructure capabilities expand deployment choices -> check the specific preview conditions before incorporating them into a production architecture. [3]
- **Requested Priority Areas Remain Incomplete**: I have not established a dependable net-new inventory for Power Platform, Teams, SharePoint, Purview, Intune, Edge for Business, Security Copilot, licensing or industry solutions. Their absence from the tables below is **not evidence that Microsoft made no announcements** in those areas.

## Officially Verified Candidates: Azure Resilience and Confidential Computing

**Exclusion status for every row in this report: unresolved.** These are verified Microsoft announcements, but their absence from `LLM.TXT` has not been established. I am keeping that distinction explicit rather than falsely presenting them as the requested set difference.

**Field conventions:**

- **NS** means not stated in the cited announcement passage. It does not mean that no requirement or restriction exists.
- **Preview - stage unspecified** preserves Microsoft's wording; it is not upgraded to public preview.
- **At announcement** means the Book of News says "now" available or in preview. It does not establish a separate calendar release date.
- **Source B** is the official source URL: https://news.microsoft.com/events/ignite/2026/book-of-news/

| Product family | Product | Capability | Short description | Status | Availability date | Regions | Audience | Licensing prerequisites | Official source URL |
|---|---|---|---|---|---|---|---|---|---|
| Azure | Azure Chaos Studio | Workspaces | Organize resilience tests and apply reusable disruption scenarios, including availability-zone loss and database failover. | GA | At announcement; exact day NS | NS | Application and resilience engineering teams | NS | B [3] |
| Azure | Azure Chaos Studio | AKS extension | Introduce controlled disruptions to Kubernetes pods with fewer permissions required to run experiments. | GA | At announcement; exact day NS | NS | Teams operating applications on AKS | NS | B [3] |
| Azure | Azure confidential computing | VR72 multi-GPU confidential computing | Extend confidential-computing protection toward large models that span more than one GPU. | Preview - stage unspecified | Exact date NS | NS | Organizations processing sensitive AI workloads | NS | B [3] |
| Azure | Azure confidential computing | Azure Confidential Enclaves | Create a smaller trusted execution environment within a broader virtual machine. | Preview - stage unspecified | Exact date NS | NS | Organizations requiring protection during data processing | NS | B [3] |
| Azure | AKS | Kata CoCo confidential containers | Use confidential containers to narrow the surrounding system that must be trusted and verified. | Preview - stage unspecified | Exact date NS | NS | Kubernetes platform and security teams | NS | B [3] |
| Azure | Azure confidential computing | Azure Confidential Clean Room | Support multiparty analytics while helping protect participants' sensitive raw data from collaborators and cloud operators. | Preview - stage unspecified | Exact date NS | NS | Organizations collaborating on sensitive datasets | NS | B [3] |

The useful distinction is between the **GA resilience-testing tools** and the **preview confidential-computing offerings**. The latter should not be interpreted as generally available simply because they appear alongside GA infrastructure announcements. [3]

## Officially Verified Candidates: Azure Operations and Agent Infrastructure

The Book of News separates generally available operational capabilities from preview customization, workload extensions and agent infrastructure. That separation matters for deployment planning: a GA monitoring foundation does not make every connected agent capability GA. [3]

| Product family | Product | Capability | Short description | Status | Availability date | Regions | Audience | Licensing prerequisites | Official source URL |
|---|---|---|---|---|---|---|---|---|---|
| Azure | Azure Monitor | Natural-language capabilities | Help users plan and deploy cloud workloads using natural language. | GA | At announcement; exact day NS | NS | Cloud operators and workload teams | NS | B [3] |
| Azure | Azure Monitor | Health models | Translate telemetry into a real-time health graph connecting application architecture, dependencies and business priorities. | GA | At announcement; exact day NS | NS | Operations and incident-response teams | NS | B [3] |
| Azure | Azure Copilot | Spaces and custom skills | Let teams tailor agents and retain persistent operational context. | Preview - stage unspecified | Exact date NS | NS | Cloud operations teams | NS | B [3] |
| Azure | Azure Workload Center | Oracle and SAP extensions | Extend agentic operations to workload-health monitoring and configuration validation for Oracle and SAP. | Preview - stage unspecified | Exact date NS | NS | Oracle and SAP workload operators | NS | B [3] |
| Azure / AI | Microsoft Foundry and AKS | Deploy open-weight models and agents to customer AKS clusters | Extend the Foundry development experience to customer-controlled infrastructure, security policies and governance. | Preview - stage unspecified | Exact date NS | No region list stated; teams can select infrastructure based on cost, latency and residency needs | AI developers and platform teams | NS | B [3] |
| Azure / AI | AKS | Agent Grid | New infrastructure capability within Azure's production-AI foundation. | Preview - stage unspecified | Exact date NS | NS | AI application operators | NS | B [3] |
| Azure / AI | AKS | Agent Sandbox extension | New sandbox infrastructure capability for agent workloads on AKS. | Preview - stage unspecified | Exact date NS | NS | AI application and platform operators | NS | B [3] |
| Azure | AKS | Flex nodes | Extend AKS to customer servers. | Preview - stage unspecified | Exact date NS | NS | Organizations extending their Kubernetes infrastructure | NS | B [3] |

For an adoption shortlist, distinguish **monitoring capabilities available now** from **preview infrastructure requiring further qualification**. Regional availability and commercial prerequisites remain unspecified in the cited passages; those fields should not be filled with assumptions. [3]

## Additional Verified Candidate: Windows Server 2028

Windows Server 2028 is another officially announced candidate, but it has the same unresolved exclusion status as the Azure rows. Its preview announcement also distinguishes ordinary preview access from limited early access to enterprise hybrid intelligence. [3]

| Product family | Product | Capability | Short description | Status | Availability date | Regions | Audience | Licensing prerequisites | Official source URL |
|---|---|---|---|---|---|---|---|---|---|
| Windows Server | Windows Server 2028 | Next server release preview | Preview capabilities across security, enterprise infrastructure and simplified administration; enterprise hybrid intelligence has limited early access. | Preview; hybrid intelligence limited early access | Exact date NS | NS | Enterprise infrastructure and server administrators | Windows Server Insider Program is the stated preview-access route; commercial licensing prerequisites NS | B [3] |

The access distinction is important: the announcement does not justify treating every Windows Server 2028 capability as equally available. Evaluate the relevant component and access program separately. [3]

## Requested Priority Areas: What This Partial Catalogue Does Not Establish

The following coverage gaps prevent this answer from satisfying the requested complete, de-duplicated catalogue. In particular, the Book of News and live news are event-wide sources, not substitutes for a completed capability-by-capability comparison with the supplied exclusion file. [3][2][1]

| Requested area | Result in this answer | What remains unresolved |
|---|---|---|
| Power Platform, including Copilot Studio | No confirmed net-new rows reported | Individual capabilities, release stages, dates, regions and licensing, compared with the complete exclusion file |
| Teams | No confirmed net-new rows reported | Whether individual announcements or status changes are absent from the exclusion file |
| SharePoint and OneDrive | No confirmed net-new rows reported | Capability-level differences, including governance and administration announcements |
| Purview | No confirmed net-new rows reported | Individual security, governance and compliance announcements and their prerequisites |
| Intune | No confirmed net-new rows reported | Individual endpoint-management announcements, statuses and licensing |
| Edge for Business | No confirmed net-new rows reported | Browser capability differences, availability and prerequisites |
| Security Copilot | No confirmed net-new rows reported | Product-specific additions, status changes and commercial prerequisites |
| Licensing, pricing and retirements | No confirmed net-new rows reported | Event-specific commercial or retirement changes absent from the file |
| Industry solutions | No confirmed net-new rows reported | Distinct product announcements versus illustrative customer or industry scenarios |

**Do not interpret these gaps as negative findings.** This answer does not establish that these areas lack additional announcements; it establishes only that their net-new entries have not been resolved here.

## Synthesis

The verified candidates differ along three practical dimensions. **Chaos Studio** addresses controlled resilience testing and is GA; **Azure Monitor** supplies GA operational context; **confidential computing and agent infrastructure** introduce preview capabilities with different protection and deployment scopes. **Windows Server 2028** adds another preview track, with a separate limited-access qualification for hybrid intelligence. [3]

The central unresolved issue is **exclusion eligibility**, not whether the candidate announcements appear on an official Microsoft page. Consequently, this report should be used as a sourced working list, **not imported as a completed list of announcements missing from `LLM.TXT`**. I cannot substantiate a complete net-new count from the evidence evaluated.

All candidate announcement facts above are sourced to an official Microsoft page. No third-party-only announcement is presented as verified. Unspecified dates, regions and licensing remain explicitly marked rather than inferred.

## References

1. *ignite-2026-announcements/LLM.TXT at main · anorthernman-developer/ignite-2026-announcements · GitHub*. https://github.com/anorthernman-developer/ignite-2026-announcements/blob/main/LLM.TXT
2. *Microsoft Ignite 2026 | Live News*. https://news.microsoft.com/events/ignite/2026/live-news/
3. *Microsoft Ignite 2026 | Book of News*. https://news.microsoft.com/events/ignite/2026/book-of-news/
