function temperature_graph() {
    $.ajax({
        dataType: "json",
        type: 'GET',
        url: '/data/temperature/current',
        success: function (data) {
            var labels = data.map(function (e) {
                return e.hour;
            });
            var temperature = data.map(function (e) {
                return e.temperature;
            });;

            console.log(labels);
            console.log(temperature);


        }
    });
}

$(document).ready(function () {
    temperature_graph();
    setInterval(temperature, 50000);
})



