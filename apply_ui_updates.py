import re

with open('study.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Header HTML to include Search and Lang Toggle
header_pattern = r'(<header>.*?)(<div class="header-stats">.*?</header>)'
header_replacement = r'''\1
  <div class="header-search">
    <input type="text" id="globalSearch" placeholder="🔍 Search glossary & protocols..." onkeyup="handleSearch(event)">
  </div>
  <div class="header-right">
    <select id="langToggle" onchange="changeLanguage(this.value)">
      <option value="ukrainian">🇺🇦 Ukrainian</option>
      <option value="spanish">🇪🇸 Spanish</option>
    </select>
    \2'''
content = re.sub(header_pattern, header_replacement, content, flags=re.DOTALL)
content = content.replace('<div class="header-stats">', '<div class="header-stats" style="display:flex;gap:12px;">')
content = content.replace('header {', 'header { display: flex; align-items: center; justify-content: space-between;')
# Add some CSS for the new elements
css_append = '''
  .header-right { display: flex; align-items: center; gap: 16px; }
  .header-search input { padding: 8px 12px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.2); background: rgba(0,0,0,0.2); color: white; width: 300px; outline: none; }
  .header-search input::placeholder { color: rgba(255,255,255,0.6); }
  #langToggle { padding: 6px 10px; border-radius: 8px; background: rgba(255,255,255,0.1); color: white; border: 1px solid rgba(255,255,255,0.3); font-weight: bold; cursor: pointer; }
  #langToggle option { color: black; }
  #searchResults { display: none; padding: 20px; background: var(--bg2); border-radius: 12px; margin-top: 20px; }
  .search-highlight { background: rgba(255,215,0,0.3); font-weight: bold; }
'''
content = content.replace('</style>', css_append + '\n</style>')

# 2. Inject Javascript for Language and Search
js_append = '''
// MULTI-LANGUAGE & SEARCH SYSTEM
let currentAppLang = localStorage.getItem('ges_lang') || 'ukrainian';
document.getElementById('langToggle').value = currentAppLang;

function changeLanguage(lang) {
  currentAppLang = lang;
  localStorage.setItem('ges_lang', lang);
  
  // Update Protocols UI
  document.querySelectorAll('.script-box.ukraine, .script-box.spanish').forEach(el => {
    el.style.display = 'none';
  });
  document.querySelectorAll(`.script-box.${lang === 'ukrainian' ? 'ukraine' : 'spanish'}`).forEach(el => {
    el.style.display = 'block';
  });

  // Re-render active tab content
  loadFlashcard();
  renderGlossary();
  buildQuiz();
}

// Initial setup of protocols
changeLanguage(currentAppLang);

function handleSearch(e) {
  const q = e.target.value.toLowerCase().trim();
  const resContainer = document.getElementById('searchResults') || createSearchContainer();
  
  if (q.length < 2) {
    resContainer.style.display = 'none';
    document.querySelectorAll('.tab-content').forEach(el => {
      if(el.id === 'content-' + document.querySelector('.nav-btn.active').id.split('-')[1]) el.style.display = 'block';
    });
    return;
  }
  
  // Hide all tabs
  document.querySelectorAll('.tab-content').forEach(el => el.style.display = 'none');
  resContainer.style.display = 'block';
  
  let html = `<h3>🔍 Search Results for "${q}"</h3><div class="glossary-list">`;
  
  // Search Glossary
  let found = 0;
  for (const [cat, terms] of Object.entries(GLOSSARY_DATA)) {
    for (const item of terms) {
      if (item.english.toLowerCase().includes(q) || 
          item.ukrainian.toLowerCase().includes(q) || 
          (item.spanish && item.spanish.toLowerCase().includes(q))) {
        html += `
          <div class="glos-item">
            <div class="glos-en">${item.english.replace(new RegExp(q, 'gi'), match => `<span class="search-highlight">${match}</span>`)}</div>
            <div class="glos-uk">${item[currentAppLang].replace(new RegExp(q, 'gi'), match => `<span class="search-highlight">${match}</span>`)}</div>
          </div>`;
        found++;
      }
    }
  }
  
  if (found === 0) html += `<p>No matches found in glossary.</p>`;
  html += `</div>`;
  resContainer.innerHTML = html;
}

function createSearchContainer() {
  const main = document.querySelector('main');
  const div = document.createElement('div');
  div.id = 'searchResults';
  main.prepend(div);
  return div;
}

// Overrides for existing functions to use currentAppLang
'''
content = content.replace('// INIT', js_append + '\n\n// INIT')

# 3. Replace card.ukrainian with card[currentAppLang]
content = content.replace('card.ukrainian', 'card[currentAppLang]')
content = content.replace('q.ukrainian', 'q[currentAppLang]')
content = content.replace('isEnToUk ? \'UKRAINIAN\' : \'ENGLISH\'', 'isEnToUk ? currentAppLang.toUpperCase() : \'ENGLISH\'')
content = content.replace('item.ukrainian', 'item[currentAppLang]')
content = content.replace('term.ukrainian', 'term[currentAppLang]')
content = content.replace('isEnToUk ? t.ukrainian : t.english', 'isEnToUk ? t[currentAppLang] : t.english')

with open('study.html', 'w', encoding='utf-8') as f:
    f.write(content)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied UI updates for language toggle and search.")
