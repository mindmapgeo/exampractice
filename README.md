# General Education System Ukrainian Interpreter — Training Exam Study System

> **Quick context for any AI assistant:** This workspace contains a complete self-study system built for an employee preparing for their General Education System Ukrainian medical interpreter certification exam. The exam tests knowledge of (1) call-handling protocols and (2) English ↔ Ukrainian medical vocabulary. Everything needed to understand the content, extend the system, or answer questions about it is in this file.

---

## 📁 Files in This Folder

| File | Purpose |
|------|---------|
| `study.html` | Interactive study app — flashcards, quiz, protocols, glossary, cheat sheet, audiobook |
| `audiobook_script.txt` | Full narration-ready script (47 KB, 810 lines) for TTS conversion |
| `convert_to_audio.py` | Python script to convert the audiobook to MP3 using Microsoft Edge TTS (free, no API key) |
| `_General Education System - Protocols 2025 UKR.pdf` | **Source file 1** — 8-page PDF of all interpreter protocols |
| `Interpreters Glossary.xlsx` | **Source file 2** — Excel workbook with 8 sheets of English ↔ Ukrainian vocabulary |
| `README.md` | This file |

---

## 🧠 What the Exam Tests

The exam covers two areas:

### 1. Protocols (`_General Education System - Protocols 2025 UKR.pdf`)
Twelve specific call-handling protocols that interpreters must follow precisely. Each has mandatory scripts, step sequences, and timing rules.

### 2. Vocabulary (`Interpreters Glossary.xlsx`)
469 English ↔ Ukrainian medical terms across 8 categories.

---

## 📋 All 12 Protocols — Summary

### 1. Greeting Protocol *(Mandatory)*
Every call starts with a structured introduction to the **provider** (doctor/healthcare facility) AND to the **LEP** (Limited English Proficiency patient).

**Mandatory for provider:**
- Interpreter's name
- Language (Ukrainian)
- Interpreter's ID #
- "Everything will be interpreted"

**Script:** *"Hello, this is [name], your Ukrainian interpreter, ID XXXXX. Everything in the session will be interpreted. How can I help you?"*

**Mandatory for patient (Ukrainian):** *"Добрий день, мене звати ___, я ваш перекладач англійської мови. Усе під час цієї сесії буде перекладатися та залишатиметься конфіденційним."*

---

### 2. Closing Protocol *(Mandatory)*
Different for audio vs. video calls. Always ends with Ukrainian farewell to patient.

| Step | Audio Call | Video Call |
|------|-----------|------------|
| 1 | Offer additional assistance *(mandatory)* | Offer additional assistance *(mandatory)* |
| 2 | State Interpreter's ID # | Remind doctor to **rate the call** |
| 3 | Goodbye to doctor | Goodbye to doctor |
| 4 | Goodbye to LEP in Ukrainian | Goodbye to LEP in Ukrainian |

**Ukrainian farewell:** *"Гарного вам дня, пане / пані."*

---

### 3. Intervention — 3-Step Process
When needing to clarify, repeat, or verify during a session:

1. Identify yourself as interpreter → speak to the **waiting** party
2. Identify yourself to the **other** party → request clarification
3. Resume interpreting

**Script:** *"This is the interpreter speaking / Excuse me, the interpreter needs to clarify / a repetition / etc."*

---

### 4. 3rd Person Protocol
Normally interpret in **first person**. If parties speak to the interpreter instead of each other, intervene.

**Script to provider:** *"This is the interpreter, [provider], may I please ask you to speak directly to your patient so that we can ensure accuracy and avoid confusion?"*

**Script to patient (Ukrainian):** *"Пане / пані, я перекладач. Будь ласка, звертайтеся безпосередньо до лікаря, щоб уникнути двозначностей і забезпечити точність повідомлення."*

**If they continue speaking to you:** Continue in first person anyway. Note reason in Call Notes.

**Exceptions — 3rd person IS allowed:**
- Children ≤ 7 years old
- Emergencies (summarizing)
- Confused patients (dementia, substance abuse, post-surgery)
- Mentally ill patients
- Trauma triggered during call

---

### 5. "Say No" Model
For inappropriate requests (gifts, working hours, sight translation, etc.):

1. **Be gracious**
2. **Offer 2–3 alternatives**
3. **Give a reason**

---

### 6. Hold Protocol *(Timing Critical)*

| Situation | Hold Duration |
|-----------|--------------|
| Standard hold | **10 minutes** |
| Provider gives specific time | Honor that time |
| Provider gives unspecified time | **20 minutes** |
| Life or death situation | **Indefinitely** |
| Blue/black screen at call start | **60 seconds** |

**5-Step Hold Process:**
1. Inform provider of 10-min policy
2. Inform patient of the hold
3. Camera off + mute audio
4. Note in Call Notes
5. Report on Discord

**Script to provider:** *"This is the interpreter; I need to let you know that I have a 10-minute hold policy. I'll be here with my camera off until you come back."*

**Script to patient (Ukrainian):** *"Пане / пані, з вами говорить перекладач. Я вимкну свою камеру з міркувань безпеки до повернення лікаря. Я слухатиму все, що буде сказано (за потреби)."*

---

### 7. Troubleshooting Protocol
For poor audio/video quality:

1. Ask provider to reposition device OR toggle camera off/on
2. If unresolved: camera off, continue interpreting
3. If still unresolved: offer to connect another interpreter + give Tech Support: **1-866-449-4428**

---

### 8. Dial-Out Protocol
Before placing a call, collect these **5 pieces of information**:

1. What is the phone number to dial?
2. Who should I say is calling?
3. Name of the person/patient being called?
4. Leave a voicemail if no answer?
5. Is there a callback number?

---

### 9. Long Calls — Withdrawal Protocol *(Timing Critical)*

| Milestone | Action |
|-----------|--------|
| 90 minutes | Self-monitor; consider transferring |
| 120 minutes | Expected to transfer |

**Signs to transfer:** Increased fatigue, performance concerns, emotional distress, need for restroom/water.

**Key rules:**
- End of shift alone is **NOT** a valid reason to withdraw
- If not tired at 120 min, you may stay
- Always note in Call Notes and report to TL on Discord

---

### 10. Shadowing Between Languages
When provider speaks Ukrainian or patient speaks English, stay on the line in shadow mode.

**Rules:** Remain alert, take notes, be ready to jump in, ensure all parties know you're present, be transparent.

---

### 11. Direct Access Line (DAL)
Some hospitals give LEP patients a direct dial line. DAL calls appear as standard audio. Check the **Account** field in the Call Sheet for "Direct Access Line" or "DAL".

---

### 12. Dual Interpretation
Used when patient (typically a minor) uses ASL while parent speaks another language.

1. Whoever connects first adds the other language interpreter
2. Brief provider on hold; brief the team
3. **ASL interpreter takes the lead**

**Notes:** Identify yourself as "the Ukrainian interpreter" when clarifying. Always interpret each other's interpretation. Note in Call Notes + report on Discord.

---

### Call Notes (Universal Rule)
- Always leave a note, even if nothing eventful happened
- Names in CAPITAL LETTERS
- If patient refuses data: type initials if given; otherwise type **N/A** (capitals)
- Note refusals explicitly

---

## 🔑 Critical Numbers — Memorize These

```
60 seconds  →  Blue/black screen wait time
10 minutes  →  Standard hold
20 minutes  →  Unspecified flexible hold
∞           →  Life/death hold (indefinite)
90 minutes  →  Start considering transfer
120 minutes →  Expected to transfer

1-866-449-4428  →  Tech Support number
```

---

## 📖 Vocabulary — 8 Categories (469 Terms)

| Sheet | Category | Count |
|-------|----------|-------|
| VOCAB | General Medical Vocabulary | 75 |
| PROC ACRONYMS | Procedure & Medical Acronyms | 16 |
| MEDICATIONS | Medication terminology | 13 |
| ROUTINE VISITS | Routine medical visits | 29 |
| SPECIALTY CARE | Medical specialists | 39 |
| PAIN DESCRIPTORS | Pain description adjectives | 93 |
| ANATOMY | Body parts & systems | 96 |
| MED INSURANCE | Insurance terms (General/Medicaid/Medicare) | 108 |

The insurance sheet has 3 subsections: **General**, **Medicaid**, and **Medicare**.

---

## 🛠️ Technical Notes (For AI Assistants)

### Study App (`study.html`)
- **Pure HTML/CSS/JS** — single file, no dependencies, no server needed
- Opens directly in any browser via `open study.html` or double-click
- Progress saved to `localStorage` (persists across browser sessions)
- All 469 vocabulary terms are **embedded directly in the JS** as a `GLOSSARY_DATA` object
- Protocol quiz questions are in a `PROTOCOL_QUESTIONS` array (20 questions)
- Flashcard keyboard shortcuts: `Space`=flip, `→/←`=navigate, `G`=mark known, `X`=mark unknown
- Uses Google Fonts (Inter) and browser Speech Synthesis API for TTS preview

### Audiobook Script (`audiobook_script.txt`)
- 47,390 bytes, 810 lines, 469 vocabulary terms
- Structure: Part 1 (Protocols) → Part 2 (Critical Facts Drill) → Part 3 (Vocab Drill)
- Designed for TTS at ~0.85x speed
- Ukrainian phrases included in script for bilingual TTS tools

### TTS Converter (`convert_to_audio.py`)
- Uses `edge-tts` (Microsoft Azure neural voices, **completely free**, no API key)
- Voice: `en-US-ChristopherNeural` (authoritative, clear)
- Splits the long script into chunks for processing
- Output: `audiobook_output.mp3` in this folder
- Install dependency: `pip3 install edge-tts`
- Run: `python3 convert_to_audio.py`

### Data Extraction
The source files were parsed with:
- `PyMuPDF` (fitz) for PDF text extraction
- `openpyxl` for Excel sheet parsing

---

## 🚀 How to Use the Study System

### For studying protocols:
1. Open `study.html` → click **Protocols** tab
2. Expand each protocol card
3. Study the scripts, steps, and timing rules

### For vocabulary flashcards:
1. Open `study.html` → click **Flashcards** tab
2. Select a category or use "All"
3. Flip cards, mark known/unknown — progress saves automatically

### For self-testing:
1. Open `study.html` → click **Quiz** tab
2. Select category + question count → Start
3. Aim for 90%+ before the real exam

### For audio study:
1. Run `python3 convert_to_audio.py` to generate `audiobook_output.mp3`
2. Transfer to phone and listen while commuting/exercising
3. OR open `study.html` → **Audiobook** tab → click "Play in Browser"

### Recommended study sequence:
1. Read through each protocol in the Protocols tab (day 1)
2. Do flashcard sessions by category — 1–2 categories per day
3. Run the quiz daily, targeting weak areas
4. Listen to the audiobook during commute/exercise
5. Final day: Cheat Sheet review + full quiz (all categories, 50 questions)

---

*Last generated: 2026-07-15 | Source: General Education System Protocols 2025 UKR.pdf + Interpreters Glossary.xlsx*
