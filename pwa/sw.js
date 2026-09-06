// sw.js — Service Worker for the Digital Resilience Library PWA
// Serves from https://m1ck5k1.github.io/digital-resilience-library/
// Network-first with cache fallback for the entry/manifest; cache-first for library content (reference + templates).
const CACHE = 'drl-v1';
const SCOPE = '/digital-resilience-library/';

const PRECACHE = [
  SCOPE,
  SCOPE + 'index.html',          // repo-root landing (for the site root)
  SCOPE + 'pwa/',
  SCOPE + 'pwa/index.html',
  SCOPE + 'pwa/manifest.json',
  SCOPE + 'pwa/icon.svg',
  SCOPE + 'library/catalog.json',
];

self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRECACHE)));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
  );
});

self.addEventListener('fetch', e => {
  const url = e.request.url;
  // Only handle requests within our scope
  if (!url.startsWith(self.location.origin + SCOPE)) return;

  // Library content (.md) + the nav index: cache-first for fast offline access
  if (url.endsWith('.md') || url.endsWith('library.json') || url.endsWith('catalog.json')) {
    e.respondWith(
      caches.match(e.request).then(cached => cached || fetch(e.request).then(r => {
        const clone = r.clone();
        caches.open(CACHE).then(c => c.put(e.request, clone));
        return r;
      }))
    );
    return;
  }

  // Everything else: network-first
  e.respondWith(
    fetch(e.request).then(r => {
      const clone = r.clone();
      caches.open(CACHE).then(c => c.put(e.request, clone));
      return r;
    }).catch(() => caches.match(e.request))
  );
});