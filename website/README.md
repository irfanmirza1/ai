# munchlings.de: Website Files

A simple, fast website: German at `/` and English at `/en/`. It uses **no cookies, no tracking and no Google Fonts** (the fonts are stored on your own server, which avoids GDPR problems in Germany).

## ⚠️ Before uploading

Open `impressum.html` and `datenschutz.html` and replace **every** yellow `[…]` field:
- your name
- your address
- the name and address of your hosting company
- how many days your server keeps its log files

**Don't publish the Impressum with placeholders.** German law requires real details.

## Upload with FileZilla (free)

1. Open FileZilla and enter your **FTP host, username and password**. Your hosting company gives you these.
2. On the right (the server side), open the web folder. It's often called `public_html`, `htdocs` or `www`.
3. Drag **everything inside this `website/` folder** into it. That means `index.html`, `impressum.html`, `datenschutz.html`, `en/` and `assets/`.
4. Open https://www.munchlings.de and check that the characters show up.

## Files

```
index.html          German homepage
en/index.html       English homepage
impressum.html      Impressum (fill in your details first)
datenschutz.html    Privacy policy (fill in your details first)
assets/style.css    Design
assets/fonts/       Fredoka and Nunito (self-hosted)
assets/img/         Logo, favicon, link preview picture, 5 character drawings
```
