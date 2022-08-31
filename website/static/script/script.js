function check() {
    alert("i am working")
}


let forexReceive = document.getElementById("#forex-receive");
forexReceive.style.display = "none";

let forexSend = document.getElementById("#forex-send")
// forexSend.style.display

function toggleSendCalc(){
    if (forexReceive.style.display = 'none') {
        forexReceive.style.display = '';
        forexSend.style.display = "none";
    }
}


function toggleReceiveCalc() {
    if (forexSend.style.display = "none") {
        forexSend.style.display = "";
        forexReceive.style.display = "none";
    }
}


forex = document.getElementById("#forex")
let euroPrime = document.getElementById("#euro")
let EUR = euroPrime.value;
let nairaPrime = document.getElementById("#naira")
let NGN = nairaPrime.value

// console.log(USD, EUR, NGN);


function sendCalc() {
    let naira = euroPrime.value * nairaPrime.value;
    nairaPrime.value = naira;
    console.log(naira)
}

function resetSendCalcBtn() {
    console.log(EUR, NGN); // debug
    euroPrime.value = EUR;
    nairaPrime.value = NGN;
    console.log("you clicked reset") // debug
}


// let usdPrime2 = document.getElementById("#usd-r")
// let USD2 = usdPrime2.value;
let receiveEuroPrime = document.getElementById("#euro-receive")
let receiveEUR =  receiveEuroPrime.value;
let receiveNairaPrime = document.getElementById("#naira-receive")
let receiveNGN = receiveNairaPrime.value;


function receiveCalc(){
    // let euro = euroPrime2.value+1 * usdPrime2.value;
    // let usd = nairaPrime2.value * usdPrime2.value;
    let euro = receiveEuroPrime.value * receiveNairaPrime.value;
    // let naira = usdPrime2.value * nairaPrime2.value;
    console.log(euro);
    // ReceiveEuroPrime.value = euro;
    receiveNairaPrime.value = euro
    // nairaPrime2.value = naira;
}

function resetReceiveCalcBtn() {
    console.log(receiveEUR, receiveNGN); // debug
    receiveEuroPrime.value = receiveEUR
    receiveNairaPrime.value = receiveNGN
    console.log("you clicked reset") // debug
}



