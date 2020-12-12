$.ajax({
    url: "http://127.0.0.1:5000/data",
    type: "POST",
    success: function(resp){
        console.log(resp);
    },
    error: function(er,a,b){
        console.log("error has occurred");
    }
});

function process(){
    return $.ajax({
    url: "http://127.0.0.1:5000/data",
    type: "POST",
    data: request,
    success: async function(resp){
        console.log(resp);
        console.log("got it");
        temp = resp;

    },
    error: function(er,a,b){
        console.log("error has occurred");
    }
});
}

process().then(function(res) {
reponse(JSON.stringify(res));
})