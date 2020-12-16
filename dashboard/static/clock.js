function realtimedateandclock() {
    var clock = new Date();

    var hours = clock.getHours();
    var minutes = clock.getMinutes();
    var day = clock.getDay();
    function getmonthname() {
        var t = new Date();
        const monthNames = ["Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"];
        var month = monthNames[t.getMonth()];
        console.log(month)
        return month;
    }
    var month = getmonthname();

    var htmldate = day + "." + month
    $( ".date" ).html(htmldate);

    var htmltime = hours + ":" + minutes
    $(".time").html(htmltime);

}
$(document).ready(function() {
    realtimedateandclock();
    setInterval(realtimedateandclock, 500);
  })
