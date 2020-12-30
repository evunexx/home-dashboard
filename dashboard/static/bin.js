function bin() {
    $.ajax({
        dataType: "json",
        type: 'GET',
        url: '/data/bin',
        success: function (data) {
            var blue = data.blue;
            var green = data.green;
            var grey = data.grey;
            var yellow = data.yellow;

            $(".foo-blue #foo-date").html(blue);
            $(".foo-green #foo-date").html(green);
            $(".foo-grey #foo-date").html(grey);
            $(".foo-yellow #foo-date").html(yellow);
        }
    });
}

$(document).ready(function () {
    bin();
    setInterval(bin, 900000);
})