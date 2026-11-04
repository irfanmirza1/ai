# blog.softexpress.de – Change log

**Scope:** blog.softexpress.de only (WordPress admin access).
**Not in scope:** softexpress.de (shop), surffact.de, DNS, hosting.

This log has two purposes:
1. **Show the results of the work.** Part 5 compares the numbers before and
   after the changes.
2. **Protection.** Every change has a date, the reason, the before and after
   state, and how to undo it. Anything outside the scope has written approval
   from the client.

Rules:
- Fill in the baseline (Part 2) **before** the first change.
- Make one change at a time and log it right away, with date **and** time.
  If traffic or rankings move later, you can match it to the change.
- Take a screenshot of every setting before you change it.
- Anything outside your scope or touching legal texts gets written approval
  first (Part 3).

---

## 1. Access

| Date | Given by (name, role) | Access | Role in WordPress | Notes |
|---|---|---|---|---|
| | | WordPress admin, blog.softexpress.de | | |

## 2. Baseline – how the blog looks before any change

Date recorded: ____________
Screenshots saved in: ____________

| # | Item | Where to find it | Current value |
|---|---|---|---|
| B1 | Backup made | Hosting panel or backup plugin | Date, method, where it's stored |
| B2 | WordPress version | Dashboard → Updates (Aktualisierungen) | |
| B3 | Theme and version | Appearance → Themes (Design → Themes) | |
| B4 | Active plugins | Plugins → Installed plugins (screenshot of the full list) | |
| B5 | "Discourage search engines" | Settings → Reading (Einstellungen → Lesen) | Ticked / not ticked |
| B6 | Site title and tagline | Settings → General (Einstellungen → Allgemein) | |
| B7 | Permalink structure and category base | Settings → Permalinks | |
| B8 | SEO plugin and version | Plugins | Yoast / Rank Math / All in One SEO / SEOPress / none |
| B9 | Index settings for tag, date and author archives | SEO plugin settings | index / noindex |
| B10 | Sitemap URL | SEO plugin, or try /sitemap_index.xml and /wp-sitemap.xml | |
| B11 | robots.txt | Open blog.softexpress.de/robots.txt, copy the text | |
| B12 | Homepage title and meta description | Homepage → right-click → View page source → look for `<title>` and `name="description"` | |
| B13 | Existing tracking | Page source: search for `gtag`, `googletagmanager`, `matomo`, `etracker` | None / what was found |
| B14 | Cookie banner | Visit the blog in a private window | None / plugin name |
| B15 | Privacy policy link | Footer → where it points (blog page or main site) | |
| B16 | Imprint (Impressum) link | Footer → where it points | |
| B17 | Author profile | Users → Profile "softexpress": display name, bio | |
| B18 | Number of published posts and pages | Posts / Pages | |
| B19 | Page source saved (proof of the "before" state) | Homepage, 1 post, 1 category page: right-click → Save page as… (HTML only) | File names |

## 3. Approvals from the client

| Date | What was approved | Approved by | How (email, call, ticket) |
|---|---|---|---|
| | Cookie banner on the blog | | |
| | Google Analytics section in the privacy policy | | |
| | Google account that owns Search Console and GA4 | | |

## 4. Changes

Status: **Planned** · **Waiting for approval** · **Done** · **Rolled back**

| # | Date & time | Change | Where (WordPress menu) | Why | Before | After | Done by | How to undo | Status |
|---|---|---|---|---|---|---|---|---|---|
| C1 | | Full backup before the first change | Hosting panel or backup plugin | Safety net | – | Backup file and location | | – | Done |
| C2 | | Save page source and screenshots (B19) | Browser | Proof of the "before" state | – | Files saved | | – | Planned |
| C3 | | Install and activate Yoast SEO (free). Only if B8 shows no other SEO plugin | Plugins → Add new | Titles, meta descriptions, sitemap, index settings | See B8 | Yoast version: | | Deactivate and delete the plugin | Planned |
| C4 | | Yoast first-time configuration: record every answer (Organization "SoftExpress GmbH", logo, LinkedIn page) | Yoast SEO → General → First-time configuration | Correct company data for Google | – | Answers: | | Change in Yoast settings | Planned |
| C5 | | Verify Search Console, URL-prefix property `https://blog.softexpress.de/`, with the HTML tag | Yoast SEO → Settings → Site connections → Google | Search data for the blog | No property | Verified | | Remove the code and the property | Planned |
| C6 | | Add a SoftExpress contact as Owner in Search Console | Search Console → Settings → Users and permissions | The client owns the data | – | Owner: | | Remove the user | Waiting for approval |
| C7 | | Submit the Yoast sitemap | Search Console → Sitemaps → `sitemap_index.xml` | Help Google find all posts | See B10 | Submitted | | Remove the sitemap | Planned |
| C8 | | Record the results baseline (Part 5, "Before" column) | Search Console, PageSpeed Insights | Prove the results later | – | Filled in | | – | Planned |
| C9 | | Set tag, date and author archives to noindex | Yoast SEO → Settings → Taxonomies / Advanced | Stop thin pages competing with articles | See B9 | noindex | | Set back to index | Planned |
| C10 | | Set the tagline | Settings → General | Clear blog description | See B6 | Text from `blog-bio.md` | | Paste back the old text | Planned |
| C11 | | Set the homepage SEO title and meta description | Yoast SEO → Settings → Homepage | Better search snippet | See B12 | Text from `blog-bio.md` | | Paste back the old text | Planned |
| C12 | | Update the author bio | Users → Profile | Author box | See B17 | Text from `blog-bio.md` | | Paste back the old text | Planned |
| C13 | | Cookie banner with Google Consent Mode v2 | Plugins | Legally required before GA4 | See B14 | Plugin and version: | | Deactivate the plugin | Waiting for approval |
| C14 | | Add a Google Analytics section to the privacy policy | Depends on B15 | Legally required before GA4 | – | – | Client | Client | Waiting for approval |
| C15 | | Create the GA4 property and install the tag (one place only) | GA4 Admin + Site Kit or the cookie plugin | Visitor data | No GA4 | Measurement ID: G-… | | Remove the tag, delete the property | Waiting for approval |
| C16 | | GA4 settings: 14-month retention, Google Signals off, internal traffic filter, data processing terms accepted | GA4 Admin | GDPR and clean data | – | – | | Change back in GA4 Admin | Planned |

## 5. Results – before vs after

Fill in "Before" right after Search Console is verified (C8).
Always compare periods of the same length. Seasons matter, so where possible
also compare with the same months of the previous year.

| KPI | Where | Before (date: ____) | After 3 months | After 6 months |
|---|---|---|---|---|
| Clicks from Google, last 3 months | Search Console → Performance | | | |
| Impressions, last 3 months | Search Console → Performance | | | |
| Average CTR | Search Console → Performance | | | |
| Average position | Search Console → Performance | | | |
| Number of search queries with impressions | Search Console → Performance → Queries (export) | | | |
| Pages indexed / not indexed | Search Console → Pages | | | |
| Core Web Vitals (mobile) | Search Console → Core Web Vitals | | | |
| PageSpeed score, homepage (mobile / desktop) | pagespeed.web.dev, save the report link | | | |
| PageSpeed score, one post (mobile / desktop) | pagespeed.web.dev, save the report link | | | |
| Posts published per month | WordPress → Posts | | | |
| Visitors (users) per month | GA4, after C15 | – (no GA4 before) | | |
| Clicks from the blog to the shop | GA4, after C15 | – (no GA4 before) | | |
