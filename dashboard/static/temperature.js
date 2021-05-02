function temperature() {
    $.ajax({
        dataType: "json",
        type: 'GET',
        url: '/data/temperature/current',
        success: function (data) {
            var inside = data.inside;
            var outside = data.outside;

            $(".temp-el-inside .temperature #value").html(inside + ' C°');
            $(".temp-el-outside .temperature #value").html(outside + ' C°');

        }
    });
}

$(document).ready(function () {
    temperature();
    setInterval(temperature, 90000);
})