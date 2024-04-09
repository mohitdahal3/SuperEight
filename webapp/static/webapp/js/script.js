
let imageLink = document.getElementById('nav-image-link')
let options={}
let observer = new IntersectionObserver((entries, observer)=>{
    entries.forEach(entry => {
        if(entry.isIntersecting){
            document.getElementById("nav").classList.remove('fixed-top')
        }else{
            document.getElementById("nav").classList.add('fixed-top')
        }
    });
} , options)
observer.observe(imageLink)



function scrollToElement(elementId) {
    let element = document.getElementById(elementId);
    if (element) {
        let elementPosition = element.getBoundingClientRect().top + window.scrollY;
        window.scrollTo({
            top: elementPosition - document.getElementById("head-wrapper").offsetHeight,
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
