// Munchlings character drawings. Each character lives in a 200x260 box, feet at y≈250.
const OUT = '#2B2B2B';

function eyes(cx, cy, s = 1, look = 0) {
  const e = (x) => `
    <ellipse cx="${x}" cy="${cy}" rx="${12 * s}" ry="${14 * s}" fill="#fff" stroke="${OUT}" stroke-width="${2.5 * s}"/>
    <circle cx="${x + look * s}" cy="${cy + 2 * s}" r="${7 * s}" fill="${OUT}"/>
    <circle cx="${x + look * s + 2.5 * s}" cy="${cy - 1.5 * s}" r="${2.6 * s}" fill="#fff"/>`;
  return e(cx - 19 * s) + e(cx + 19 * s);
}

function smile(cx, cy, s = 1, open = true) {
  if (!open) return `<path d="M${cx - 13 * s},${cy} Q${cx},${cy + 13 * s} ${cx + 13 * s},${cy}" fill="none" stroke="${OUT}" stroke-width="${3.5 * s}" stroke-linecap="round"/>`;
  return `<path d="M${cx - 15 * s},${cy} Q${cx},${cy + 22 * s} ${cx + 15 * s},${cy} Z" fill="#7A2E2E" stroke="${OUT}" stroke-width="${3 * s}" stroke-linejoin="round"/>
    <path d="M${cx - 7 * s},${cy + 9 * s} Q${cx},${cy + 5 * s} ${cx + 7 * s},${cy + 9 * s} Q${cx},${cy + 15 * s} ${cx - 7 * s},${cy + 9 * s} Z" fill="#FF8C8C"/>`;
}

function cheeks(cx, cy, s = 1) {
  return `<ellipse cx="${cx - 33 * s}" cy="${cy}" rx="${9 * s}" ry="${5.5 * s}" fill="#FF7B9C" opacity=".55"/>
    <ellipse cx="${cx + 33 * s}" cy="${cy}" rx="${9 * s}" ry="${5.5 * s}" fill="#FF7B9C" opacity=".55"/>`;
}

function face(cx, cy, s = 1, look = 0) {
  return eyes(cx, cy, s, look) + cheeks(cx, cy + 20 * s, s) + smile(cx, cy + 20 * s, s);
}

function feet(x1, x2, y, col) {
  return `<ellipse cx="${x1}" cy="${y}" rx="17" ry="9" fill="${col}" stroke="${OUT}" stroke-width="3"/>
    <ellipse cx="${x2}" cy="${y}" rx="17" ry="9" fill="${col}" stroke="${OUT}" stroke-width="3"/>`;
}

function arm(x1, y1, x2, y2, col) {
  return `<path d="M${x1},${y1} Q${(x1 + x2) / 2},${Math.min(y1, y2) - 8} ${x2},${y2}" fill="none" stroke="${OUT}" stroke-width="13" stroke-linecap="round"/>
    <path d="M${x1},${y1} Q${(x1 + x2) / 2},${Math.min(y1, y2) - 8} ${x2},${y2}" fill="none" stroke="${col}" stroke-width="7" stroke-linecap="round"/>`;
}

const chars = {
  bob() { // Broccoli Bob
    const floret = [[52, 92, 36], [148, 92, 36], [75, 60, 38], [125, 60, 38], [100, 45, 36], [100, 92, 40]];
    return `
      ${feet(80, 120, 246, '#6FB644')}
      ${arm(68, 175, 38, 150, '#9BD16B')}${arm(132, 175, 162, 150, '#9BD16B')}
      <rect x="64" y="110" width="72" height="132" rx="30" fill="#9BD16B" stroke="${OUT}" stroke-width="4"/>
      ${floret.map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#3F9B3A" stroke="${OUT}" stroke-width="4"/>`).join('')}
      ${floret.map(([x, y, r]) => `<circle cx="${x - r * .25}" cy="${y - r * .25}" r="${r * .45}" fill="#5DBB4F"/>`).join('')}
      ${face(100, 158, .95)}`;
  },
  coco() { // Carrot Coco
    return `
      ${feet(84, 116, 246, '#E86F0C')}
      <g stroke="${OUT}" stroke-width="4">
        <path d="M100,62 C88,30 70,18 58,8 C80,14 96,28 100,52 Z" fill="#46B04A"/>
        <path d="M100,62 C104,30 118,10 140,4 C126,22 112,40 104,60 Z" fill="#46B04A"/>
        <path d="M100,60 C98,36 100,16 104,0 C110,20 108,42 102,62 Z" fill="#5CC75C"/>
      </g>
      ${arm(58, 130, 30, 110, '#FF9A3C')}${arm(142, 130, 170, 110, '#FF9A3C')}
      <path d="M52,92 Q52,58 100,58 Q148,58 148,92 Q146,172 100,244 Q54,172 52,92 Z" fill="#FF8A1F" stroke="${OUT}" stroke-width="4"/>
      <path d="M66,170 q12,-4 20,0 M112,190 q10,-4 18,0 M70,205 q8,-3 14,0" stroke="#D96A0A" stroke-width="4" fill="none" stroke-linecap="round"/>
      <g fill="#C8620A" opacity=".55"><circle cx="72" cy="120" r="2.4"/><circle cx="79" cy="126" r="2.4"/><circle cx="121" cy="120" r="2.4"/><circle cx="128" cy="126" r="2.4"/></g>
      ${face(100, 100, .95)}`;
  },
  tim() { // Tomato Tim
    return `
      ${feet(76, 124, 246, '#C22E1E')}
      ${arm(34, 160, 12, 132, '#F0553F')}${arm(166, 160, 188, 132, '#F0553F')}
      <circle cx="100" cy="160" r="80" fill="#E8412C" stroke="${OUT}" stroke-width="4"/>
      <ellipse cx="68" cy="122" rx="20" ry="12" fill="#fff" opacity=".35" transform="rotate(-30 68 122)"/>
      <path d="M100,86 L86,70 L100,76 L108,58 L112,78 L130,72 L116,88 L126,98 L106,94 L100,108 L94,94 L74,98 L86,86 Z" fill="#46B04A" stroke="${OUT}" stroke-width="3.5" stroke-linejoin="round" transform="rotate(-12 100 86)"/>
      <rect x="102" y="54" width="8" height="18" rx="4" fill="#3A8F3E" stroke="${OUT}" stroke-width="3" transform="rotate(-12 100 86)"/>
      ${face(100, 150, 1.05, 1.5)}`;
  },
  pete() { // Potato Pete
    return `
      ${feet(78, 122, 246, '#A87B45')}
      ${arm(30, 150, 10, 124, '#D6AA6B')}${arm(170, 150, 190, 124, '#D6AA6B')}
      <ellipse cx="100" cy="148" rx="76" ry="96" fill="#C99A5B" stroke="${OUT}" stroke-width="4"/>
      <g fill="#A87B45"><ellipse cx="62" cy="96" rx="5" ry="3.5"/><ellipse cx="140" cy="110" rx="4" ry="3"/><ellipse cx="58" cy="170" rx="4" ry="3"/><ellipse cx="146" cy="180" rx="5" ry="3.5"/></g>
      <path d="M58,178 Q100,168 142,178 L136,236 Q100,248 64,236 Z" fill="#fff" stroke="${OUT}" stroke-width="3.5"/>
      <rect x="86" y="196" width="28" height="18" rx="5" fill="none" stroke="#E0E0E0" stroke-width="3"/>
      ${face(100, 120, 1)}
      <g fill="none" stroke="${OUT}" stroke-width="4"><circle cx="81" cy="120" r="19"/><circle cx="119" cy="120" r="19"/><path d="M100,118 h0"/><path d="M96,117 q4,-4 8,0"/></g>`;
  },
  kai() { // Kernel Kai
    let kernels = '';
    for (let r = 0; r < 9; r++) for (let c = 0; c < 4; c++) {
      const x = 72 + c * 16 + (r % 2 ? 8 : 0), y = 58 + r * 19;
      if (x > 128) continue;
      kernels += `<rect x="${x}" y="${y}" width="13" height="15" rx="6" fill="#FFE27A" stroke="#E0A800" stroke-width="1.5"/>`;
    }
    return `
      ${feet(82, 118, 246, '#E0A800')}
      ${arm(64, 150, 34, 122, '#FFD23F')}${arm(136, 150, 166, 122, '#FFD23F')}
      <g stroke="${OUT}" stroke-width="3" fill="#F7E7A0"><path d="M92,40 C84,20 88,8 96,2 C94,16 98,28 100,40 Z"/><path d="M104,40 C108,20 118,12 126,8 C118,20 110,30 108,42 Z"/><path d="M96,40 C88,26 76,20 66,20 C78,26 86,34 92,44 Z"/></g>
      <rect x="62" y="38" width="76" height="200" rx="38" fill="#FFD23F" stroke="${OUT}" stroke-width="4"/>
      <clipPath id="kaiClip"><rect x="62" y="38" width="76" height="200" rx="38"/></clipPath>
      <g clip-path="url(#kaiClip)">${kernels}</g>
      <path d="M62,238 C40,200 36,160 50,120 C60,160 72,196 100,238 Z" fill="#5CC75C" stroke="${OUT}" stroke-width="4" stroke-linejoin="round"/>
      <path d="M138,238 C160,200 164,160 150,120 C140,160 128,196 100,238 Z" fill="#46B04A" stroke="${OUT}" stroke-width="4" stroke-linejoin="round"/>
      <ellipse cx="100" cy="118" rx="36" ry="34" fill="#FFD23F"/>
      ${face(100, 108, .85)}`;
  },
};

function char(name, x, y, scale = 1, rot = 0) {
  return `<g transform="translate(${x} ${y}) rotate(${rot} ${100 * scale} ${130 * scale}) scale(${scale})">${chars[name]()}</g>`;
}

function standalone(name) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -4 200 264" width="200" height="264">${chars[name]()}</svg>`;
}

module.exports = { chars, char, standalone };
