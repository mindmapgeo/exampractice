#!/usr/bin/env python3
import asyncio, edge_tts, os, tempfile, shutil
from build_glossary_audio_dual import GLOSSARY as GLOSSARY_EN, SECTIONS
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='es')

VOICE_EN = "en-US-ChristopherNeural"
VOICE_ES = "es-ES-AlvaroNeural"

async def generate_file(text, voice, filepath, sem, rate="+0%"):
    async with sem:
        if not os.path.exists(filepath):
            retries = 3
            for attempt in range(retries):
                try:
                    comm = edge_tts.Communicate(text, voice, rate=rate)
                    await comm.save(filepath)
                    break
                except Exception as e:
                    if attempt < retries - 1:
                        await asyncio.sleep(2 * (attempt + 1))
                    else:
                        print(f"Failed to generate {filepath} after {retries} attempts: {e}")
            
async def main():
    temp_dir = tempfile.mkdtemp()
    print(f"Working in temp dir: {temp_dir}")
    
    tasks = []
    sem = asyncio.Semaphore(5)
    file_list = []
    
    total = sum(len(terms) for _, terms in SECTIONS)
    
    intro_text = f"General Education System Spanish Interpreter Glossary. Comprehensive Dual-Language Audio Edition. {total} terms across 8 sections. Each entry is read in English, then natively in Spanish, followed by a brief description in English, and finally the description translated to Spanish."
    intro_path = os.path.join(temp_dir, "00000_intro.mp3")
    tasks.append(generate_file(intro_text, VOICE_EN, intro_path, sem))
    file_list.append(intro_path)
    
    idx = 1
    for section_name, term_keys in SECTIONS:
        present = [k for k in term_keys if k in GLOSSARY_EN]
        if not present:
            continue
            
        sec_path = os.path.join(temp_dir, f"{idx:05d}_sec.mp3")
        tasks.append(generate_file(f"Section: {section_name}. {len(present)} terms.", VOICE_EN, sec_path, sem))
        file_list.append(sec_path)
        idx += 1
        
        for key in present:
            uk_term_en_dict, en_desc = GLOSSARY_EN[key]
            
            # Translate term and desc to Spanish synchronously (cached if run multiple times)
            try:
                es_term = translator.translate(key)
                es_desc = translator.translate(en_desc)
            except:
                es_term = key
                es_desc = en_desc
            
            p1 = os.path.join(temp_dir, f"{idx:05d}_en.mp3")
            tasks.append(generate_file(f"{key}.", VOICE_EN, p1, sem))
            file_list.append(p1)
            idx += 1
            
            p2 = os.path.join(temp_dir, f"{idx:05d}_es.mp3")
            tasks.append(generate_file(f"{es_term}.", VOICE_ES, p2, sem))
            file_list.append(p2)
            idx += 1
            
            p3 = os.path.join(temp_dir, f"{idx:05d}_desc_en.mp3")
            tasks.append(generate_file(f"{en_desc}", VOICE_EN, p3, sem))
            file_list.append(p3)
            idx += 1

            p4 = os.path.join(temp_dir, f"{idx:05d}_desc_es.mp3")
            tasks.append(generate_file(f"{es_desc}", VOICE_ES, p4, sem))
            file_list.append(p4)
            idx += 1
            
    outro_path = os.path.join(temp_dir, f"{idx:05d}_outro.mp3")
    tasks.append(generate_file(f"End of glossary. {total} terms covered. Good luck on your exam.", VOICE_EN, outro_path, sem))
    file_list.append(outro_path)
    
    print(f"Queueing {len(tasks)} TTS requests. (this takes ~2-4 minutes)...")
    await asyncio.gather(*tasks)
    
    print("Concatenating files...")
    output = "glossary_audiobook_comprehensive_spanish.mp3"
    with open(output, "wb") as outfile:
        for f in file_list:
            if os.path.exists(f):
                with open(f, "rb") as infile:
                    outfile.write(infile.read())
                    
    shutil.rmtree(temp_dir)
    mb = os.path.getsize(output) / 1024 / 1024
    print(f"✅ Done! {output} — {mb:.1f} MB")
    
if __name__ == "__main__":
    asyncio.run(main())
