#!/usr/bin/env python3
"""
General Education System Audiobook TTS Converter
============================
Converts audiobook_script.txt → audiobook_output.mp3
Uses Microsoft Edge TTS (free, no API key required).

Install dependency:
    pip3 install edge-tts

Run:
    python3 convert_to_audio.py

Output:
    audiobook_output.mp3  (in this folder)
    audiobook_output_vocab_only.mp3  (vocabulary drill only, shorter)
"""

import asyncio
import os
import sys
import time

# ── Check dependency ──────────────────────────────────────────────────────────
try:
    import edge_tts
except ImportError:
    print("❌ edge-tts not found. Installing now...")
    os.system(f"{sys.executable} -m pip install edge-tts --quiet")
    import edge_tts

# ── Configuration ─────────────────────────────────────────────────────────────

SCRIPT_FILE   = "audiobook_script.txt"
OUTPUT_FULL   = "audiobook_output.mp3"
OUTPUT_DRILL  = "audiobook_output_critica_drill_only.mp3"
OUTPUT_VOCAB  = "audiobook_output_vocab_only.mp3"
OUTPUT_PROTOCOLS = "audiobook_output_protocols_only.mp3"

# Voice options (all free, Microsoft Azure neural):
#   en-US-ChristopherNeural  - Male, News/Novel, authoritative (RECOMMENDED for study)
#   en-US-GuyNeural          - Male, News/Novel, passionate
#   en-US-AriaNeural         - Female, News/Novel, confident
#   en-US-JennyNeural        - Female, General, friendly
#   en-US-EricNeural         - Male, News/Novel, rational
VOICE = "en-US-ChristopherNeural"
RATE  = "-10%"   # Slightly slower than default for clarity (-20% = very slow, +0% = normal)
PITCH = "+0Hz"

# ── Helpers ───────────────────────────────────────────────────────────────────

def load_script(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def clean_for_tts(text: str) -> str:
    """Remove decorative characters that TTS would read aloud awkwardly."""
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        # Skip box-drawing lines (═══, ───, ╔══, etc.)
        stripped = line.strip()
        if all(c in "═─╔╗╚╝║╠╣╦╩╬▼" for c in stripped) and len(stripped) > 2:
            continue
        # Replace decorative chars with pause-friendly equivalents
        line = line.replace("...", ",")
        line = line.replace("•", ".")
        line = line.replace("✓", "")
        line = line.replace("📋", "")
        line = line.replace("🎧", "")
        line = line.replace("═", "")
        line = line.replace("─", "")
        cleaned.append(line)
    return "\n".join(cleaned)


def extract_section(text: str, start_marker: str, end_marker: str = None) -> str:
    """Extract text between two markers."""
    start = text.find(start_marker)
    if start == -1:
        return text
    if end_marker:
        end = text.find(end_marker, start)
        return text[start:end] if end != -1 else text[start:]
    return text[start:]


async def synthesize(text: str, output_file: str, voice: str = VOICE):
    """Convert text to speech and save as MP3."""
    communicate = edge_tts.Communicate(text, voice, rate=RATE, pitch=PITCH)
    await communicate.save(output_file)


async def main():
    print("=" * 60)
    print("  General Education System Audiobook TTS Converter")
    print("  Voice:", VOICE)
    print("  Rate:", RATE)
    print("=" * 60)

    # ── Load and clean script ─────────────────────────────────────────────────
    if not os.path.exists(SCRIPT_FILE):
        print(f"❌ Error: '{SCRIPT_FILE}' not found. Make sure you're running from the exam folder.")
        sys.exit(1)

    raw = load_script(SCRIPT_FILE)
    full_text = clean_for_tts(raw)
    total_chars = len(full_text)
    print(f"\n📄 Script loaded: {total_chars:,} characters\n")

    # ── Menu ──────────────────────────────────────────────────────────────────
    print("Which audio file(s) would you like to generate?")
    print()
    print("  [1] Full audiobook (protocols + drill + vocab) — ~60-80 min")
    print("  [2] Protocols only (Chapters 1-12)             — ~20-25 min")
    print("  [3] Critical facts drill only                  — ~8-10 min  ← great for daily review")
    print("  [4] Vocabulary drill only (all 469 terms)      — ~35-40 min")
    print("  [5] All of the above (generates 4 files)")
    print()

    choice = input("Enter choice [1-5]: ").strip()
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Defaulting to [1] Full audiobook.")
        choice = "1"

    tasks = []
    if choice in ["1", "5"]:
        tasks.append(("Full Audiobook", full_text, OUTPUT_FULL))
    if choice in ["2", "5"]:
        protocols_text = extract_section(full_text, "PART 1: PROTOCOLS", "PART 2: CRITICAL FACTS")
        tasks.append(("Protocols Only", protocols_text, OUTPUT_PROTOCOLS))
    if choice in ["3", "5"]:
        drill_text = extract_section(full_text, "PART 2: CRITICAL FACTS", "PART 3: COMPLETE VOCABULARY")
        tasks.append(("Critical Facts Drill", drill_text, OUTPUT_DRILL))
    if choice in ["4", "5"]:
        vocab_text = extract_section(full_text, "PART 3: COMPLETE VOCABULARY")
        tasks.append(("Vocabulary Drill", vocab_text, OUTPUT_VOCAB))

    # ── Generate ──────────────────────────────────────────────────────────────
    for label, text, output in tasks:
        print(f"\n🎙️  Generating: {label}")
        print(f"   Output file: {output}")
        print(f"   Characters:  {len(text):,}")
        print("   Converting... ", end="", flush=True)

        t0 = time.time()
        try:
            await synthesize(text, output)
            elapsed = time.time() - t0
            size_mb = os.path.getsize(output) / 1024 / 1024
            print(f"✅ Done in {elapsed:.1f}s — {size_mb:.1f} MB")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("   Tip: Check your internet connection (edge-tts requires internet access).")

    # ── Done ──────────────────────────────────────────────────────────────────
    print()
    print("=" * 60)
    print("  ✅ Audio generation complete!")
    print()
    print("  Files saved in this folder:")
    for _, _, output in tasks:
        if os.path.exists(output):
            size_mb = os.path.getsize(output) / 1024 / 1024
            print(f"    📼 {output}  ({size_mb:.1f} MB)")
    print()
    print("  Transfer to your phone and listen anywhere.")
    print("  Recommended: Apple Podcasts, VLC, or any audio player.")
    print("=" * 60)

    # Auto-open first output file on macOS
    if tasks and os.path.exists(tasks[0][2]):
        open_q = input(f"\n▶ Open '{tasks[0][2]}' now? [y/N]: ").strip().lower()
        if open_q == "y":
            os.system(f"open '{tasks[0][2]}'")


if __name__ == "__main__":
    asyncio.run(main())
