function sunrisesunset() {
    var sunrise;
    var sunset;
    // get new data from server
    $.ajax({
        dataType: "json",
        type: 'GET',
        url: '/data/sunrise',
        success: function (data) {
            console.log('success', data);
            var result = data.results;
            console.log('success', result);
            sunrise = result['sunrise'];
            console.log('success', sunrise);
            sunset = result['sunset'];
             // Create new Objects with dates from get-request
            var sunrise_date = new Date(sunrise);
            var sunset_date = new Date (sunset);

            // Have to format hours for timezone
            var sunrise_hour_raw = sunrise_date.getHours();

            if (sunrise_hour_raw < 10) {


            }


            var sunrise_minutes = sunrise_date.getMinutes();

            console.log('succes', typeof(sunrise_hour));
            console.log('success', 'test123'+sunrise_hour);

            $("#sunrise").html(sunrise_hour);
        }
    });
}

$(document).ready(function() {
    sunrisesunset();
    setInterval(sunrisesunset, 500000);
  })
