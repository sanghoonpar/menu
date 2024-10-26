var CACHE_NAME = 'pwa-manager';
var urlsToCache = [
    '/static/css/home.css',    // CSS 파일은 static 폴더 안에 위치
    '/'                    // Flask에서 템플릿을 렌더링하는 URL 경로
];

// 서비스 워커 설치
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(function(cache) {
            console.log('Opened cache');
            return cache.addAll(urlsToCache);
        })
    );
});

// 요청 캐싱 및 응답
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if (response) {
                return response;
            }
            return fetch(event.request);
        })
    );
});

// 서비스 워커 업데이트
self.addEventListener('activate', event => {
    var cacheWhitelist = ['pwa-manager'];
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});