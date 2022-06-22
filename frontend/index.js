$(document).ready(function() {
  var key = sessionStorage.getItem("access_key");
  console.log(key);
        $.ajax ({
            url: "https://blogdrf.pythonanywhere.com/api/posts/",
            type: "GET",
            contentType: "application/json",
            headers: {
              Authorization: 'Bearer '+key
              // "Authorization": "Basic " + btoa(USERNAME + ":" + PASSWORD)
            },
          }).done(function(data) {
            var data = data[0];  
            console.log(data);    
            document.getElementById("title").innerHTML = data.title;  
            // document.getElementById("id").innerHTML = data.id;
            document.getElementById("text").innerHTML = data.text;
            document.getElementById("status").innerHTML = data.status;
            document.getElementById("created_date").innerHTML = data.created_date;
          }).fail(function(data, err) {
            console.log("fail " + JSON.stringify(err));
          });
  });

  function getData() {
    location.href = "file:///D:/blog_drf/frontend/view.html";
  }


