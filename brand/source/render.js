const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { char } = require('./veggies');

const OUT_DIR = process.argv[2] || path.join(__dirname, 'out');
fs.mkdirSync(OUT_DIR, { recursive: true });
const b64 = (f) => fs.readFileSync(path.join(__dirname, 'fonts', f)).toString('base64');
const fontCss = `
@font-face{font-family:Fredoka;src:url(data:font/woff2;base64,${b64('fredoka.woff2')}) format('woff2');font-weight:300 700}
@font-face{font-family:Nunito;src:url(data:font/woff2;base64,${b64('nunito.woff2')}) format('woff2');font-weight:200 1000}
html,body{margin:0;padding:0}`;

const GREEN = '#4CAF50', DARK = '#1F5E2A', CREAM = '#FFF8E7';

// Wordmark: white letters with a thick dark outline, drawn with SVG text.
function wordmark(x, y, size, anchor = 'middle', fill = '#fff', stroke = DARK) {
  return `<text x="${x}" y="${y}" text-anchor="${anchor}" font-family="Fredoka" font-weight="700" font-size="${size}"
    fill="${fill}" stroke="${stroke}" stroke-width="${size * 0.12}" paint-order="stroke" stroke-linejoin="round" letter-spacing="${size * 0.01}">Munchlings</text>`;
}

function confetti(w, h, n, seed = 7) {
  let s = seed; const rnd = () => (s = (s * 9301 + 49297) % 233280) / 233280;
  const cols = ['#FFD23F', '#FF8A1F', '#E8412C', '#5DBB4F', '#FFFFFF'];
  let out = '';
  for (let i = 0; i < n; i++) {
    const x = rnd() * w, y = rnd() * h, r = 4 + rnd() * 8, c = cols[i % cols.length];
    out += `<circle cx="${x}" cy="${y}" r="${r}" fill="${c}" opacity="${0.35 + rnd() * 0.4}"/>`;
  }
  return out;
}

const assets = {
  // 800x800 profile picture (YouTube, Instagram, TikTok, Pinterest, Facebook). Circle-safe.
  'profile-800.png': [800, 800, `
    <svg xmlns="http://www.w3.org/2000/svg" width="800" height="800">
      <defs><radialGradient id="g" cx="50%" cy="40%" r="65%"><stop offset="0" stop-color="#8BD65A"/><stop offset="1" stop-color="#3E9B3A"/></radialGradient></defs>
      <rect width="800" height="800" fill="url(#g)"/>
      ${confetti(800, 800, 26, 3)}
      <circle cx="400" cy="400" r="372" fill="none" stroke="#fff" stroke-width="14" opacity=".9"/>
      ${char('coco', 118, 150, 1.15, -8)}
      ${char('bob', 210, 120, 1.15, -3)}
      ${char('kai', 404, 118, 1.15, 3)}
      ${char('pete', 480, 158, 1.15, 7)}
      ${char('tim', 293, 188, 1.2, 0)}
      <rect x="95" y="455" width="610" height="170" rx="85" fill="${CREAM}" stroke="${DARK}" stroke-width="10"/>
      ${wordmark(400, 575, 124, 'middle', '#FF8A1F', DARK)}
    </svg>`],

  // 2560x1440 YouTube banner. Everything important inside the centre 1546x423 (x 507-2053, y 508-931).
  'youtube-banner-2560x1440.png': [2560, 1440, `
    <svg xmlns="http://www.w3.org/2000/svg" width="2560" height="1440">
      <defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#CFF1FF"/><stop offset=".62" stop-color="${CREAM}"/></linearGradient></defs>
      <rect width="2560" height="1440" fill="url(#sky)"/>
      <circle cx="2250" cy="560" r="110" fill="#FFD23F" opacity=".9"/>
      ${confetti(2560, 900, 70, 11)}
      <path d="M0,960 Q400,860 800,940 T1600,930 T2560,920 V1440 H0 Z" fill="#8BD65A"/>
      <path d="M0,1010 Q500,930 1100,1000 T2560,990 V1440 H0 Z" fill="#5DBB4F"/>
      <g fill="#fff" opacity=".9"><ellipse cx="420" cy="620" rx="120" ry="38"/><ellipse cx="490" cy="596" rx="80" ry="40"/><ellipse cx="2150" cy="720" rx="130" ry="40"/><ellipse cx="2080" cy="698" rx="80" ry="38"/></g>
      ${wordmark(1280, 625, 128)}
      <text x="1280" y="690" text-anchor="middle" font-family="Nunito" font-weight="800" font-size="44" fill="${DARK}">Lustige Gemüse-Abenteuer &amp; einfache Kinderrezepte</text>
      <text x="1280" y="736" text-anchor="middle" font-family="Nunito" font-weight="700" font-size="32" fill="#3A7D44">Fun veggie adventures &amp; easy kids recipes · Neue Folge jede Woche 🇩🇪 🇬🇧</text>
      ${['coco', 'bob', 'tim', 'pete', 'kai'].map((n, i) => char(n, 870 + i * 175, 770, .6, [-6, -2, 0, 3, 6][i])).join('')}
    </svg>`],

  // Facebook cover 1640x624 (content kept in the middle).
  'facebook-cover-1640x624.png': [1640, 624, `
    <svg xmlns="http://www.w3.org/2000/svg" width="1640" height="624">
      <defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#CFF1FF"/><stop offset="1" stop-color="${CREAM}"/></linearGradient></defs>
      <rect width="1640" height="624" fill="url(#sky)"/>
      ${confetti(1640, 500, 40, 5)}
      <path d="M0,520 Q400,470 820,510 T1640,500 V624 H0 Z" fill="#5DBB4F"/>
      ${wordmark(480, 280, 120)}
      <text x="480" y="345" text-anchor="middle" font-family="Nunito" font-weight="800" font-size="34" fill="${DARK}">Lustige Gemüse-Abenteuer &amp; Kinderrezepte</text>
      <text x="480" y="392" text-anchor="middle" font-family="Nunito" font-weight="700" font-size="30" fill="#3A7D44">Fun veggie adventures &amp; easy kids recipes</text>
      ${['coco','bob','tim','pete','kai'].map((n,i)=>char(n, 905 + i*135, 250, 1.0, [-6,-2,0,3,6][i])).join('')}
    </svg>`],

  // Open Graph / link preview image for the website 1200x630.
  'og-image-1200x630.png': [1200, 630, `
    <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630">
      <rect width="1200" height="630" fill="${CREAM}"/>
      ${confetti(1200, 630, 30, 9)}
      <path d="M0,520 Q300,480 600,515 T1200,505 V630 H0 Z" fill="#5DBB4F"/>
      ${wordmark(600, 160, 130)}
      <text x="600" y="228" text-anchor="middle" font-family="Nunito" font-weight="800" font-size="38" fill="${DARK}">Lustige Gemüse-Abenteuer &amp; Kinderrezepte</text>
      ${char('coco', 150, 270, 1.1, -6)}${char('bob', 330, 290, 1.05, -2)}${char('tim', 500, 320, 1, 0)}${char('pete', 690, 290, 1.05, 3)}${char('kai', 870, 270, 1.1, 5)}
    </svg>`],

  'lineup-preview.png': [1100, 320, `
    <svg xmlns="http://www.w3.org/2000/svg" width="1100" height="320"><rect width="1100" height="320" fill="#fff"/>
      ${['bob', 'coco', 'tim', 'pete', 'kai'].map((n, i) => char(n, 20 + i * 215, 30, 1)).join('')}
    </svg>`],
};

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const only = process.argv[3];
  for (const [file, [w, h, svg]] of Object.entries(assets)) {
    if (only && !file.startsWith(only)) continue;
    await page.setViewportSize({ width: w, height: h });
    await page.setContent(`<html><head><style>${fontCss}</style></head><body>${svg}</body></html>`);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(OUT_DIR, file), clip: { x: 0, y: 0, width: w, height: h } });
    console.log('wrote', file);
  }
  await browser.close();
})();
