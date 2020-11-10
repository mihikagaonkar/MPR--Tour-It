let heart = document.querySelectorAll(".heart");

heart.forEach(function(button){
    button.addEventListener("click", function(){
    if(button.classList.contains("liked")){
        button.classList.remove("liked");
    }
    else{
        button.classList.add("liked");
    }
    });
});
