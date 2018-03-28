  function fillModal(parent, a){
    //document.getElementById("replyCheeps"+a).innerHTML = "THIS IS A TEST"
    var form = new FormData();
    form.append("parent", parent);

    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "{{=URL('replies')}}",
      "method": "POST",
      "processData": false,
      "contentType": false,
      "mimeType": "multipart/form-data",
      "data": form
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
      document.getElementById("replyCheeps"+a).innerHTML = response;
    });
  }

function likeCheep(cheepId, a){
    //document.getElementById("replyCheeps"+a).innerHTML = "THIS IS A TEST"
    var form = new FormData();
    form.append("cheepId", cheepId);

    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "{{=URL('like')}}",
      "method": "POST",
      "processData": false,
      "contentType": false,
      "mimeType": "multipart/form-data",
      "data": form
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
      n = parseInt(document.getElementById("likeButton"+a).innerHTML.trim().split(" ")[1]);

      document.getElementById("likeButton"+a).innerHTML = "Like " + (n+parseInt(response));
    });
  }
function recheepButton(cheepId){
    //document.getElementById("replyCheeps"+a).innerHTML = "THIS IS A TEST"
    var form = new FormData();
    form.append("cheepId", cheepId);

    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "{{=URL('recheep')}}",
      "method": "POST",
      "processData": false,
      "contentType": false,
      "mimeType": "multipart/form-data",
      "data": form
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    window.location = "{{=URL('home')}}";
    });
  }
