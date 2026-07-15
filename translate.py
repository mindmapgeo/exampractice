import json
import re
from deep_translator import GoogleTranslator

with open('study.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find GLOSSARY_DATA
match = re.search(r'const GLOSSARY_DATA = (\{.*?\});', content, re.DOTALL)
if not match:
    print("Could not find GLOSSARY_DATA")
    exit(1)

glossary_json = match.group(1)
try:
    glossary_data = json.loads(glossary_json)
except json.JSONDecodeError as e:
    # the JSON might have trailing commas or single quotes. Let's fix common JS issues if it's not valid JSON.
    print(f"JSON Decode Error: {e}")
    # since we saw the data in study.html, it used double quotes for keys and values. It might have trailing commas.
    glossary_json_fixed = re.sub(r',\s*([\]}])', r'\1', glossary_json)
    glossary_data = json.loads(glossary_json_fixed)

translator = GoogleTranslator(source='en', target='es')

# Translate
print("Translating...")
count = 0
for category, terms in glossary_data.items():
    for term in terms:
        if "spanish" not in term:
            english_text = term["english"]
            try:
                spanish_text = translator.translate(english_text)
                term["spanish"] = spanish_text
                count += 1
                if count % 50 == 0:
                    print(f"Translated {count} terms...")
            except Exception as e:
                print(f"Failed to translate {english_text}: {e}")
                term["spanish"] = english_text # fallback

print(f"Translation complete! {count} terms translated.")

new_glossary_json = json.dumps(glossary_data, ensure_ascii=False, indent=2)
# The JS expected `const GLOSSARY_DATA = { ... };`
new_content = content[:match.start()] + f"const GLOSSARY_DATA = {new_glossary_json};" + content[match.end():]

with open('study.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated study.html successfully!")
