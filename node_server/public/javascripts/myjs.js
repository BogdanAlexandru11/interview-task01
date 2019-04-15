$(document).ready(function () {
        //  the port used is 5768
     var ws = new WebSocket("ws://127.0.0.1:5678/"),
    messages = document.createElement('ul');
    ws.onmessage = function (event) {
    var messages = document.getElementsByTagName('ul')[0],
        message = document.createElement('li'),
        content = document.createTextNode(event.data);
    message.appendChild(content);
    messages.appendChild(message);
    var listLength=$('ul#mylist li').length;
    // if there are more than 10 elements in the list, remove the first length-10 elements
    if(listLength>10){
        $('li').slice(0, (listLength-10)).remove();
    }
    };
    document.getElementById("mylist").appendChild(messages);
    
});



