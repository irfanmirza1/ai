#!/usr/bin/env python3
"""Build the recipe pages for munchlings.de.

Writes website/rezepte/*.html (German) and website/en/recipes/*.html (English),
plus an index page for each language. Add a new recipe to RECIPES and run:

    python3 tools/make_recipes.py
"""
import html
import json
from pathlib import Path

SITE = "https://www.munchlings.de"
ROOT = Path(__file__).resolve().parent.parent / "website"
YOUTUBE = "https://www.youtube.com/channel/UCeb5TiEV0HajChm5p1zjoGw"

RECIPES = [
    {
        "slug": {"de": "brokkoli-kaese-happen", "en": "broccoli-cheese-bites"},
        "character": "bob",
        "episode": 1,
        "prep": 10, "cook": 18,
        "yield": {"de": "ca. 12 Happen", "en": "about 12 bites"},
        "de": {
            "name": "Brokkoli-Käse-Happen",
            "episode": "Brokkoli Bob will eine Superkraft!",
            "intro": "Aus Folge 1: Brokkoli Bob lernt, dass er schon eine Superkraft hat. Diese kleinen „Bäumchen“ sind außen goldbraun und innen weich.",
            "ingredients": ["1 Tasse gekochter Brokkoli, fein gehackt", "1 Ei", "½ Tasse geriebener Käse (z. B. halal-zertifiziert)"],
            "steps": [
                ("adult", "Den Ofen auf 180 °C (Ober-/Unterhitze) vorheizen. Ein Blech mit Backpapier auslegen."),
                ("adult", "Den gekochten Brokkoli fein hacken."),
                ("kid", "Brokkoli, Ei und Käse in einer Schüssel gut verrühren."),
                ("kid", "Mit einem Teelöffel kleine Häufchen aufs Blech setzen und leicht flach drücken."),
                ("adult", "15–18 Minuten backen, bis die Happen goldbraun sind."),
                ("adult", "5 Minuten abkühlen lassen, dann servieren."),
            ],
            "allergens": "Ei, Milch (Käse)",
            "safety": "Für Kinder unter 4 Jahren die Happen in kleine Stücke teilen und vorher abkühlen lassen.",
            "fact": "Brokkoli besteht aus winzigen Blütenknospen.",
            "word": "Röschen",
            "keywords": "Brokkoli Kinder, Kinderrezept, 3 Zutaten, Fingerfood Kinder",
            "category": "Snack", "cuisine": "International",
        },
        "en": {
            "name": "Broccoli Cheese Bites",
            "episode": "Broccoli Bob Wants a Superpower!",
            "intro": "From Episode 1: Broccoli Bob learns he already has a superpower. These little “tiny trees” are golden outside and soft inside.",
            "ingredients": ["1 cup cooked broccoli, finely chopped", "1 egg", "½ cup grated cheese (halal-certified if you like)"],
            "steps": [
                ("adult", "Heat the oven to 180°C (350°F). Line a baking tray with baking paper."),
                ("adult", "Finely chop the cooked broccoli."),
                ("kid", "Mix the broccoli, egg and cheese together in a bowl."),
                ("kid", "Put small spoonfuls on the tray and press them a little flat."),
                ("adult", "Bake for 15–18 minutes, until golden."),
                ("adult", "Let them cool for 5 minutes, then serve."),
            ],
            "allergens": "egg, dairy (cheese)",
            "safety": "For children under 4, break the bites into small pieces and let them cool first.",
            "fact": "Broccoli is made of tiny flower buds.",
            "word": "Floret",
            "keywords": "broccoli for kids, kids recipe, 3 ingredients, finger food",
            "category": "Snack", "cuisine": "International",
        },
    },
    {
        "slug": {"de": "mini-pizza-toasts", "en": "mini-pizza-toasts"},
        "character": "tim",
        "episode": 2,
        "prep": 5, "cook": 8,
        "yield": {"de": "8 Mini-Toasts", "en": "8 mini toasts"},
        "de": {
            "name": "Mini-Pizza-Toasts",
            "episode": "Tomaten-Tims großes Hoppla!",
            "intro": "Aus Folge 2: Tim sagt Entschuldigung, und dann machen alle zusammen etwas Leckeres. Der schnellste Pizza-Snack der Welt!",
            "ingredients": ["2 Scheiben Brot", "2 EL Tomatensoße", "½ Tasse geriebener Käse (z. B. halal-zertifiziert)"],
            "steps": [
                ("adult", "Den Ofen auf 200 °C (Ober-/Unterhitze) vorheizen."),
                ("adult", "Jede Brotscheibe in 4 kleine Quadrate schneiden und aufs Blech legen."),
                ("kid", "Etwas Tomatensoße auf jedes Stück streichen."),
                ("kid", "Den Käse darüberstreuen."),
                ("adult", "6–8 Minuten backen, bis der Käse geschmolzen ist."),
                ("adult", "2 Minuten abkühlen lassen: geschmolzener Käse ist sehr heiß!"),
            ],
            "allergens": "Gluten (Brot), Milch (Käse)",
            "safety": "Geschmolzener Käse bleibt lange heiß. Vor dem Servieren kurz prüfen.",
            "fact": "Eine Tomate hat Samen im Inneren – eigentlich ist sie eine Frucht!",
            "word": "Samen",
            "keywords": "Pizzatoast Kinder, Kinderrezept, 3 Zutaten, schneller Snack",
            "category": "Snack", "cuisine": "Italienisch",
        },
        "en": {
            "name": "Mini Pizza Toasts",
            "episode": "Tomato Tim's Big Oops!",
            "intro": "From Episode 2: Tim says sorry, and then everyone makes something yummy together. The fastest pizza snack ever!",
            "ingredients": ["2 slices of bread", "2 tbsp tomato sauce", "½ cup grated cheese (halal-certified if you like)"],
            "steps": [
                ("adult", "Heat the oven to 200°C (400°F)."),
                ("adult", "Cut each slice of bread into 4 small squares and put them on a baking tray."),
                ("kid", "Spread a little tomato sauce on each square."),
                ("kid", "Sprinkle the cheese on top."),
                ("adult", "Bake for 6–8 minutes, until the cheese melts."),
                ("adult", "Let them cool for 2 minutes: melted cheese is very hot!"),
            ],
            "allergens": "gluten (bread), dairy (cheese)",
            "safety": "Melted cheese stays hot for a long time. Check it before serving.",
            "fact": "A tomato has seeds inside, so it's really a fruit!",
            "word": "Seed",
            "keywords": "pizza toast for kids, kids recipe, 3 ingredients, quick snack",
            "category": "Snack", "cuisine": "Italian",
        },
    },
    {
        "slug": {"de": "paratha", "en": "paratha"},
        "character": "pete",
        "episode": 3,
        "prep": 25, "cook": 10,
        "yield": {"de": "3 Parathas", "en": "3 parathas"},
        "de": {
            "name": "Einfaches Paratha",
            "episode": "Essens-Reisepass: PAKISTAN!",
            "intro": "Aus Folge 3: Die Zauber-Brotdose bringt die Munchlings nach Pakistan. Paratha ist ein rundes, blättriges Brot, das dort viele zum Frühstück lieben. Mazedaar!",
            "ingredients": ["1 Tasse Weizenmehl (Atta) mit einer Prise Salz", "ca. ⅓ Tasse Wasser", "Ghee oder Butter"],
            "steps": [
                ("kid", "Mehl und Salz in eine Schüssel geben. Nach und nach das Wasser dazugeben und zu einem weichen Teig kneten."),
                ("kid", "Den Teig abgedeckt 15 Minuten ruhen lassen. Dann in 3 Kugeln teilen."),
                ("kid", "Eine Kugel flach ausrollen und dünn mit Ghee bestreichen."),
                ("kid", "Den Teig zur Hälfte falten, nochmal falten, dann wieder ausrollen. So entstehen die Schichten!"),
                ("adult", "Eine Pfanne (oder Tawa) auf mittlerer Stufe heiß werden lassen. Das Paratha 1–2 Minuten pro Seite mit etwas Ghee braten, bis es goldene Flecken hat."),
                ("adult", "Kurz abkühlen lassen, dann in Stücke reißen und genießen."),
            ],
            "allergens": "Gluten (Mehl), Milch (Ghee/Butter)",
            "safety": "Die Pfanne wird sehr heiß: Das Braten übernimmt nur ein Erwachsener.",
            "fact": "Paratha ist so blättrig, weil der Teig in Schichten gefaltet wird.",
            "word": "Mazedaar! (Urdu für „lecker“)",
            "keywords": "Paratha Rezept, pakistanisches Essen Kinder, Kinderrezept, 3 Zutaten",
            "category": "Frühstück", "cuisine": "Pakistanisch",
        },
        "en": {
            "name": "Simple Paratha",
            "episode": "Food Passport: PAKISTAN!",
            "intro": "From Episode 3: the Magic Lunchbox takes the Munchlings to Pakistan. Paratha is a round, flaky flatbread that many people there love for breakfast. Mazedaar!",
            "ingredients": ["1 cup wheat flour (atta) with a pinch of salt", "about ⅓ cup water", "ghee or butter"],
            "steps": [
                ("kid", "Put the flour and salt in a bowl. Add the water a little at a time and knead it into a soft dough."),
                ("kid", "Cover the dough and let it rest for 15 minutes. Then split it into 3 balls."),
                ("kid", "Roll one ball flat and spread a thin layer of ghee on it."),
                ("kid", "Fold the dough in half, fold it again, then roll it flat again. That makes the layers!"),
                ("adult", "Heat a pan (or tawa) on medium. Cook the paratha for 1–2 minutes on each side with a little ghee, until it has golden spots."),
                ("adult", "Let it cool a little, then tear it into pieces and enjoy."),
            ],
            "allergens": "gluten (flour), dairy (ghee/butter)",
            "safety": "The pan gets very hot: only a grown-up does the cooking.",
            "fact": "Paratha is flaky because the dough is folded into layers.",
            "word": "Mazedaar! (Urdu for “delicious”)",
            "keywords": "paratha recipe, Pakistani food for kids, kids recipe, 3 ingredients",
            "category": "Breakfast", "cuisine": "Pakistani",
        },
    },
]

TEXT = {
    "de": {
        "dir": "rezepte", "home": "../", "assets": "../assets", "other": "en",
        "index_title": "Rezepte", "index_sub": "Alle Rezepte aus den Munchlings-Folgen – mit nur 3 Zutaten, zum Nachmachen mit Erwachsenen.",
        "index_meta": "Einfache Kinderrezepte mit nur 3 Zutaten aus den Munchlings-Folgen: zum Ausdrucken und Nachkochen mit Erwachsenen.",
        "episode": "Folge", "prep": "Vorbereitung", "cook": "Backen/Braten", "min": "Min.", "makes": "Ergibt",
        "ingredients": "Zutaten", "steps": "So geht's", "adult": "👩 Erwachsene", "count": "3 Zutaten",
        "allergens": "Enthält", "fact": "🧠 Der Fakt", "word": "🔤 Das Wort", "print": "🖨️ Rezept ausdrucken",
        "watch": "▶ Folge auf YouTube ansehen", "all": "Alle Rezepte", "start": "Start", "note": "Immer mit einem Erwachsenen kochen.",
        "footer": '<a href="{home}impressum.html">Impressum</a> · <a href="{home}datenschutz.html">Datenschutz</a>',
    },
    "en": {
        "dir": "en/recipes", "home": "../../", "assets": "../../assets", "other": "de",
        "index_title": "Recipes", "index_sub": "Every recipe from the Munchlings episodes – just 3 ingredients, to make with a grown-up.",
        "index_meta": "Easy 3-ingredient kids recipes from the Munchlings episodes: print them and cook them together with a grown-up.",
        "episode": "Episode", "prep": "Prep", "cook": "Cook", "min": "min", "makes": "Makes",
        "ingredients": "Ingredients", "steps": "How to make it", "adult": "👩 Grown-up", "count": "3 ingredients",
        "allergens": "Contains", "fact": "🧠 The fact", "word": "🔤 The word", "print": "🖨️ Print this recipe",
        "watch": "▶ Watch the episode on YouTube", "all": "All recipes", "start": "Home", "note": "Always cook with a grown-up.",
        "footer": '<a href="{home}impressum.html">Impressum (Legal notice)</a> · <a href="{home}datenschutz.html">Datenschutz (Privacy)</a>',
    },
}

e = html.escape


def url(lang, slug=""):
    return f"{SITE}/{TEXT[lang]['dir']}/{slug + '.html' if slug else ''}"


def head(lang, title, desc, page_url, alt_de, alt_en, assets, extra=""):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{page_url}">
<link rel="alternate" hreflang="de" href="{alt_de}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="icon" type="image/png" href="{assets}/img/favicon-64.png">
<link rel="apple-touch-icon" href="{assets}/img/logo-192.png">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:url" content="{page_url}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{assets}/style.css">
{extra}</head>
<body>
"""


def header(lang, t, other_href):
    other = "EN" if lang == "de" else "DE"
    return f"""
<header class="top">
  <div class="wrap">
    <a class="brand" href="{t['home'] if lang == 'de' else '../'}"><img src="{t['assets']}/img/logo-192.png" alt="">Munchlings</a>
    <nav class="nav">
      <a href="./">{t['all']}</a>
      <a class="lang" href="{other_href}" hreflang="{t['other']}">{other}</a>
    </nav>
  </div>
</header>
"""


def footer(t):
    return f"""
<footer>
  <div class="wrap">
    <span>© 2026 Munchlings</span>
    <span>{t['footer'].format(home=t['home'])}</span>
  </div>
</footer>
</body>
</html>
"""


def schema(lang, r):
    c = r[lang]
    return {
        "@context": "https://schema.org",
        "@type": "Recipe",
        "name": c["name"],
        "description": c["intro"],
        "image": [f"{SITE}/assets/img/og-image.png"],
        "author": {"@type": "Organization", "name": "Munchlings", "url": SITE + "/"},
        "inLanguage": lang,
        "prepTime": f"PT{r['prep']}M",
        "cookTime": f"PT{r['cook']}M",
        "totalTime": f"PT{r['prep'] + r['cook']}M",
        "recipeYield": r["yield"][lang],
        "recipeCategory": c["category"],
        "recipeCuisine": c["cuisine"],
        "keywords": c["keywords"],
        "recipeIngredient": c["ingredients"],
        "recipeInstructions": [{"@type": "HowToStep", "text": s} for _, s in c["steps"]],
    }


def recipe_page(lang, r):
    t, c = TEXT[lang], r[lang]
    slug = r["slug"][lang]
    other = "en" if lang == "de" else "de"
    other_href = (f"../en/recipes/{r['slug']['en']}.html" if lang == "de"
                  else f"../../rezepte/{r['slug']['de']}.html")
    ld = json.dumps(schema(lang, r), ensure_ascii=False, indent=1)
    extra = f'<script type="application/ld+json">\n{ld}\n</script>\n'
    desc = f"{c['name']}: {c['intro']}"
    out = head(lang, f"{c['name']} – Munchlings", desc, url(lang, slug),
               url("de", r["slug"]["de"]), url("en", r["slug"]["en"]), t["assets"], extra)
    out += header(lang, t, other_href)
    ingredients = "\n".join(f"      <li>{e(i)}</li>" for i in c["ingredients"])
    steps = "\n".join(f'      <li><span class="adult">{t["adult"]}</span> {e(s)}</li>' if who == "adult"
                      else f"      <li>{e(s)}</li>" for who, s in c["steps"])
    out += f"""
<main class="recipe">
  <p class="crumbs"><a href="{t['home'] if lang == 'de' else '../'}">{t['start']}</a> › <a href="./">{t['all']}</a></p>
  <h1>{e(c['name'])}</h1>
  <div class="intro">
    <img src="{t['assets']}/img/characters/{r['character']}.svg" alt="">
    <p>{e(c['intro'])}</p>
  </div>
  <ul class="facts">
    <li>🥕 {t['count']}</li>
    <li>⏱️ {t['prep']}: {r['prep']} {t['min']}</li>
    <li>🔥 {t['cook']}: {r['cook']} {t['min']}</li>
    <li>🍽️ {t['makes']}: {e(r['yield'][lang])}</li>
  </ul>

  <h2>{t['ingredients']}</h2>
  <div class="box">
    <ul>
{ingredients}
    </ul>
  </div>

  <h2>{t['steps']}</h2>
  <div class="box">
    <ol>
{steps}
    </ol>
  </div>
  <div class="note">
    <p><strong>⚠️ {t['note']}</strong> {e(c['safety'])}</p>
    <p><strong>{t['allergens']}:</strong> {e(c['allergens'])}</p>
  </div>

  <h2>{t['episode']} {r['episode']}: {e(c['episode'])}</h2>
  <div class="learn">
    <div class="box"><p><strong>{t['fact']}</strong></p><p>{e(c['fact'])}</p></div>
    <div class="box"><p><strong>{t['word']}</strong></p><p>{e(c['word'])}</p></div>
  </div>

  <div class="btns" style="justify-content:flex-start">
    <button class="btn print" onclick="window.print()">{t['print']}</button>
    <a class="btn alt print" href="{YOUTUBE}" rel="noopener">{t['watch']}</a>
  </div>
</main>
"""
    out += footer(t)
    return out


def index_page(lang):
    t = TEXT[lang]
    other_href = "../en/recipes/" if lang == "de" else "../../rezepte/"
    out = head(lang, f"{t['index_title']} – Munchlings", t["index_meta"], url(lang),
               url("de"), url("en"), t["assets"])
    out += header(lang, t, other_href)
    cards = "\n".join(
        f"""      <a href="{r['slug'][lang]}.html"><div class="card"><img src="{t['assets']}/img/characters/{r['character']}.svg" alt=""><h3>{e(r[lang]['name'])}</h3><p>{t['episode']} {r['episode']}: {e(r[lang]['episode'])}</p><p class="quote">{r['prep'] + r['cook']} {t['min']} · {t['count']}</p></div></a>"""
        for r in RECIPES)
    out += f"""
<main>
<section>
  <div class="wrap">
    <h2>{t['index_title']}</h2>
    <p class="sub">{e(t['index_sub'])}</p>
    <div class="recipe-list">
{cards}
    </div>
  </div>
</section>
</main>
"""
    out += footer(t)
    return out


def main():
    for lang in ("de", "en"):
        folder = ROOT / TEXT[lang]["dir"]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "index.html").write_text(index_page(lang), encoding="utf-8")
        for r in RECIPES:
            (folder / f"{r['slug'][lang]}.html").write_text(recipe_page(lang, r), encoding="utf-8")
        print(f"wrote {folder.relative_to(ROOT.parent)}/ ({len(RECIPES) + 1} pages)")


if __name__ == "__main__":
    main()
