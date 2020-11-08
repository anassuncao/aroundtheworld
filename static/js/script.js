
function initMap() {
            var doha = {lat: 25.204849, lng: 55.270782}
            var map = new google.maps.Map(document.getElementById("map"), {
                zoom: 2,
                center: doha
            });
            
            var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

            var markers = locations.map((location, i) => {
                return new google.maps.Marker({
                position: location,
                label: labels[i % labels.length],
                });
            });

            new MarkerClusterer(map, markers, {
                imagePath:
                "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m",
            });

        }

        var locations = [
                {lat: 25.204849, lng: 55.270782},
                {lat: -37.813629, lng: 144.963058},
                {lat: 25.285446, lng: 51.531040},
                {lat: 40.712776, lng: -74.005974},
                {lat: 21.306944, lng: -157.858337},
                {lat: 38.7436214, lng: -9.1952226},
                {lat: 51.573684, lng: 5.0036701},
                {lat: 29.4816561, lng: -98.6544881},
                {lat: -27.3812533, lng: 152.7130155}
            ];