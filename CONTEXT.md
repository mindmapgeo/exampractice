# 🤖 Antigravity IDE Context

> **ATTENTION AI AGENTS:** Read this file before modifying the codebase. It explains the architecture, constraints, and current state of the General Education System Medical Interpreter Study System.

## 🎯 Project Purpose
This is a self-contained study application for a Ukrainian-English medical interpreter preparing for their certification exam at General Education System. It covers two main areas:
1. **12 Call-Handling Protocols:** Strict rules, scripts, and timelines for medical calls.
2. **Medical Vocabulary:** 469 terms across 8 categories (Anatomy, Medications, Insurance, etc.).

## 🏗 Architecture & Tech Stack
The entire study application is designed to be **hyper-portable** and hosted on GitHub Pages without any build steps or backend servers.

*   **Frontend:** Pure HTML5, CSS3, and Vanilla JavaScript. No frameworks (React/Vue) were used to keep it a single-file deployment.
*   **Data Storage:** All 469 vocabulary terms and 12 protocols are hardcoded as JSON objects directly inside the `<script>` tag in `study.html` (or `index.html`).
*   **State Management:** User progress (known/unknown flashcards, quiz scores) is saved to the browser's `localStorage`.
*   **Text-to-Speech (In-App):** Uses the browser's native `window.speechSynthesis` API for the flashcard preview audio.

## 📁 Critical Files
*   `study.html` (and its exact copy `index.html`): The main application. Contains all CSS, JS, and Data.
*   `_General Education System - Protocols 2025 UKR.pdf`: Source of truth for the 12 protocols.
*   `Interpreters Glossary.xlsx`: Source of truth for the 469 medical terms.
*   `README.md`: Human-readable study guide summarizing all the medical rules and vocabulary.

## 🎙 Audio Generation System (Python)
Because the user needs to study while commuting, we built a robust text-to-speech engine to generate a dual-language audiobook of the glossary.

*   **Stack:** Python 3 + `edge-tts` (Microsoft Azure neural voices, no API key needed).
*   **Core Script:** `build_final_audio.py`
    *   Generates a 4-part sequence for every term: `English Term` → `Ukrainian Term` → `English Description` → `Ukrainian Description`.
    *   Uses `en-US-ChristopherNeural` for English and `uk-UA-OstapNeural` for Ukrainian.
    *   Contains custom retry logic (`asyncio.Semaphore` and exponential backoff) to prevent Microsoft from dropping the connection, as it makes ~1,200 consecutive requests.
*   **Translations:** `glossary_ukr.py` contains the API-translated Ukrainian descriptions generated via `deep-translator`.
*   **Outputs:** The main output is `glossary_audiobook_comprehensive.mp3` (32MB).

## 🚀 Deployment Status
The project is initialized as a Git repository.
**Remote:** `https://github.com/mindmapgeo/exampractice.git`
**Branch:** `main`

## 🛠 Future AI Tasks
If you are modifying this project in the future, adhere to these constraints:
1.  **Do NOT add a build step** (Webpack, Vite, npm) unless explicitly requested. Keep `index.html` standalone.
2.  **Do NOT separate CSS/JS into different files.** The single-file portability is an intentional feature.
3.  If you add new vocabulary terms to the `index.html` array, you MUST also regenerate the audiobook by updating `build_glossary_audio_dual.py` and running `build_final_audio.py`.
