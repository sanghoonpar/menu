var CACHE_NAME = 'pwa-manager';
var urlsToCache = ['/templates/home.html', '/css/home.css']; // 절대 경로로 수정

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
            // 캐시 히트 - 응답 반환
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

// 홈 화면 추가 프로세스
let deferredPrompt = null;

window.addEventListener('beforeinstallprompt', function(event) {
    event.preventDefault();
    deferredPrompt = event;
});

// 버튼 클릭 이벤트 처리
$(document).ready(function() {
    $("#a2hs_btn").on("click", function(e) {
        e.preventDefault();
        if (deferredPrompt) {
            deferredPrompt.prompt();
            deferredPrompt.userChoice.then(function(choiceResult) {
                if (choiceResult.outcome === 'accepted') {
                    deferredPrompt = null;
                }
            });
        } else {
            alert("홈 화면에 추가할 수 없습니다.");
        }
    });
});