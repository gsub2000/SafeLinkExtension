console.log("Hello World");
//current site domain
//https://www.coolmath.com


var dom = document.domain;

var aTag = document.getElementsByTagName("a");

var badLinks = [];
badLinks.push(dom);
var linkDict = {};

for (let i = 0; i < aTag.length; i++){
    // console.log(aTag[i].href);
    var link = aTag[i].href;
    console.log(link)
    linkDict[link] = aTag[i];
    badLinks.push(aTag[i].href);


    // if ( link.indexOf('bit.ly') != -1 ){
    //     linkDict[link] = aTag[i];
    //     badLinks.push(aTag[i]);
    // }
    // else if ( link.indexOf('redirect') != -1 ){
    //     linkDict[link] = aTag[i];
    //     badLinks.push(aTag[i]);
    // }
    // else if ( link.indexOf('article') != -1 ){
    //     linkDict[link] = aTag[i];
    //     badLinks.push(aTag[i]);
    // }
    // else if ( link.indexOf(dom) == -1 ){
    //     linkDict[link] = aTag[i];
    //     badLinks.push(aTag[i]);
    // }
};

msgString = "";
badLinks.forEach(elem => {
    msgString += elem + ','
});

chrome.runtime.sendMessage({message: msgString}, async function(response) {

    console.log("RESPONSE");
    var cleanData = []
    var badsites = response.substring(1, response.length-1).split(',');
    for(let i = 0; i < badsites.length; i++){
        if (badsites[i].length > 5){
            cleanData.push(badsites[i].trim().substring(1, badsites[i].length-2))
        }
    }
  

    for(let i = 0; i < cleanData.length; i++){
        if (cleanData[i] in linkDict){
            console.log(cleanData[i]);
            highlight(linkDict[cleanData[i]]);
        }
    }
    console.log('DONE')

});


// for(let i = 1; i < badLinks.length; i++){
//     highlight(badLinks[i]);
// }

function highlight(tag) {
    if (tag){
        var h = tag.innerHTML;
        var s2 = '<span style="background-color: aqua;">' + h + '</span>';
        
        tag.style.backgroundColor = "aqua";
    }
};

