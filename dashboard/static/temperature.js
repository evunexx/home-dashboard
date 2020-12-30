function temperature() {
    $.ajax({
        dataType: "json",
        type: 'GET',
        url: '/data/temperature/current',
        success: function (data) {
            var inside = data.inside;
            var outside = data.outside;

            $(".temp-el-inside .temperature #value").html(inside);
            $(".temp-el-outside .temperature #value").html(outside);

        }
    });
}

$(document).ready(function () {
    temperature();
    setInterval(temperature, 900000);
})