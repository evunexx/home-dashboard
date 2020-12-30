function sunrisesunset() {
    var sunrise;
    var sunset;
    // get new data from server
    $.ajax({
        dataType: "json",
        type: 'GET',
        url: '/data/sunrise',
        success: function (data) {
            var result = data.results;
            sunrise = result['sunrise'];
            sunset = result['sunset'];
            // Create new Objects with dates from get-request
            var sunrise_date = new Date(sunrise);
            var sunset_date = new Date(sunset);
            console.log('info', sunrise_date);
            console.log('info', sunset_date);
            // Maybe format time here for winter and summer time
            var sunrise_hour_raw = sunrise_date.getHours();
            var sunrise_minutes_raw = sunrise_date.getMinutes();
            var sunrise = sunrise_hour_raw + ":" + sunrise_minutes_raw;
            $(".sunrise #timestamp").html(sunrise);

            var sunset_hour_raw = sunset_date.getHours();
            var sunset_minutes_raw = sunset_date.getMinutes();
            var sunset = sunset_hour_raw + ":" + sunset_minutes_raw;
            $(".sunset #timestamp").html(sunset);


        }
    });
}

function formatime(dateobject) {
    var offset = dateobject.getTimezoneOffset();
    console.log('success', offset);
}
$(document).ready(function () {
    sunrisesunset();
    setInterval(sunrisesunset, 500000);
})
