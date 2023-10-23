// function that write to the console after button click
let clickCount = 0;

function writeConsole() {
    get = document.getElementById("btn");
    get.onclick = function() {
        clickCount++;
        console.log("Button clicked! Click count: " + clickCount);
        console.log("Don't click me!");
    }
}