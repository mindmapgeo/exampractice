#!/usr/bin/env python3
"""
Generate a standalone cheatsheet.html — just the Cheat Sheet tab, directly
linkable, without loading the rest of the study app (glossary data, quiz
engine, flashcards, etc).

index.html is the source of truth for the Cheat Sheet content and styling;
this script extracts it so the two never drift. Re-run after any edit to
the Cheat Sheet section in index.html.
"""
import re

SOURCE = "index.html"
OUTPUT = "cheatsheet.html"


def extract_balanced(content, start_marker):
    """Return the inner HTML of the first element matching start_marker,
    respecting nested <div>...</div> balance."""
    start = content.index(start_marker)
    tag_end = content.index(">", start) + 1
    depth = 1
    i = tag_end
    while depth > 0:
        next_open = content.find("<div", i)
        next_close = content.find("</div>", i)
        if next_close == -1:
            raise ValueError("unbalanced <div> while extracting " + start_marker)
        if next_open != -1 and next_open < next_close:
            depth += 1
            i = next_open + 4
        else:
            depth -= 1
            i = next_close + 6
    return content[tag_end : i - 6]


def main():
    with open(SOURCE, encoding="utf-8") as f:
        source = f.read()

    style_block = re.search(r"<style>.*?</style>", source, re.DOTALL).group(0)
    cheatsheet_body = extract_balanced(
        source, '<div class="tab-content" id="content-cheatsheet">'
    ).strip()
    # Drop the in-app "open as standalone page" link — it would just point
    # to this very page.
    cheatsheet_body = re.sub(
        r'\s*<a id="standaloneLink".*?</a>', "", cheatsheet_body, flags=re.DOTALL
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cheat Sheet — Medical Interpreter Study Guide</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
{style_block}
<style>
  .cs-page-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    padding: 16px 32px;
    border-bottom: 1px solid var(--border);
  }}
  .cs-back-link {{
    color: var(--text2);
    text-decoration: none;
    font-size: 13px;
    font-weight: 600;
  }}
  .cs-back-link:hover {{ color: var(--accent); }}
  main {{ max-width: 1100px; margin: 0 auto; padding: 32px; }}
</style>
</head>
<body>

<div class="cs-page-header">
  <a class="cs-back-link" href="index.html">← Full Study Guide</a>
  <select id="langToggle" onchange="changeLanguage(this.value)">
    <option value="english">🇺🇸 English</option>
    <option value="ukrainian">🇺🇸 ↔ 🇺🇦 English - Ukrainian</option>
    <option value="spanish">🇺🇸 ↔ 🇪🇸 English - Spanish</option>
  </select>
</div>

<main>
{cheatsheet_body}
</main>

<script src="ui_dict.js"></script>
<script src="version.js"></script>
<script>
let currentAppLang = localStorage.getItem('ges_lang') || 'english';
document.getElementById('langToggle').value = currentAppLang;

const originalTexts = new Map();

function translatePage() {{
  if (typeof UI_DICT === 'undefined') return;
  const langCode = currentAppLang === 'ukrainian' ? 'uk' : (currentAppLang === 'spanish' ? 'es' : 'en');

  const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
  let node;
  while (node = walk.nextNode()) {{
    const parent = node.parentNode;
    if (!parent) continue;
    if (['SCRIPT', 'STYLE', 'TEXTAREA', 'INPUT', 'SELECT', 'OPTION'].includes(parent.tagName)) continue;

    const rawVal = node.nodeValue;
    const text = rawVal.trim();
    if (text.length <= 1) continue;

    if (!originalTexts.has(node)) {{
      originalTexts.set(node, rawVal);
    }}

    const originalText = originalTexts.get(node).trim();
    if (UI_DICT[originalText]) {{
      const translation = UI_DICT[originalText][langCode];
      if (translation) {{
        const leading = originalTexts.get(node).match(/^\\s*/)[0];
        const trailing = originalTexts.get(node).match(/\\s*$/)[0];
        node.nodeValue = leading + translation + trailing;
      }} else {{
        node.nodeValue = originalTexts.get(node);
      }}
    }} else {{
      node.nodeValue = originalTexts.get(node);
    }}
  }}
}}

function changeLanguage(lang) {{
  currentAppLang = lang;
  localStorage.setItem('ges_lang', lang);
  document.getElementById('langToggle').value = lang;
  translatePage();
}}

changeLanguage(currentAppLang);
</script>

</body>
</html>
"""

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generated {OUTPUT} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
