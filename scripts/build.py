"""Build every derived file in the repo from scripts/data.py.
Run from the repo root: python scripts/build.py"""
import csv, json, os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
import data
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo

RUN_DATE = "2026-11-18"
RUN_TIME = "13:30 GMT"
REPO = "https://github.com/anorthernman-developer/ignite-2026-announcements"
FAM_CODE = {data.F_COP:"COP",data.F_AG:"AGT",data.F_IQ:"IQ",data.F_AI:"AI",data.F_AZ:"AZ",data.F_DATA:"DATA",data.F_DEV:"DEV",
            data.F_SEC:"SEC",data.F_WIN:"WIN",data.F_EDGE:"EDGE",data.F_BIZ:"BIZ",data.F_PART:"PART",data.F_LIC:"LIC",data.F_IND:"IND"}
FAM_ORDER = list(FAM_CODE)

def status_category(s):
    l = s.lower()
    if "retir" in l: return "Retirement"
    if "milestone" in l: return "Milestone"
    if l.startswith("effective") or "csp preview" in l: return "Licensing change"
    toks = l.replace(";"," ").replace(",", " ").replace("(", " ").split()
    if "mixed" in l or (("ga" in toks or "available" in toks) and ("preview" in l or "frontier" in l)): return "Mixed"
    if "frontier" in l: return "Frontier"
    if l.startswith("ga"): return "GA"
    if "public preview" in l: return "Public preview"
    if "private preview" in l or "limited" in l: return "Private or limited preview"
    if "preview" in l: return "Preview (stage not stated)"
    if "coming soon" in l: return "Coming soon"
    if "available" in l: return "GA"
    return "Announced"

rows = []
count = {}
for r in sorted(data.R, key=lambda r: (FAM_ORDER.index(r["product_family"]), r["product"], r["title"])):
    c = FAM_CODE[r["product_family"]]; count[c] = count.get(c, 0) + 1
    out = {"id": f"IGN26-{c}-{count[c]:03d}", "title": r["title"], "announced_date": "2026-11-17" if r["ignite_scope"]=="Ignite 2026" else "",
           "event": "Microsoft Ignite 2026", "ignite_scope": r["ignite_scope"], "product_family": r["product_family"], "product": r["product"],
           "capability_area": r["capability_area"], "announcement_type": r["announcement_type"], "status": r["status"],
           "status_category": status_category(r["status"]), "availability": r["availability"], "audience": r["audience"],
           "industry": r["industry"], "licensing": r["licensing"], "region": r["region"], "tags": r["tags"], "summary": r["summary"],
           "source_url": r["source_url"], "secondary_source": r["secondary_source"], "verification": r["verification"],
           "related": "", "first_seen": RUN_DATE, "last_updated": RUN_DATE}
    rows.append(out)
# related: same product
byprod = {}
for r in rows: byprod.setdefault(r["product"], []).append(r["id"])
for r in rows: r["related"] = ";".join(i for i in byprod[r["product"]] if i != r["id"])
FIELDS = list(rows[0])

os.makedirs("data", exist_ok=True)
with open("data/announcements.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
json.dump({"generated": RUN_DATE, "count": len(rows), "announcements": rows}, open("data/announcements.json", "w"), indent=2, ensure_ascii=False)

CHANGELOG = [
 (RUN_DATE, "Run 1 (first build)", f"Created repo. Captured {len(rows)} announcements from the live news blog, Book of News and official Microsoft blogs, cross-checked with 3 Parallel test runs and 1 Parallel deep research run."),
 (RUN_DATE, "Format change", "Added verification, ignite_scope, secondary_source, licensing and status_category columns after reviewing the Parallel runs."),
 (RUN_DATE, "Format change", "Separated adjacent November partner and licensing items from Ignite stage announcements using ignite_scope."),
 (RUN_DATE, "Format change", "LLM.TXT now leads each line with status so a model or reader can filter GA from preview quickly."),
]

# Excel
wb = Workbook(); ws = wb.active; ws.title = "Announcements"
ws.append(FIELDS)
for r in rows: ws.append([r[k] for k in FIELDS])
hdr = Font(bold=True, color="FFFFFF"); fill = PatternFill("solid", fgColor="1F3864")
for c in ws[1]: c.font = hdr; c.fill = fill; c.alignment = Alignment(wrap_text=True, vertical="top")
widths = {"id":16,"title":45,"summary":70,"source_url":45,"secondary_source":35,"product_family":28,"product":24,"status":26,"availability":30,"licensing":30,"tags":28,"related":24}
for i, k in enumerate(FIELDS, 1):
    ws.column_dimensions[ws.cell(1, i).column_letter].width = widths.get(k, 18)
su = FIELDS.index("source_url") + 1
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
    cell = row[su-1]; cell.hyperlink = cell.value; cell.font = Font(color="0563C1", underline="single")
t = Table(displayName="Announcements", ref=f"A1:{ws.cell(1,len(FIELDS)).column_letter}{len(rows)+1}")
t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True); ws.add_table(t)
ws.freeze_panes = "C2"

tax = json.load(open("taxonomy/taxonomy.json"))
s2 = wb.create_sheet("Taxonomy - products"); s2.append(["product_family","product","capability_areas"])
for fam in tax["dimensions"]["product_family"]["values"]:
    for p in fam["products"]: s2.append([fam["name"], p["name"], "; ".join(p.get("capability_areas", []))])
s3 = wb.create_sheet("Taxonomy - lookups"); s3.append(["dimension","value","definition"])
for dim, d in tax["dimensions"].items():
    if dim == "product_family": continue
    for v in d["values"]: s3.append([dim, v["name"], v.get("definition","")])
s4 = wb.create_sheet("Summary"); s4.append(["product_family","announcements","GA","Public preview","Frontier","Mixed","Other"])
for fam in FAM_ORDER:
    fr = [r for r in rows if r["product_family"] == fam]
    if not fr: continue
    sc = lambda k: sum(1 for r in fr if r["status_category"] == k)
    s4.append([fam, len(fr), sc("GA"), sc("Public preview"), sc("Frontier"), sc("Mixed"), len(fr)-sc("GA")-sc("Public preview")-sc("Frontier")-sc("Mixed")])
s4.append(["Total", len(rows)])
s5 = wb.create_sheet("Change log"); s5.append(["date","entry","detail"])
for c in CHANGELOG: s5.append(list(c))
s6 = wb.create_sheet("Sources"); s6.append(["source_url","announcements_citing"])
src = {}
for r in rows:
    for u in (r["source_url"], r["secondary_source"]):
        if u: src[u] = src.get(u, 0) + 1
for u, n in sorted(src.items(), key=lambda x: -x[1]): s6.append([u, n])
for sh in (s2, s3, s4, s5, s6):
    for c in sh[1]: c.font = hdr; c.fill = fill
    sh.auto_filter.ref = sh.dimensions; sh.freeze_panes = "A2"
    for col in sh.columns: sh.column_dimensions[col[0].column_letter].width = 40
wb.save("data/announcements.xlsx")

# LLM.TXT
L = [f"# Microsoft Ignite 2026 announcements (LLM.TXT)", f"# Event: 17-20 November 2026, San Francisco and online", f"# Built: {RUN_DATE} {RUN_TIME}. Announcements: {len(rows)}. Repo: {REPO}",
     "# Primary sources: https://news.microsoft.com/events/ignite/2026/live-news/ and https://news.microsoft.com/events/ignite/2026/book-of-news/",
     "# Line format: [STATUS] Title | availability | one-line summary | source URL | id",
     "# Status values: GA, Public preview, Private or limited preview, Preview (stage not stated), Frontier, Coming soon, Mixed, Licensing change, Retirement, Announced, Milestone",
     "# Items marked (adjacent) were published in November 2026 around Ignite but not on the Ignite stage.", ""]
for fam in FAM_ORDER:
    fr = [r for r in rows if r["product_family"] == fam]
    if not fr: continue
    L.append(f"## {fam} ({len(fr)})")
    for r in fr:
        adj = " (adjacent)" if r["ignite_scope"] != "Ignite 2026" else ""
        L.append(f"[{r['status_category']}] {r['title']}{adj} | {r['availability']} | {r['summary']} | {r['source_url']} | {r['id']}")
    L.append("")
open("LLM.TXT", "w").write("\n".join(L))
print(len(rows), "rows")
