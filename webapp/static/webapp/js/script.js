let headWrapper = document.getElementById('head-wrapper')
let nav = document.getElementById("nav")
let fixedNav = document.getElementById("fixed-nav")
let imageLink = document.getElementById('nav-image-link')
let carousel = document.getElementById("main-slider")

let navElements = [
    document.querySelectorAll(".nav-link-home"),
    document.querySelectorAll(".nav-link-services"),
    document.querySelectorAll(".nav-link-support"),
    document.querySelectorAll(".nav-link-about"),
    document.querySelectorAll(".nav-link-contact")
]



let navoptions={}
let navobserver = new IntersectionObserver((entries, navobserver)=>{
    entries.forEach(entry => {
        if(entry.isIntersecting){
            // nav.classList.remove('fixed-top')
            nav.classList.remove('visibility-hidden')
            fixedNav.classList.add('d-none')

        }else{
            // nav.classList.add('fixed-top')
            nav.classList.add('visibility-hidden')
            fixedNav.classList.remove('d-none')

        }
    });
} , navoptions)
navobserver.observe(imageLink)

carouseloptions={
    rootMargin: `-${headWrapper.offsetHeight}px`
}
let carouselObserver = new IntersectionObserver((entries, carouselObserver)=>{
    entries.forEach(entry => {
        if(entry.isIntersecting){
            addActiveClass(0 , navElements)
        }else{
            addActiveClass(1 , navElements)
        }
    });
} , carouseloptions)
carouselObserver.observe(carousel)


function scrollToElement(elementId) {
    let element = document.getElementById(elementId);
    if (element) {
        let elementPosition = element.getBoundingClientRect().top + window.scrollY;
        window.scrollTo({
            top: elementPosition - headWrapper.offsetHeight,
            behavior: 'smooth' // Smooth scrolling
        });
    }
}

function scrollToTop(){
    window.scrollTo({
        top:0,
        behavior: 'smooth' 
    })
}


function addActiveClass(index , navElements){
    navElements.forEach((element , counter)=>{
        if(index == counter){
            element[0].classList.add("active")
            element[1].classList.add("active")
        }else{
            element[0].classList.remove("active")
            element[1].classList.remove("active")
        }
    })
}