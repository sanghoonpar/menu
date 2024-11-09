var CACHE_NAME = "pwa-manager";
var urlsToCache = ["/templates/home.html", "/css/home.css"];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(function(cache) {
            console.log("Opened cache");
            return cache.addAll(urlsToCache)}))});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if (response) {return response}
            return fetch(event.request)}))});

self.addEventListener("activate", event => {
    var cacheWhitelist = ["pwa-manager"];
    event.waitUntil(caches.keys().then(cacheNames => {return Promise.all(cacheNames.map(cacheName => {if (cacheWhitelist.indexOf(cacheName) === -1) {return caches.delete(cacheName)}}))}))});

let deferredPrompt = null;

window.addEventListener("beforeinstallprompt", function(event) {
    event.preventDefault();
    deferredPrompt = event});

$(document).ready(function() {
    $("#a2hs_btn").on("click", function(e) {
        e.preventDefault();
        if (deferredPrompt) {
            deferredPrompt.prompt();
            deferredPrompt.userChoice.then(function(choiceResult) {if (choiceResult.outcome === "accepted") {deferredPrompt = null}})} 
        else {alert("홈 화면에 추가할 수 없습니다.")}})});