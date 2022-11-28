const API = "http://127.0.0.1:81"
let manaZina = document.querySelector(".manaZina")
let chataZina = document.querySelector(".chataZina")
let vards = document.querySelector(".vards")

function sutitZinu(){
    console.log("darbojas")
    chataZina.innerHTML += '<br/>' + manaZina.value
    fetch(API+'/suit/'+vards.value+'/'+manaZina.value)
}

async function ieladetChatZinas(){
    let datNoServera = await fetch(API + "/lasit")
    let dati = await datNoServera.jason()
    console.log(dati)

    chataZina.innerHTML = dati
}

//setInterval(ieladetChatZinas,1000)

async function ieladetChatZinasJson(){
    let datiNoServera = await fetch(API +'/lasit')
    let dati = await datiNoServera

    i=0;
    while(i < await dati.length){
        chataZina.innerHTML = chataZina.innerHTML + dati[i]['Vards'] + ":" + dati[i]['zinas'] + '<br'
    }
}