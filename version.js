// Single source of truth for the visible version badge shown on every page.
// Bump this on any content/feature edit so it's obvious which rendition is live.
const SITE_VERSION = { number: 'v1', date: '2026-07-16' };

(function () {
  function addBadge() {
    const badge = document.createElement('div');
    badge.id = 'siteVersionBadge';
    badge.textContent = `${SITE_VERSION.number} · ${SITE_VERSION.date}`;
    badge.style.cssText = [
      'position:fixed', 'bottom:8px', 'left:8px', 'z-index:9999',
      'background:rgba(0,0,0,0.55)', 'color:#94a3b8',
      'font:11px/1.4 -apple-system,BlinkMacSystemFont,sans-serif',
      'padding:4px 9px', 'border-radius:6px', 'pointer-events:none',
      'letter-spacing:0.02em', 'backdrop-filter:blur(4px)'
    ].join(';');
    document.body.appendChild(badge);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addBadge);
  } else {
    addBadge();
  }
})();
