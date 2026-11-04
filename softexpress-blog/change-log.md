# blog.softexpress.de – Change log

**Scope:** blog.softexpress.de only (WordPress admin access).
**Not in scope:** softexpress.de (shop), surffact.de, DNS, hosting.

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
| B8 | SEO plugin and version | Plugins | Yoast / Rank Math / none |
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
| C1 | | Full backup before the first change | Hosting panel or backup plugin | Safety net | – | Backup file and location | | – | Planned |
| C2 | | Install the "Site Kit by Google" plugin | Plugins → Add new | Connect Search Console | Not installed | Installed, version: | | Deactivate and delete the plugin | Planned |
| C3 | | Verify Search Console, URL-prefix property `https://blog.softexpress.de/` | Site Kit setup | Search data for the blog | No property | Verified | | Remove the property in Search Console | Planned |
| C4 | | Add a SoftExpress contact as Owner in Search Console | Search Console → Settings → Users and permissions | The client owns the data | – | Owner: | | Remove the user | Waiting for approval |
| C5 | | Submit the sitemap | Search Console → Sitemaps | Help Google find all posts | Not submitted | Sitemap URL: | | Remove the sitemap | Planned |
| C6 | | Set tag, date and author archives to noindex | SEO plugin → archive settings | Stop thin pages competing with articles | See B9 | noindex | | Set back to index | Planned |
| C7 | | Set the tagline | Settings → General | Clear blog description | See B6 | Text from `blog-bio.md` | | Paste back the old text | Planned |
| C8 | | Set the homepage SEO title and meta description | SEO plugin → homepage | Better search snippet | See B12 | Text from `blog-bio.md` | | Paste back the old text | Planned |
| C9 | | Update the author bio | Users → Profile | Author box | See B17 | Text from `blog-bio.md` | | Paste back the old text | Planned |
| C10 | | Cookie banner with Google Consent Mode v2 | Plugins | Legally required before GA4 | See B14 | Plugin and version: | | Deactivate the plugin | Waiting for approval |
| C11 | | Add a Google Analytics section to the privacy policy | Depends on B15 | Legally required before GA4 | – | – | Client | Client | Waiting for approval |
| C12 | | Create the GA4 property and install the tag (one place only) | GA4 Admin + Site Kit or the cookie plugin | Visitor data | No GA4 | Measurement ID: G-… | | Remove the tag, delete the property | Waiting for approval |
| C13 | | GA4 settings: 14-month retention, Google Signals off, internal traffic filter, data processing terms accepted | GA4 Admin | GDPR and clean data | – | – | | Change back in GA4 Admin | Planned |
