const API = "http://127.0.0.1:81"
let manaZina = document.querySelector(".manaZina")
let chataZina = document.querySelector(".chataZina")
let vards = document.querySelector(".vards")

function sutitZinu(){
    console.log("darbojas")
    chataZina.innerHTML += '<br/>' + manaZina.value
    fetch(API+'/suit/'+vards.value+'/'+manaZina.value)
}