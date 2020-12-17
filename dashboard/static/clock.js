function realtimedateandclock() {
    var clock = new Date();
    var hours = clock.getHours();
    var minutes = clock.getMinutes();
    var date = clock.getDate();
    var month = getmonthname();
    var dayname = getdayname();

    function getmonthname() {
        var t = new Date();
        const monthNames = ["Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"];
        var month = monthNames[t.getMonth()];
        return month;
    }

    function getdayname() {
        var t = new Date();
        const dayNames = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag",
        "Samstag", "Sonntag"];
        var day = dayNames[t.getDay()];
        return day;
    }



    var htmldate = dayname + ", " + date + "." + month;
    $( "#date" ).html(htmldate);

    var htmltime = hours + ":" + minutes;
    $("#time").html(htmltime);

}
$(document).ready(function() {
    realtimedateandclock();
    setInterval(realtimedateandclock, 500);
  })
