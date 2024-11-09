let lat, lon;

function draw() {window.location.href = "roulette?lat=" + lat + "&lon=" + lon}

function iM() {
    navigator.geolocation.getCurrentPosition((position) => {
        lat = position.coords.latitude;
        lon = position.coords.longitude;

        const locPosition = new kakao.maps.LatLng(lat, lon);
        const mapContainer = document.getElementById("map");
        const mapOption = {center: locPosition};
        const map = new kakao.maps.Map(mapContainer, mapOption);
        const marker = new kakao.maps.Marker({position: locPosition, map: map});
        const circle = new kakao.maps.Circle({center: locPosition, 
            radius: 1500, 
            strokeWeight: 5, 
            strokeColor: "#B5D692", 
            strokeOpacity: 1, 
            strokeStyle: "solid", 
            fillColor: "#B5D692", 
            fillOpacity: 0.7});

        circle.setMap(map);

        dCL(locPosition);

        const ps = new kakao.maps.services.Places();
        sP();

        function sP() {
            const keyword = "주변맛집";
            ps.keywordSearch(keyword, pSCB, {location: locPosition})}

        function pSCB(data, status, pagination) {
            if (status === kakao.maps.services.Status.OK) {
                dPlaces(data);
                dPagination(pagination)} 
            else if (status === kakao.maps.services.Status.ZERO_RESULT) {alert("검색 결과가 존재하지 않습니다.")} 
            else if (status === kakao.maps.services.Status.ERROR) {alert("검색 중 오류가 발생했습니다.")}}

        function dPlaces(places) {
            const listEl = document.getElementById("placesList");
            const fragment = document.createDocumentFragment();
            const bounds = new kakao.maps.LatLngBounds();
            listEl.innerHTML = "";
            places.forEach((place, index) => {
                const placePosition = new kakao.maps.LatLng(place.y, place.x);
                const marker = aM(placePosition, index);
                const itemEl = gLI(index, place);
                bounds.extend(placePosition);

                (function (marker, place) {
                    kakao.maps.event.addListener(marker, "mouseover", function () {dI(marker, place.place_name);});
                    kakao.maps.event.addListener(marker, "mouseout", function () {infowindow.close()});

                    itemEl.onmouseover = function () {dI(marker, place.place_name)};
                    itemEl.onmouseout = function () {infowindow.close()}})(marker, place);

                fragment.appendChild(itemEl)});

            listEl.appendChild(fragment);
            map.setBounds(bounds);}

        function gLI(index, place) {
            const el = document.createElement("li");
            let itemStr = '<span class="markerbg marker_' + (index + 1) + '"></span>' + '<div class="info">' + "<h5>" + place.place_name + "</h5>";

            itemStr += '<span class="tel">' + place.phone + "</span>" + "</div>";
            el.innerHTML = itemStr;
            el.className = "item";

            return el}

        function aM(position, idx) {
            const imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png";
            const imageSize = new kakao.maps.Size(36, 37);
            const imgOptions = {spriteSize: new kakao.maps.Size(36, 691), spriteOrigin: new kakao.maps.Point(0, idx * 46 + 10), offset: new kakao.maps.Point(13, 37)};
            const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions);
            const marker = new kakao.maps.Marker({position: position, image: markerImage});

            marker.setMap(map);
            return marker}

        function dPagination(pagination) {
            const paginationEl = document.getElementById("pagination");
            const fragment = document.createDocumentFragment();

            while (paginationEl.hasChildNodes()) {paginationEl.removeChild(paginationEl.lastChild)}

            for (let i = 1; i <= pagination.last; i++) {
                const el = document.createElement("a");
                el.href = "#";
                el.innerHTML = i;

                if (i === pagination.current) {el.className = "on"} 
                else {el.onclick = ((i) => {return () => pagination.gotoPage(i)})(i)}
                fragment.appendChild(el)}
            paginationEl.appendChild(fragment)}})}

function dCL(locPosition) {document.getElementById("currentLocation").textContent = "현재위치 : " + lat + ", " + lon;}

const infowindow = new kakao.maps.InfoWindow({zIndex: 1});
window.onload = iM;