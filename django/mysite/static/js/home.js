let slides = document.querySelector(".slider").children;
let prev = document.querySelector(".prev");
let next = document.querySelector(".next");
let indicator = document.querySelector(".indicator");
let index = 0;

prev.addEventListener("click", function(){
    prevSlide();
    updateCircleIndicator();
    resetTimer();
});

next.addEventListener("click", function(){
    nextSlide();
    updateCircleIndicator();
    resetTimer();
});

function circleIndicator(){
    for(let i=0;i<slides.length;i++){
        let div = document.createElement("div");
        div.setAttribute("onclick", "indicateSlide(this)");
        div.id=i;
        if(i==0){
            div.className = "active";
        }
        indicator.appendChild(div);
    }
}

function updateCircleIndicator(){
    for(let i=0;i<indicator.children.length;i++){
        indicator.children[i].classList.remove("active");
    }
    indicator.children[index].classList.add("active");
}

function indicateSlide(element){
    index = element.id;
    changeSlide();
    updateCircleIndicator();
    resetTimer();
}

circleIndicator();

function nextSlide(){
    if(index==slides.length-1){
        index=0;
    }
    else{
        index++;
    }
    changeSlide();
}

function prevSlide() {
    if (index == 0) {
        index = slides.length-1;
    }
    else {
        index--;
    }
    changeSlide();
}


function changeSlide(){
    for(let i=0; i<slides.length;i++){
        slides[i].classList.remove("active");

    }
    slides[index].classList.add("active");
}

function autoPlay(){
    nextSlide();
    updateCircleIndicator();
}

function resetTimer(){
    clearInterval(timer);
    timer = setInterval(autoPlay, 4000);
}

let timer = setInterval(autoPlay, 4000);
