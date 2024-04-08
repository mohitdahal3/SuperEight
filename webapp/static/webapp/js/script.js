// let lastScrollTop = 0;
// let scrollDirection = null; // Variable to track scroll direction
// let consecutiveScrolls = 0; // Counter for consecutive scrolls in the same direction
// let navbar = document.getElementById("nav");
// let navbarHeight = navbar.offsetHeight

// window.addEventListener("scroll", function() {
//     if (isMobile()) {
//         let currentScroll = window.scrollY || document.documentElement.scrollTop;

//         if (currentScroll > lastScrollTop) {
//             // Scroll down
//             if (scrollDirection !== "down") {
//                 scrollDirection = "down";
//                 consecutiveScrolls = 1;
//             } else {
//                 consecutiveScrolls++;
//             }
//         } else {
//             // Scroll up
//             if (scrollDirection !== "up") {
//                 scrollDirection = "up";
//                 consecutiveScrolls = 1;
//             } else {
//                 consecutiveScrolls++;
//             }
//         }

//         if (currentScroll <= 0) {
//             navbar.classList.remove("d-none");
//             consecutiveScrolls = 0; // Reset the counter
//             return; // Exit the function early
//         }

//         // Check if ten consecutive scrolls in the same direction have occurred
//         if (consecutiveScrolls > (navbarHeight/2) + 5) {
//             if (scrollDirection === "down") {
//                 navbar.classList.add("d-none");
//             } else {
//                 navbar.classList.remove("d-none");
//             }
//             // Reset the counter
//             consecutiveScrolls = 0;
//         }

//         lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
//     }
// });


// function isMobile() {
//     return window.innerWidth < 992;
// }