var seq = "theta"
var input = ""
window.addEventListener("keypress", function(e) {
    input += String.fromCharCode(e.keyCode)

    for (var i = 0; i < seq.length; i++) {
        if (input[i] != seq[i] && input[i] != undefined) {
            input = ""
        }
    }

    if (input == seq) {
        startGame();

        input = ""
    }
})

function startGame(){
    var element = document.getElementById("boring");
    element.classList.add("theta");

    document.getElementById("header").style.display = 'none';
    document.getElementById("theta").style.display = 'block';

    var audio = new Audio('../assets/drama.mp3');
    audio.play();



}
