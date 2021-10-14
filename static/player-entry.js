function formSubmit() {
    //Most form elements should be hidden by default
    greenIdStr = 'GreenId'
    redIdStr = 'RedId'
    greenNmStr = 'GreenName'
    redNmStr = 'RedName'
    for (let i = 0; i < 15; i++) {
        concatGreenIdStr = greenIdStr + i.toString();
        concatRedIdStr = redIdStr + i.toString();
        concatGreenNmStr = greenIdStr + i.toString();
        concatRedNmStr = redNmStr = i.toString();

        if (document.getElementById(concatGreenIdStr).value != "") {
            document.getElementById(concatGreenNmStr).inputMode="hidden";
        }

        if (document.getElementById(concatRedIdStr).value != "") {
            document.getElementById(concatGreenNmStr).type = "text";
        }
    }
}

//$( "#GreenId0" ).load("../templates/player-entry.html #GreenId0");