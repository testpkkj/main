let data = require("./epgdata.json");

//--------------------------------------------------------
let titleArray = data.map(i => i.title);

let filteredData = data.map(i => {
    return ({
        id: i.id,
        title: i.title,
        epg: i.epg ? i.epg.length : 0
    })
})
// .filter(i => i);

let filteredData1 = data.filter(i => {
    return (!i.epg || i.epg.length === 0)
}).map(i => {
    return ({
        id: i.id,
        title: i.title,
        epg: i.epg ? i.epg.length : 0
    })
})
console.log(filteredData1);
//=====================================================

let EPGArray = data.filter(i =>{
    return (!i.epg || i.epg.length === 0)
}).map(i =>{
    return({ 
        title: i.title,
        id: i.id
    })
})
    



console.log("No Epg",EPGArray);

console.log("Total No. of Object",data.length);