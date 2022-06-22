function test(){
    var username = document.getElementById('uname').value;
    var pass = document.getElementById('psw').value;
    var data = JSON.stringify({"username":username, "password":pass});
    
    $.ajax ({
        url: "https://blogdrf.pythonanywhere.com/user/login/",
        type: "POST",
        data: data,
        dataType: "json",
        contentType: "application/json"
      }).done(function(data) {  
        // console.log(data.access);   
        sessionStorage.setItem("access_key", data.access); 
        // console.log(localStorage.getItem("access-key"));
        location.href = "file:///D:/blog_drf/frontend/index1.html";
      }).fail(function(data, err) {
        alert("fail " + JSON.stringify(err));
      });
}


