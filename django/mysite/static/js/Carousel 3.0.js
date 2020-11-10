let track = document.querySelector(".track");
let  slides_cards = Array.from(track.children);
let left = document.querySelector(".left");
let right = document.querySelector(".right");
let nav = document.querySelector(".nav");
let indicator_cards = Array.from(nav.children);

let slideWidth =  slides_cards[0].getBoundingClientRect().width;
console.log(slideWidth);
 slides_cards.forEach(function(slide,index){
    slide.style.left = slideWidth * index + "px";
});


function moveToSlide(track, current_slide, target_slide){
    track.style.transform = "translateX(-" + target_slide.style.left + ")";
    console.log(track.style.transform);
    current_slide.classList.remove("current_slide");
    target_slide.classList.add("current_slide");
}

right.addEventListener("click", function changeRight(){
    let currentSlide = track.querySelector(".current_slide");
    let nextSlide = currentSlide.nextElementSibling;
    let currentDot = nav.querySelector(".current_slide");
    let targetDot = currentDot.nextElementSibling;
    let nextIndex =  slides_cards.findIndex(slide => slide === nextSlide)

    moveToSlide(track, currentSlide, nextSlide);
    updateDots(currentDot, targetDot);
    Arrows(nextIndex, left, right,  slides_cards);
});

left.addEventListener("click", function changeLeft() {
    let currentSlide = track.querySelector(".current_slide");
    let previousSlide = currentSlide.previousElementSibling;
    let currentDot = nav.querySelector(".current_slide");
    let targetDot = currentDot.previousElementSibling;
    let prevIndex =  slides_cards.findIndex(slide => slide === previousSlide)

    moveToSlide(track, currentSlide, previousSlide);
    updateDots(currentDot, targetDot);
    Arrows(prevIndex, left, right,  slides_cards);
});

function updateDots(currentDot, targetDot){
    currentDot.classList.remove("current_slide");
    targetDot.classList.add("current_slide");
}

function Arrows(targetIndex, left, right,  slides_cards){
    if (targetIndex === 0) {
        left.classList.add("is_hidden");
        right.classList.remove("is_hidden");
    }
    else if (targetIndex ===  slides_cards.length - 1) {
        left.classList.remove("is_hidden");
        right.classList.add("is_hidden");
    }
    else {
        left.classList.remove("is_hidden");
        right.classList.remove("is_hidden");
    }
}

nav.addEventListener("click", function(e){
    let targetDot = e.target.closest("button");
    console.log(targetDot);

    if(!targetDot){
        return;
    }
    let currentSlide = track.querySelector(".current_slide");
    let currentDot = nav.querySelector(".current_slide");
    let targetIndex = indicator_cards.findIndex(dot => dot === targetDot);
    let targetSlide =  slides_cards[targetIndex];

    moveToSlide(track, currentSlide, targetSlide);
    updateDots(currentDot, targetDot);
    Arrows(targetIndex, left, right,  slides_cards);
    
});
