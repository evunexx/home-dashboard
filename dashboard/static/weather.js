function weather() {

    //const iconElement = $("#date");
    //const tempElement = $("#date");
    //const descElement = $("#date");

    $.ajax({
        dataType: "json",
        type: 'GET',
        url: '/data/weather/current',
        success: function (data) {
            var iconcode = data.icon;
            var temp = data.temperature;
            var desc = data.weather;

            var iconurl = "static/icons/" + iconcode + ".png";
            $('#wicon').attr('src', iconurl);
            $(".temperature-value").html(temp + " C");
        }
    });


}

$(document).ready(function () {
    weather();
    setInterval(weather, 500);
})