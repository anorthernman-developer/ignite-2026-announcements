"""Generate taxonomy/taxonomy.json and taxonomy/taxonomy.md from scripts/data.py plus fixed lookups."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import data
FAM_DEF = {
 data.F_COP:"Microsoft 365 Copilot, the Copilot app, Office in Copilot, Cowork, Code, Autopilot, SharePoint, OneDrive, Teams and Viva Engage experiences.",
 data.F_AG:"Building, running, tuning, governing and paying for agents: Agent 365, Copilot Studio, Frontier Tuning, Windows 365 for Agents.",
 data.F_IQ:"Enterprise context layer: Microsoft IQ, Work IQ, Fabric IQ, Foundry IQ, Web IQ.",
 data.F_AI:"Models (MAI, OpenAI, Meta, Microsoft-Decision), Microsoft Foundry platform services and AI silicon.",
 data.F_AZ:"Azure compute, operations, migration, AI infrastructure, Azure Local, sovereign cloud and Windows Server.",
 data.F_DATA:"Microsoft Fabric, Power BI and Azure databases (HorizonDB, SQL, Cosmos DB, DocumentDB, PostgreSQL, Redis).",
 data.F_DEV:"GitHub Copilot, GitHub Enterprise, Copilot SDK and developer tooling.",
 data.F_SEC:"Microsoft Perception, Defender, Sentinel, Entra, Purview, Microsoft 365 Backup, Baseline Security Mode, MDASH and responsible AI.",
 data.F_WIN:"Windows 11, Windows 365, Intune and endpoint management.",
 data.F_EDGE:"Edge for Business security and governed AI browsing.",
 data.F_BIZ:"Dynamics 365, Power Apps, Power Platform and contact centre.",
 data.F_PART:"Strategic partnerships announced at Ignite (for example Salesforce).",
 data.F_LIC:"Licensing, pricing, billing, retirements and partner programme changes.",
 data.F_IND:"Industry-specific solutions (healthcare, financial services, public sector and others).",
}
fams = []
for f, d in FAM_DEF.items():
    prods = {}
    for r in data.R:
        if r["product_family"] == f: prods.setdefault(r["product"], set()).add(r["capability_area"])
    fams.append({"name": f, "definition": d, "products": [{"name": p, "capability_areas": sorted(c)} for p, c in sorted(prods.items())]})
def vals(pairs): return [{"name": n, "definition": d} for n, d in pairs]
tax = {"name": "Microsoft Ignite 2026 announcement taxonomy", "version": "1.0", "updated": "2026-11-24",
 "dimensions": {
  "product_family": {"definition": "Top level grouping. Hierarchy: product_family > product > capability_area.", "values": fams},
  "announcement_type": {"definition": "What kind of news it is.", "values": vals([
    ("New product","A product or service that did not exist before."),("New capability","A new feature in an existing product."),
    ("New model","A new AI model or model family."),("New version","A new major version of an existing product."),
    ("Status change","A move between release stages, usually preview to GA."),("Update","A bundle of improvements to an existing product."),
    ("Mixed","One announcement with parts at different stages."),("Default change","A change to default settings or behaviour."),
    ("Pricing / licensing","Price, SKU, billing or licence terms."),("Retirement","End of sale, end of support or removal."),
    ("Partnership","A named commercial or technical partnership."),("Industry initiative","A multi-organisation effort or standard."),
    ("New programme","A customer or partner programme."),("Milestone","A usage or scale figure shared on stage.")])},
  "status_category": {"definition": "Normalised release stage used for filtering. The free-text status column keeps Microsoft's own wording.", "values": vals([
    ("GA","Generally available for production use."),("Public preview","Open preview, any eligible customer can try it."),
    ("Private or limited preview","Invitation, eligibility or limited-access preview."),("Preview (stage not stated)","Microsoft says preview without saying public or private."),
    ("Frontier","Microsoft's early-access programme for Copilot and agents."),("Coming soon","Announced with no current access."),
    ("Mixed","Parts of the announcement sit at different stages; see the status column."),("Licensing change","A dated licensing or billing change."),
    ("Retirement","Being retired or removed."),("Announced","Announced with no stage given."),("Milestone","A figure, not a product change.")])},
  "audience": {"definition": "Primary reader the announcement is aimed at.", "values": vals([
    ("Business decision makers","Budget holders and leaders deciding on spend and value."),("IT pros and admins","People who deploy, manage and govern."),
    ("Security teams","SOC, identity, data security and compliance."),("Developers","People who build apps, agents and integrations."),
    ("Data professionals","Analysts, data engineers and BI developers."),("End users","Everyday users of Copilot and Microsoft 365."),("Partners","Microsoft partners, CSPs and MSPs.")])},
  "industry": {"definition": "Industry focus where stated; most items are cross-industry.", "values": vals([
    ("Cross-industry","No specific industry."),("Healthcare","Clinical and health organisations."),("Financial services","Banks, insurers, capital markets."),
    ("Public sector","Government, defence, sovereign requirements."),("Retail","Retail and consumer goods."),("Manufacturing","Manufacturing and industrial.")])},
  "ignite_scope": {"definition": "Whether the item was announced at Ignite or is adjacent news from the same period.", "values": vals([
    ("Ignite 2026","Announced at Ignite 2026 (live news, Book of News or Ignite-dated official blogs)."),
    ("Adjacent (November partner announcements)","Partner Center or licensing news published in November 2026."),
    ("Adjacent (28 Oct 2026, pre-Ignite)","Published before Ignite but directly relevant."),("Ignite window (docs)","Documented in product docs during the Ignite window.")])},
  "verification": {"definition": "Which kind of source the row rests on.", "values": vals([
    ("Book of News","Confirmed in the Ignite 2026 Book of News."),("Live news + official blog","Confirmed on the live news blog and an official blog."),
    ("Official blog","Confirmed on an official Microsoft, Azure, Windows, Dynamics 365 or Tech Community blog."),
    ("Microsoft AI blog","Confirmed on microsoft.ai news."),("Book of News + Microsoft AI blog","Confirmed in the Book of News and on microsoft.ai."),
    ("Live news + Microsoft AI blog","Confirmed on the live news blog and on microsoft.ai."),("Live news + Microsoft Source","Confirmed on the live news blog and Microsoft Source."),("GitHub changelog","Confirmed on the GitHub changelog."),
    ("Partner Center announcements","Confirmed on Microsoft Learn Partner Center announcements."),("Official docs (Defender for Office 365 what's new)","Confirmed in Microsoft Learn docs."),
    ("Parallel deep research (official blog)","Found by Parallel deep research citing an official blog; to be re-read on the next run.")])},
  "region": {"definition": "Region availability where Microsoft states it; otherwise 'Not stated'.", "values": vals([("Not stated","Microsoft did not give regions."),("Named regions","See the region column.")])},
 }}
json.dump(tax, open("taxonomy/taxonomy.json", "w"), indent=2, ensure_ascii=False)
md = ["# Taxonomy", "", "How every announcement is classified. The machine-readable version is [taxonomy.json](taxonomy.json). Values in the spreadsheet and JSON come only from this list.", "",
      "## Product hierarchy", "", "Three levels: product family > product > capability area.", ""]
for f in fams:
    md += [f"### {f['name']}", "", f["definition"], ""]
    for p in f["products"]: md.append(f"- {p['name']}: {', '.join(p['capability_areas'])}")
    md.append("")
for k, d in tax["dimensions"].items():
    if k == "product_family": continue
    md += [f"## {k.replace('_',' ').capitalize()}", "", d["definition"], "", "| Value | Definition |", "| --- | --- |"]
    md += [f"| {v['name']} | {v['definition']} |" for v in d["values"]] + [""]
open("taxonomy/taxonomy.md", "w").write("\n".join(md))
