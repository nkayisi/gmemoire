// // set map options
// const mylatLng = {lat:38.3460, lng: -0.4907};
// const mapOptions = {
//     center: mylatLng,
//     zoom: 8,
//     mapTypeId: google.maps.MapTypeId.ROADMAP
// };


// // create Map
// let map = new google.maps.Map(document.getElementById("googleMap"), mapOptions)


// // create a direction service object to use the route method and get
// let directionsService = new google.maps.DirectionsService();

// // create a directionsRenderer object which we will use to display the route
// let directionsDisplay = new google.maps.DirectionsRenderer();


// // bind the directionsRenderer to the map
// directionsDisplay.setMap(map);


// // function
// function calRoute() {
//     let request = {
//         origin: document.getElementById("from").value,
//         destination: document.getElementById('to').value,
//         travelMode: google.maps.TravelMode.DRIVING, //WALKING
//         unitSystem: google.maps.UnitSystem.IMPERIAL
//     }

//     // pass the request to the route method
//     directionsService.route(request, (result, status)=>{
//         if (status == new google.maps.DirectionsStatus.OK){
//             // get distance and time
//             const output = document.querySelector('#output');
//             output.innerHTML = `<div class="alert-info">From: ${document.getElementById('#from').value} 
//                                 <br> To: ${document.getElementById('#to').value}. 
//                                 <br> Driving distance} ${result.routes[0].legs[0].distance.text} 
//                                 <br> duration ${result.routes[0].legs[0].duration.text}.</div>`

//             // display route
//             directionsDisplay.setDirections(result);
//         }else {
//             // delete route from map
//             directionsDisplay.setDirections({routes: []});

//             // center map in span
//             map.setCenter(mylatLng);

//             // show error message
//             output.innerHTML = `<div class="alert-danger">Could not retrieve driving distance.</div>`
//         }
//     });
// }


// // create autoComplite objects for all input
// let options ={
//     types: ['(cities)']
// }

// let input1 = document.getElementById("#from");
// let autocomplete1 = new google.maps.places.Autocomplete(input1, options);


// let input2 = document.getElementById("#to");
// let autocomplete2 = new google.maps.places.Autocomplete(input2, options);



let directionsService = new google.maps.DirectionsService();


var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
  };
  
function success(pos) {
    var crd = pos.coords;

    console.log('Votre position actuelle est :');
    console.log(`Latitude : ${crd.latitude}`);
    console.log(`Longitude : ${crd.longitude}`);
    console.log(`La précision est de ${crd.accuracy} mètres.`);


    let request = {
        origin: pos,
        destination: {lat:38.3460, lng: -0.4907},
        travelMode: google.maps.TravelMode.DRIVING, //WALKING
        unitSystem: google.maps.UnitSystem.IMPERIAL
    }


    //  pass the request to the route method
    directionsService.route(request, (result, status)=>{
        if (status == new google.maps.DirectionsStatus.OK){

            // display route
            directionsDisplay.setDirections(result);
            console(result);
        }else {
            // delete route from map
            directionsDisplay.setDirections({routes: []});

            // center map in span
            // map.setCenter(mylatLng);

        }
    });


}
  
function error(err) {
    console.warn(`ERREUR (${err.code}): ${err.message}`);
}



navigator.geolocation.getCurrentPosition(success, error, options)
