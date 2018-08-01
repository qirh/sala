const version = "1.0";
const cacheName = 'saleh-${version}';
self.addEventListener('install', e => {
  const timeStamp = Date.now();
  e.waitUntil(
    caches.open(cacheName).then(cache => {
      return cache.addAll([
        '/templates/dropdown.html?timestamp=${timeStamp}',
        '/templates/en/skeleton.html?timestamp=${timeStamp}',
          '/templates/en/index.html?timestamp=${timeStamp}',
          '/static/icons/github.svg',
          '/static/icons/website.svg',
          '/static/photos/bike.jpg',
          '/static/photos/bike2.jpg',
          '/static/photos/moi-moustache.jpg',
          '/static/photos/moi-sans-moustache.jpg',
          '/static/photos/tech.jpg',
          '/static/photos/travel.jpg'
      ])
          .then(() => self.skipWaiting());
    })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(cacheName)
      .then(cache => cache.match(event.request, {ignoreSearch: true}))
      .then(response => {
      return response || fetch(event.request);
    })
  );
});
