const sleep = m => new Promise(r => setTimeout(r, m))

async function getContacts() {
    
    let numeros = document.querySelector(".widthWrap--d4598");
    
    
        if (numeros) {
        
    
    
    let grupos = [];
        

    grupos = grupos.filter((este, i) => grupos.indexOf(este) === i)
    
    var gruposelem = document.createElement("numeros");
    grupos.forEach(value => 
        (grupoelem = document.createElement("numero"),
        grupoelem.innerHTML = value,
        gruposelem.appendChild(grupoelem))
    )
    document.body.appendChild(gruposelem);
    

}};

getContacts()