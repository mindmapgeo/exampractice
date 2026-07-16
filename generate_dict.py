import json
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

with open('study.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

strings = set()
for element in soup.find_all(string=True):
    parent = element.parent
    if parent.name in ['script', 'style', 'title']:
        continue
    
    text = element.strip()
    if len(text) > 2 and not text.isnumeric() and '{' not in text and '}' not in text:
        strings.add(text)

# Also placeholders
for el in soup.find_all(attrs={"placeholder": True}):
    strings.add(el['placeholder'].strip())

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

ui_dict = {}
for i, s in enumerate(strings):
    try:
        uk = translator_uk.translate(s)
        es = translator_es.translate(s)
        ui_dict[s] = {'uk': uk, 'es': es}
        print(f"[{i+1}/{len(strings)}] Translated: {s[:20]}...")
    except Exception as e:
        print(f"Failed to translate {s}: {e}")

with open('ui_dict.js', 'w', encoding='utf-8') as f:
    f.write("const UI_DICT = " + json.dumps(ui_dict, ensure_ascii=False, indent=2) + ";\n")
    
print("Saved to ui_dict.js")
