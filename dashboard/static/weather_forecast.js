function weather_forecast() {

    //const iconElement = $("#date");
    //const tempElement = $("#date");
    //const descElement = $("#date");

    $.ajax({
        dataType: "json",
        type: 'GET',
        url: '/data/weather/forecast',
        success: function (data) {
            var iconcode = data[0].icon;
            console.log('success', iconcode);
            $.each(data, function (index, value) {

                var sindex = String(index);
                var dayname = value.dayname;
                var icon = value.icon;
                var maxtemp = value.maxtemp;
                var mintemp = value.mintemp;
                var desc = value.weather;

                $(".forecast-" + sindex + " #day").html(dayname);
                $(".forecast-" + sindex + " #min-temperature-value-forecast").html("Min: " + mintemp + " C°");
                $(".forecast-" + sindex + " #max-temperature-value-forecast").html("Max: " + maxtemp + " C°");
                $(".forecast-" + sindex + " #temperature-description-forecast").html(desc);

                var iconurl = "/static/svg-icons/" + icon + ".svg";
                $(".forecast-" + sindex + " #wicon-forecast").attr('src', iconurl);
            });
        }
    });

}

$(document).ready(function () {
    weather_forecast();
    setInterval(weather_forecast, 5000);
})