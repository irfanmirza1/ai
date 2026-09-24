# Munchlings: Brand Images and Where to Upload Them

| File | Where it goes |
|---|---|
| `profile-800.png` | Profile picture on **YouTube, Instagram, TikTok, Pinterest and Facebook** |
| `youtube-banner-2560x1440.png` | YouTube Studio → Customization → Branding → **Banner image** |
| `facebook-cover-1640x624.png` | Facebook → **Cover photo** |
| `og-image-1200x630.png` | Link preview picture for the website (already built into the website) |

**Source files:** `source/veggies.js` draws the 5 characters and `source/render.js` makes the images. To re-create the images, run `node render.js out` in a folder that has Playwright and the `fonts/` folder.

## YouTube Studio settings (step by step)

1. **Customization → Branding:**
   - Picture: upload `profile-800.png`
   - Banner: upload `youtube-banner-2560x1440.png`
   - Click **Publish**
2. **Customization → Basic info:**
   - Description (German): copy it from `accounts-setup.md`
   - Links: add **Website https://www.munchlings.de**, **Instagram**, **TikTok** and **Pinterest**
   - Contact email: munchlings16@gmail.com
   - Click **Publish**
3. **Settings → Channel:**
   - **Basic info:** Country **Germany**, plus the keywords from `accounts-setup.md`
   - **Advanced settings:** "Yes, set this channel as made for kids"
   - Click **Save**
4. **Settings → Upload defaults:**
   - **Language:** German
   - **Category:** Education
5. **Languages** (left menu): add **English** as a second language for the title and description.
