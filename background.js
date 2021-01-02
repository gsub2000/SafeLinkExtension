console.log("this is the bg.js file");

chrome.runtime.onMessage.addListener(
    function(request, sender, response){
        console.log("we did it folks");
        
        $.ajax({
            url: "http://127.0.0.1:5000/",
            type: "POST",
            data: request,
            success: function(resp){
                console.log(resp);
                response(resp)

            },
            error: function(er,a,b){
                console.log("error has occurred");
            }
        });
        return true;
        // sendResponse(JSON.stringify(temp));
        // chrome.runtime.sendMessage(null,"hi")
    });