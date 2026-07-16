# Project Rules and Lessons Learned

These guidelines are set up for any future AI agent or assistant working on this repository.

## 📁 Repository Health & Best Practices

1. **Never Check in Local Path Assumptions:**
   - When generating or writing files, do not use hardcoded absolute system paths (e.g. `/Users/rootv/...`). Always resolve directories relative to the executing script:
     ```python
     import os
     script_dir = os.path.dirname(os.path.abspath(__file__))
     output_path = os.path.join(script_dir, "filename")
     ```

2. **Git Tracking Hygiene:**
   - Keep a strict `.gitignore` file to ensure the following are not committed:
     - Virtual environments (`.venv/`)
     - Python compiler caches (`__pycache__/`, `*.pyc`)
     - Temporary audio test outputs (`1.mp3`, `2.mp3`, etc.)
     - Local system metadata (`.DS_Store`)

3. **Code Duplication Prevention:**
   - `index.html` and `study.html` must remain identical and synced. When updating one, synchronize the other.

4. **Multi-Language UI Consistency:**
   - The app has a custom dynamic UI translation system. It loads `ui_dict.js` containing `UI_DICT` and translates the DOM using a tree walker in the `translatePage()` helper function when the active language changes. Ensure any newly added UI text elements are present in `ui_dict.js` or translated correctly.
