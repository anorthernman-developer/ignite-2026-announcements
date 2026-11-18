# Deep research run: easy-to-miss areas, licensing, retirements and industry

- Run date: 18 November 2026 (Europe/London)
- Tool: Parallel web_research via MCP
- Reasoning effort: medium (high effort timed out twice at the MCP connector; see README)
- Response id: resp_a5c4d13c-be46-411c-b66f-29577e31ba14
- Prompt: Ignite 2026 announcements for Power Platform, Teams and Teams Phone/Rooms, SharePoint and OneDrive, Purview, Intune, Edge for Business, Microsoft 365 licensing and pricing (E5, E7, Copilot SKUs, Copilot Credits), partner programme changes, retirements and industry solutions, with status, availability, audience, licensing notes and official source URL; flag anything not verified.

Output below is unedited Parallel output. Treat it as research input, not a source. Rows in the spreadsheet cite the Microsoft pages, not this file.

---

MICROSOFT IGNITE 2026 (17–20 November 2026) — ANNOUNCEMENT ROUNDUP. All items below are sourced from the official Book of News (https://news.microsoft.com/events/ignite/2026/book-of-news/) and official Microsoft blogs/pages. Items not verifiable on an official Microsoft Ignite page are explicitly flagged. Note: one third-party site claimed the Book of News would not be published for Ignite 2026; the official Book of News is live at the URL above, so that claim is disregarded.

=== POWER PLATFORM ===
1) Power BI — custom data app creation. Power BI Pro customers can now, in preview, create purpose-built data apps directly in Power BI Desktop, starting from a trusted Power BI semantic model and describing the app in natural language; users can enter information, update records and write back to the data source. Status: Preview (public); availability: announced at Ignite, now in preview; audience: Power BI Pro customers (planning, approvals, tracking, data collection); licensing: delivered "through existing licensing options" — Power BI Pro customers also get access to Fabric Database capabilities (no additional cost reported); source: https://news.microsoft.com/events/ignite/2026/book-of-news/. Supporting official Fabric/Power BI blog: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/microsoft-fabric-is-fueling-frontier-transformation/5422989 (linked from the Book of News).
2) Fabric-related Power Platform/Fabric items — Rayfin and Fabric apps reached general availability (100,000+ apps built since preview); Fabric IQ integrations across Copilot/Fabric apps GA, Excel/GitHub Copilot/ChatGPT/Claude integrations (ChatGPT/Claude connectors in preview). Microsoft Fabric HorizonDB (PostgreSQL in Fabric) in preview.
3) Power Apps / Power Automate — NOT VERIFIED for Ignite 2026: no Power Apps or Power Automate announcements were found in the official Book of News; recent official Power Platform news comes from the October/November 2026 feature update (e.g., reusable desktop flow templates in Power Automate for desktop; modern attachments controls in Power Apps preview)[167], which predates/predates-not-part-of Ignite. Flagged: not verified on an official Ignite 2026 page.
4) Power BI retirement: built-in R and Python visuals in Power BI retire in May 2027 (announced 9 November 2026 on the Power BI Updates Blog, not an Ignite announcement; Python scripts in Power Query unaffected). Flagged: announced separately from Ignite.

=== MICROSOFT TEAMS, TEAMS PHONE / ROOMS ===
1) Salesforce in Copilot, Teams and Fabric ("Copilotforce"): Salesforce customer context, business processes and actions across Copilot, Teams and Fabric; Salesforce in Copilot plugin in preview (38+ prebuilt sales skills); Sales Cloud in Teams — Salesforce customer context directly in Teams collaboration (pipeline/quota view, deal notifications, briefings) — status: pilot; source: Book of News + Ignite Live.
2) Teams Phone Agent — AI receptionist for call queues: GA from 30 September 2026 (pre-Ignite); licensing: requires Teams Phone, a resource account and a spending policy (metered usage via Copilot Credits; Copilot Credit Estimator supported). Flagged: announced pre-Ignite, not in the Book of News.
3) Microsoft Contact Center Intelligence — Microsoft voice/digital agents layered on Genesys, Five9, Avaya, Webex contact-centre platforms: now generally available (announced 17 Nov 2026 in the official Dynamics 365 Ignite blog).
4) Teams Rooms / Teams Phone items — device management for Teams Rooms on Android, Teams phones, panels and SIP phones moving from Teams Admin Center to the Pro Management Portal, dated per device type (mid–end November; phones to 15 December; GCC High/DoD by 15 December; GCC by 30 January 2027, per Message Center MC1448373/MC1227626). Granular Conditional Access for meetings — preview late November, GA January (MC1532256); Intelligent Call Delegation — preview mid-November, GA January 2027, requires Teams Phone + Copilot license (MC1519860). Flagged: these come from Microsoft Message Center/Tech Community references rather than the Book of News; the official "What's new in Microsoft Teams | Microsoft Ignite 2026" post was not retrieved, so Teams-specific Book of News entries cannot be confirmed item-by-item.

=== SHAREPOINT AND ONEDRIVE ===
Source: official SharePoint/OneDrive Ignite blog (https://techcommunity.microsoft.com/blog/spblog/sharepoint-and-onedrive-at-microsoft-ignite-2026-putting-ai-powered-content-to-w/4535416):
1) SharePoint tools in Work IQ and the Copilot app — public preview; Copilot and agents get access to 60+ SharePoint operations (lists/libraries, files/folders, search, approvals, rules, Quick Steps, versioning).
2) Work IQ context enhancements — rolling out to public preview this month; deep document grounding for custom agents (document markdown, images/thumbnails, summaries, semantic lookup); to expand to SharePoint sites, Teams chats/channels/meetings and Outlook email over time.
3) Copilot in SharePoint — generally available since October 2026.
4) Copilot in OneDrive — now generally available (AI directly on files).
5) SharePoint indexed knowledge source — now generally available, bringing SharePoint content into Foundry IQ retrieval respecting source permissions.
6) SharePoint Admin Agent — natural-language tenant analysis and guided remediation across permissions/oversharing, content lifecycle, storage, catalog and settings; plus a new agent access heatmap and file-level EEEU permissions report (Learn-documented, https://learn.microsoft.com/en-us/sharepoint/content-governance-agent).
7) OneDrive/SharePoint security: sensitivity-label protected PDF annotation on the web (Message Center MC1545696); Purview Priority Cleanup permanently deletes SharePoint/OneDrive files post-approval (preview).

=== MICROSOFT PURVIEW ===
Source: Book of News Purview section + official Security blog:
1) Accelerated Copilot deployment — strengthened DLP for Copilot with grounding protection to block Copilot from referencing files with sensitive information even when unlabeled; Copilot will not process prompts with attached/linked files containing sensitive data. Status: public preview January 2027.
2) Enhanced data classification — high-precision, scalable, up-to-date automatic classification/labeling of sensitive data: generally available January 2027.
3) Security for AI agents — Purview extends data security capabilities for endpoint agents running on Windows, controlling what data AI agents can access and share; DLP for Microsoft agents and key local agents (Claude Code, Claude Desktop, GitHub Copilot CLI, GitHub Copilot app, VS Code extensions) in preview in the Purview portal.
4) Network DLP with Entra Global Secure Access — generally available; DLP at the network layer for human and on-behalf-of agent traffic, including unsanctioned AI apps; extension to all websites GA December 2026.
5) RETIREMENT: Microsoft Purview Data Governance (Unified Catalog, Data Map, Workflows, Azure Purview solutions) — being retired as of 12 November 2026, end of support 12 November 2027; Microsoft consolidates data governance in Microsoft Fabric and the OneLake catalog; Purview Data Security and Compliance offerings unchanged. Source: https://learn.microsoft.com/en-us/partner-center/announcements/2026-november.

=== MICROSOFT INTUNE ===
1) Local AI agent governance controls — in preview.
2) Windows Server management in Intune — Insider preview; brings eligible servers (including edge/branch servers and persistent VDI sessions) into cloud-management workflows.
3) Windows 365 admin assistant — AI-powered experience in Microsoft Intune, in preview, for Cloud PC health monitoring and troubleshooting.
4) Intune Enterprise App Management — automatic updates in preview.
5) Endpoint/Edge policy support: Purview DLP for unmanaged apps in Edge for Business with Intune multi-admin approval (MC1489971); Edge work-profile downloads to OneDrive for Business (requires Edge 158+). Licensing notes: advanced Intune features such as Remote Help and Intune P2 added to M365 E3 and E5 suites as of the 1 July 2026 packaging update. Source: https://techcommunity.microsoft.com/blog/microsoftintuneblog/what’s-new-in-microsoft-intune-at-ignite/4570003.

=== MICROSOFT EDGE FOR BUSINESS ===
Source: Book of News:
1) Skills recorder — record a workflow in Edge for Business and turn it into a reusable, shareable skill for Copilot Cowork; IT controls enablement; skills run within existing permissions/policies. Status: preview (with Cowork).
2) Managed agent browsing — IT can enforce use of Edge for Business by Microsoft and third-party agents whenever an agentic task needs a browser; agents run in dedicated windows with their own Entra agent identity. Status: preview.
3) Native Microsoft Sentinel connector for Edge for Business — browser security events/audit logs into Sentinel. Status: preview.
4) Microsoft Entra Global Secure Access in Edge for Business — private web app access from Windows PCs without a separate VPN client/extension. Status: preview.
5) Extension safety — generally available (org-wide inventory with Akamai/Spin.AI risk scores); Extension leak control — in preview.

=== MICROSOFT 365 LICENSING & PRICING (E5, E7, COPILOT SKUs, COPILOT CREDITS) ===
1) Microsoft 365 E7 — includes E5 capabilities plus Microsoft Copilot, the Microsoft Entra Suite and Microsoft Agent 365 in a single license; GA announced May 2026; list price USD 99/user/month (annual billing) vs M365 E5 USD 60/user/month. G7 government equivalent adds Copilot/Entra Suite/Agent 365 to G5.
2) E5/E-suite pricing change — effective 1 July 2026: M365 E5 $57→$60 (5%); M365 E5 (no Teams) $48.45→$51.45 (6%); M365 E3 $36→$39 (8%); Business Basic $6→$7 (16%); packaging updates (Security Copilot included in E5; Remote Help/Intune P2 added to E3/E5) rolling out from June 2026. Source: https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates.
3) Copilot SKUs — from 1 December 2026 new Microsoft 365 Copilot and Copilot Business offers can be purchased WITHOUT a qualifying M365 base subscription (all channels: commercial, education, government, nonprofit; same price); from 16 October 2026 current offers renamed "(add-on)"; add-on offers reach end of sale in CSP on 1 December 2026 (existing subscriptions unaffected).
4) Copilot Credits / usage-based billing — Copilot Credits are the usage-based currency (meter $0.01 per credit; capacity packs vs pay-as-you-go). New Copilot Business CSP purchases get usage-based billing ON BY DEFAULT during FY27 Q3 (January–March 2027; moved from 1 December 2026), with a default spending limit of 4,000 Copilot Credits per user/month (admin-adjustable). Windows 365 for Agents is now eligible for Copilot Credits (unified AI billing/governance); Today Feed recurring updates require Copilot credits.
5) Promotions: E7 + Copilot Studio annual capacity pack "Buy 5 Get 5" for CSP through 31 December 2026 (300+ E7 seats + 5 packs → Microsoft matches 1:1 for 12 months, up to 5 packs); 30% off Microsoft 365 E3 (net partner price, 300+ new licenses) 27 Oct 2026–30 Jun 2027; 25% off Business Basic + Copilot Business and 15% standalone Copilot Business promo through 31 December 2026; incremental "growth margin" on Copilot, E5, E7, Defender Suite, Purview Suite, Windows 365 Enterprise.

=== PARTNER PROGRAMME CHANGES ===
1) Custom Solutions for Microsoft Teams specialization — retired November 2026; no new enrollments/renewals; active until anniversary date.
2) MS-102 (Microsoft 365 Certified: Administrator Expert) retires 30 November 2026; AB-650 added to Modernize Endpoints specialization skilling.
3) SC-400 removed from Solutions Partner for Security skilling calculation.
4) AI Builder capacity add-ons — retired from sale 1 November 2026; existing credits usable to end of term; partners must disable auto-renew; Microsoft directs to Copilot Credits for ongoing use (no automatic conversion; no single conversion ratio).
5) Cloud Security specialization skilling calculation updated October 2026; Hybrid Cloud Infrastructure with Azure Stack HCI specialization renamed Azure Local for Hybrid & Sovereign Private Cloud (October 2026).
6) New permanent CSP bundles: Business Central (Essentials/Premium) + Microsoft 365 Copilot Business for ≤300 seats — in CSP price list preview 1 December 2026, available 1 January 2027 (saves USD 6/user/month).
7) Ignite partner programming: buy/renew partner benefits packages; Microsoft AI Cloud Partner Program booth, networking, dedicated partner sessions; Copilot in 30 promo offers until 31 December 2026; new M365 E7 cohort and FLOW signals in CloudAscent. Source: https://learn.microsoft.com/en-us/partner-center/announcements/2026-november.

=== RETIREMENTS ===
1) Purview Data Governance — retired 12 Nov 2026, EOS 12 Nov 2027 (see Purview above).
2) AI Builder capacity add-ons — retired 1 Nov 2026.
3) Power BI built-in R and Python visuals — retire May 2027 (pre-Ignite announcement, 9 Nov 2026).
4) Azure Communication Services retiring as a standalone product — no new sign-ups from 23 October 2026; standalone retirement 30 September 2028 (Teams interop — Teams Phone, Teams Phone Extensibility, Unify, video interop, Click-2-Call — not impacted).
5) Message Center retirements: Viva Engage retirement of Teams town hall event creation (MC1552394); retirement of Viva Insights (personal insights) and Viva Learning usage reports (MC1546411); Teams Free off-network invitations retirement (MC1546409); EWS deprecation (migrate Free/Busy, MailTips, calendar sharing; MC1146796). Flagged: Message Center items, not Book of News announcements.

=== INDUSTRY SOLUTIONS ===
1) Healthcare — Dragon Copilot: Dragon Copilot Transcribe, built on MAI-Transcribe-2, is now live in Dragon Copilot, powering 100% of doctor–patient conversation transcriptions, ~10 million patient encounters/month, multilingual error rates halved, used by roughly one-third of US physicians; announced at Ignite (17 Nov 2026, Microsoft AI blog). Dragon Copilot 5.0 (physicians) available with new usability/personalization capabilities (Microsoft Learn, updated 20 Aug 2026; November 17–20 window referenced). HIMSS 2026 (March) context: 100,000+ clinicians, partner AI apps/agents in Microsoft Marketplace (Canary Speech, Humata Health, Optum, Regard), role-based experiences for physicians, nurses, radiologists. Flagged: the detailed HIMSS items are not Ignite 2026 announcements; no separate official Ignite healthcare blog was retrieved.
2) Financial services — BNY is exploring capabilities in Project Perception (security/governance) and completed with Microsoft the first agentic negotiation of a US Treasury trade (keynote/Source blog). Visa customer context cited in Dynamics 365 in Copilot announcement. Flagged: no dedicated official Ignite financial-services announcement page retrieved.
3) Retail / Manufacturing / Public sector — NOT VERIFIED: no official Microsoft Ignite 2026 announcements specific to retail, manufacturing, or public sector solutions were found in the Book of News or official blogs retrieved. Only indirect references exist (e.g., a manufacturer giving agents predictive-maintenance context in the keynote live blog). Flagged as not examined on an official Microsoft page.
4) Adjacent Copilot/industry-relevant items: Dynamics 365 in Copilot — updated Sales plugin (GA) and ERP apps plugin (GA, 39+ finance and operations skills), Dynamics 365 data natively integrated with Work IQ, Copilot Studio Microsoft Copilot harness GA, Dynamics 365 Activate.

=== OTHER MAJOR ITEMS (context for the categories above) ===
Microsoft Perception (previously Project Perception) generally available — specialized agents (Posture Prioritization, Alert Triage, Threat Intelligence) and playbooks; Agent 365 Cost Management/Business Analytics (Business Analytics in Frontier; Microsoft-service insights need ≥1 M365 Copilot license in tenant, non-Microsoft service insights need Agent 365 license). Copilot Managed Runtime GA (with Fabric backend); Agents and Workflows in Managed Runtime; Copilot Workspaces (Frontier); Copilot Code (Frontier; GA December 2026); Autopilot rolling out to Frontier customers; Office in Copilot and Home GA. Windows endpoint security platform and Windows administrator protection GA; Windows 365 for Agents eligible for Copilot Credits; Windows Server 2028 public preview. GitHub Enterprise now includes GitHub Copilot usage rights at no extra cost, billed via AI Credits.