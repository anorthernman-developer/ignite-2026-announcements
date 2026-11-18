# Ontology

The ontology describes the things in this knowledge base and how they connect. The formal version is [ontology.ttl](ontology.ttl) (OWL, Turtle). [ontology.jsonld](ontology.jsonld) is a JSON-LD context that maps each column in `data/announcements.json` to the ontology, so the data can be loaded into a graph tool as is.

## Entities

| Entity | What it is | Example |
| --- | --- | --- |
| Event | The conference the news came from | Microsoft Ignite 2026, 17-20 November 2026 |
| Announcement | One piece of product or service news (one spreadsheet row) | IGN26-SEC-xxx Microsoft Perception generally available |
| ProductFamily | Top level of the product hierarchy | Security, identity and compliance |
| Product | A named Microsoft product or service | Microsoft Defender |
| Capability | Capability area within a product | Attack disruption |
| Model | An AI model (a kind of Product) | MAI Code 2, Microsoft-Decision-1.1 |
| AnnouncementType | What kind of news it is | Status change, New model, Retirement |
| Status | Normalised release stage | GA, Public preview, Frontier |
| Audience | Who it is aimed at | Security teams |
| Industry | Industry focus | Healthcare |
| Region | Where it is available | UK South |
| LicensingTerm | Licence, SKU, credit or price condition | Copilot Credits; Microsoft 365 E5 or E7 |
| Source | The web page that evidences the news | Book of News, Tech Community blog |
| Partner | A named external organisation | Salesforce, Check Point |
| UpdateRun | One scheduled build of this repo | 2026-11-18 run 1 |

## Relations

```
Announcement --announcedAt--> Event
Announcement --concernsProduct--> Product --inFamily--> ProductFamily
Announcement --hasCapability--> Capability --capabilityOf--> Product
Announcement --hasType--> AnnouncementType
Announcement --hasStatus--> Status
Announcement --targetsAudience--> Audience
Announcement --targetsIndustry--> Industry
Announcement --availableIn--> Region
Announcement --requiresLicence--> LicensingTerm
Announcement --primarySource / secondarySource--> Source
Announcement --involvesPartner--> Partner
Announcement --relatedTo--> Announcement        (symmetric; same product)
Announcement --supersedes--> Announcement       (for example preview later reaches GA)
Product --poweredBy--> Model                    (for example Cowork Auto uses Microsoft-Decision-1.1)
Announcement --changedIn--> UpdateRun           (ties rows to CHANGELOG.md)
```

## Rules

1. Every Announcement has exactly one primary Source. No source, no row.
2. Status keeps two forms: Microsoft's own words (`status`) and a normalised value (`status_category`) for filtering.
3. An announcement with parts at different stages is one row with status category Mixed; the `status` text spells out each part.
4. When a later run sees a status change (for example public preview to GA), the row is updated, `last_updated` changes and CHANGELOG.md records the old and new value.
5. Items published in the same weeks but not on the Ignite stage are kept, marked with `ignite_scope` so they can be filtered out.
