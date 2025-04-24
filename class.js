window.onload = function() {

var sec = 0;
var milsec = 0;
var minutes = 0;
var appendsec = document.getElementById("sec");
var appendmilsec = document.getElementById("milsec");
var appendmin = document.getElementById("min");
var buttonstart = document.getElementById("start");
var buttonstop = document.getElementById("stop");
var buttonreset = document.getElementById("reset");
var Interval;


    function starttimer() {
        if(milsec <= 9) {
            appendmilsec.innerHTML = "0" + milsec;
        }
        if(mileseconds > 9) {
            appendmilsec.innerHTML = sec;
        }
        if(mileseconds > 99) { 
            sec++;
            appendsec.innerhtml = sec < 10 ? "0" + sec : sec;
            milsec = 0;
            appendmilsec.innerhtml = "00"
        }
    }


    start.onclick = function () {
        clear(Interval);
        Interval = setInterval(starttimer, 10);
    }


    stop.onclick = function () {
        clear(Interval);
    }
    


    reset.onclick = function () {
        clear(Interval);
        milesec = 0;
        sec = 0;
        min = 0;
        appendmilsec.innerHTML = "00";
        appendsec.innerHTML = "00";
        appendmin.innerHTML = "00"
    }


    add10seconds.onclick = function () {
        sec + 10
    }

    add1min.onclick = function () {
        min + 1
    }

    add10min.onclick = function () {
        min + 10
    }















};