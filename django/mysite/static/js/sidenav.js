let sidenav = document.querySelector(".sidenav");
let logo = document.querySelector(".logo");
let appear = document.querySelector(".appear");
let disappear = document.querySelector(".disappear");


logo.addEventListener("click", function(){
    if(sidenav.classList.contains("disappear")){
        sidenav.classList.remove("disappear");
        sidenav.classList.add("appear");
    }
    else if(sidenav.classList.contains("appear")) {
      sidenav.classList.remove("appear");
      sidenav.classList.add("disappear");
    }
});