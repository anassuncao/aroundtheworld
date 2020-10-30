
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
                {lat: 21.306944, lng: -157.858337}
            ];

            

/*Turning cities into coordenates and add them to the var locations*/
/*
var geocoder;
var map;
function initialize() {
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(-34.397, 150.644);
    var mapOptions = {
      zoom: 8,
      center: latlng
    }
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
  }

  function codeAddress() {
    var address = document.getElementById('city_name').value;
    geocoder.geocode( { 'city_name': address}, function(results, status) {
      if (status == 'OK') {
        locations.push(address);
        });
      } else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });
  }

/* 
  for (i = 0; i < myJSONResult.results.length; i++) {
  myAddress[i] = myJSONResult.results[i].location;
}

  locations.push(location);

<body onload="initialize()">
 <div id="map" style="width: 320px; height: 480px;"></div>
  <div>
    <input id="address" type="textbox" value="Sydney, NSW">
    <input type="button" value="Encode" onclick="codeAddress()">
  </div>
</body>*/