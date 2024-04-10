let headWrapper = document.getElementById('head-wrapper')
let nav = document.getElementById("nav")
let fixedNav = document.getElementById("fixed-nav")
let imageLink = document.getElementById('nav-image-link')
let carousel = document.getElementById("carousel")
let elementsToBeObserved = document.querySelectorAll(".to-be-observed")


let navElements = [
    document.querySelectorAll(".nav-link-home"),
    document.querySelectorAll(".nav-link-services"),
    document.querySelectorAll(".nav-link-packages"),
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

let elementsOnScreen = new Set()

let contentsOptions={
    rootMargin: `-35%`
}
let contentsObserver = new IntersectionObserver((entries, contentsObserver)=>{
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            let index = getIndexFromTarget(entry.target.id);
            if (index !== undefined) {
                elementsOnScreen.add(index);
            }
        } else {
            let index = getIndexFromTarget(entry.target.id);
            if (index !== undefined) {
                elementsOnScreen.delete(index);
            }
        }
    });
    changeActiveOnSetUpdate(elementsOnScreen);
} , contentsOptions)

elementsToBeObserved.forEach((element)=>{
    contentsObserver.observe(element)
})


function scrollToElement(elementId) {
    let element = document.getElementById(elementId);
    if (element) {
        let elementPosition = element.getBoundingClientRect().top + window.scrollY;
        window.scrollTo({
            top: elementPosition - (nav.offsetHeight + 40),
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

function getIndexFromTarget(targetId){
    switch (targetId) {
        case 'carousel':
            return 0

        case 'our-services':
            return 1

        case 'packages':
            return 2

        case 'contact':
            return 3
    
        default:
            return
    }
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

function changeActiveOnSetUpdate(set){
    let sortedSet = new Set([...set].sort((a, b) => a - b));
    addActiveClass([...sortedSet][0] , navElements)
}


function redirectToCustomerLogin(){
    window.open("https://selfcare.supereight.com.np", "_blank");
}