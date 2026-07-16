import json
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

files_to_parse = ['study.html', 'playscape.html']
strings = set()

for file_path in files_to_parse:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    for element in soup.find_all(string=True):
        parent = element.parent
        if parent.name in ['script', 'style', 'title']:
            continue
        text = element.strip()
        if len(text) > 2 and not text.isnumeric() and '{' not in text and '}' not in text:
            strings.add(text)
    for el in soup.find_all(attrs={"placeholder": True}):
        strings.add(el['placeholder'].strip())

import re
with open('playscape.html', 'r', encoding='utf-8') as f:
    ps_content = f.read()
for match in re.findall(r'"title":\s*"([^"]+)"', ps_content):
    strings.add(match)
for match in re.findall(r'"topic":\s*"([^"]+)"', ps_content):
    strings.add(match)

# Hardcoded JS strings in Playscape
strings.add("→ Next World")
strings.add("Reveal Next Line (Space)")
strings.add("Press Space to reveal next line")
strings.add("🎤 Speak your translation, then press Space to check")
strings.add("🔊 Speaking... <i>(Space to skip)</i>")


strings.discard('🔊')
strings.discard('🇪🇸')
strings.discard('🇺🇦')
strings.discard('🌍')
strings.discard('🏠')
strings.discard('📇')
strings.discard('📖')
strings.discard('⚡')
strings.discard('🎧')

print(f"Found {len(strings)} strings to translate.")

translator_uk = GoogleTranslator(source='en', target='uk')
translator_es = GoogleTranslator(source='en', target='es')

existing_dict = {}
try:
    with open('ui_dict.js', 'r', encoding='utf-8') as f:
        content = f.read().strip()
        match = re.search(r'const\s+UI_DICT\s*=\s*(\{.*\});?', content, re.DOTALL)
        if match:
            existing_dict = json.loads(match.group(1))
            print(f"Loaded {len(existing_dict)} existing translations from ui_dict.js")
except Exception as e:
    print(f"No existing dictionary found or failed to parse: {e}")

ui_dict = {}
new_translations = 0
for i, s in enumerate(strings):
    if s in existing_dict:
        ui_dict[s] = existing_dict[s]
        continue
    
    try:
        uk = translator_uk.translate(s)
        es = translator_es.translate(s)
        ui_dict[s] = {'uk': uk, 'es': es}
        new_translations += 1
        print(f"[{i+1}/{len(strings)}] Translated: {s[:20]}...")
    except Exception as e:
        print(f"Failed to translate {s}: {e}")

print(f"Completed. Translated {new_translations} new strings.")

with open('ui_dict.js', 'w', encoding='utf-8') as f:
    f.write("const UI_DICT = " + json.dumps(ui_dict, ensure_ascii=False, indent=2) + ";\n")
    
print("Saved to ui_dict.js")
