// particlesJS("particles-js", {
//   particles: {
//     number: { value: 80, density: { enable: true, value_area: 800 } },
//     color: { value: "#caf0f8" },
//     shape: { type: "circle" },
//     opacity: { value: 0.5 },
//     size: { value: 5 },
//     line_linked: { enable: true, distance: 150, color: "#90e0ef", opacity: 0.4, width: 1 },
//     move: { enable: true, speed: 2, direction: "none", random: false, straight: false, out_mode: "bounce" },
//   },
//   interactivity: {
//     detect_on: "canvas",
//     events: { onhover: { enable: true, mode: "grab" }, onclick: { enable: true, mode: "push" } },
//     modes: { grab: { distance: 200, line_linked: { opacity: 1} }, push: { particles_nb: 4 } },
//   },
//   retina_detect: true,
// });

document.addEventListener("DOMContentLoaded", function () {
  setTimeout(() => {
      document.querySelectorAll(".card").forEach((card, index) => {
          setTimeout(() => {
              card.classList.add("show");
          }, index * 300); // Staggered animation effect
      });
  }, 2000); // 2-second delay before animation starts
});

  