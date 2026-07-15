#!/usr/bin/env python3
import asyncio, edge_tts, os, tempfile, shutil
from build_glossary_audio_dual import GLOSSARY as GLOSSARY_EN, SECTIONS
from glossary_ukr import GLOSSARY as GLOSSARY_UK

VOICE_EN = "en-US-ChristopherNeural"
VOICE_UK = "uk-UA-OstapNeural"

async def generate_file(text, voice, filepath, sem, rate="+0%"):
    async with sem:
        if not os.path.exists(filepath):
            retries = 3
            for attempt in range(retries):
                try:
                    comm = edge_tts.Communicate(text, voice, rate=rate)
                    await comm.save(filepath)
                    break  # Success
                except Exception as e:
                    if attempt < retries - 1:
                        await asyncio.sleep(2 * (attempt + 1))
                    else:
                        print(f"Failed to generate {filepath} after {retries} attempts: {e}")
            
async def main():
    temp_dir = tempfile.mkdtemp()
    print(f"Working in temp dir: {temp_dir}")
    
    tasks = []
    sem = asyncio.Semaphore(5)  # Reduced concurrency to 5 to avoid connection reset
    file_list = []
    
    total = sum(len(terms) for _, terms in SECTIONS)
    
    intro_text = f"General Education System Ukrainian Interpreter Glossary. Comprehensive Dual-Language Audio Edition. {total} terms across 8 sections. Each entry is read in English, then natively in Ukrainian, followed by a brief description in English, and finally the description translated to Ukrainian."
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
            # English data
            uk_term_en_dict, en_desc = GLOSSARY_EN[key]
            
            # Ukrainian data
            if key in GLOSSARY_UK:
                uk_term, uk_desc = GLOSSARY_UK[key]
            else:
                uk_term, uk_desc = uk_term_en_dict, "Переклад опису відсутній"
            
            # 1. English Term
            p1 = os.path.join(temp_dir, f"{idx:05d}_en.mp3")
            tasks.append(generate_file(f"{key}.", VOICE_EN, p1, sem))
            file_list.append(p1)
            idx += 1
            
            # 2. Ukrainian Term
            p2 = os.path.join(temp_dir, f"{idx:05d}_uk.mp3")
            tasks.append(generate_file(f"{uk_term}.", VOICE_UK, p2, sem))
            file_list.append(p2)
            idx += 1
            
            # 3. English Description
            p3 = os.path.join(temp_dir, f"{idx:05d}_desc_en.mp3")
            tasks.append(generate_file(f"{en_desc}", VOICE_EN, p3, sem))
            file_list.append(p3)
            idx += 1

            # 4. Ukrainian Description
            p4 = os.path.join(temp_dir, f"{idx:05d}_desc_uk.mp3")
            tasks.append(generate_file(f"{uk_desc}", VOICE_UK, p4, sem))
            file_list.append(p4)
            idx += 1
            
    outro_path = os.path.join(temp_dir, f"{idx:05d}_outro.mp3")
    tasks.append(generate_file(f"End of glossary. {total} terms covered. Good luck on your exam.", VOICE_EN, outro_path, sem))
    file_list.append(outro_path)
    
    print(f"Queueing {len(tasks)} TTS requests. (this takes ~1-3 minutes)...")
    await asyncio.gather(*tasks)
    
    print("Concatenating files...")
    output = "glossary_audiobook_comprehensive.mp3"
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
