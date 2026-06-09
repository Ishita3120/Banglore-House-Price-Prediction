// #javascript is abasically a server communicator
function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i in uiBathrooms) {
        if (uiBathrooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    // var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    }, function (data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
}

// function onPageLoad() {
//     console.log("document loaded");
//     var url = "http://127.0.0.1:5000/get_locations_names"; // Use this if you are NOT using nginx which is first 7 tutorials
//     // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
//     $.get(url, function (data, status) {
//         console.log("got response for get_location_names request");
//         if (data) {
//             var locations = data.locations;
//             var uiLocations = document.getElementById("uiLocations");
//             $('#uiLocations').empty();
//             for (var i in locations) {
//                 var opt = new Option(locations[i]);
//                 $('#uiLocations').append(opt);
//             }
//         }
//     });
// }
function onPageLoad() {
    console.log("document loaded");

    var url = "/api/get_locations_names"

    $.get(url, function (data, status) {
        console.log("got response");
        console.log(data);

        if (data && data.locations) {
            var locations = data.locations;
            var uiLocations = $('#uiLocations');

            uiLocations.empty();

            uiLocations.append(
                '<option value="" disabled selected>Choose a Location</option>'
            );

            for (var i = 0; i < locations.length; i++) {
                var opt = new Option(locations[i], locations[i]);
                uiLocations.append(opt);
            }
        }
    });
}

window.onload = onPageLoad;

// ngniix->it is a real production/proxy reverse server
//flask server is maily used for development server
//flask ka port ususlly 5000 hota hai vhi ngnix ka 443 ya 80 port hota hai
//flow kuch aisa hota hai
//browser->ngnix(listens on port 443)->gunicorn browser->flask server(listens on port 5000)
// ngnix is a live web server used for production use deployment->it uses the reverse proxy setup to forward the request to flask server
