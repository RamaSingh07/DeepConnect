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

//feedback

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("feedbackForm");

  form.addEventListener("submit", function (e) {
      e.preventDefault();

      const name = document.getElementById("name").value;
      const email = document.getElementById("email").value;
      const feedbackType = document.getElementById("feedbackType").value;
      const rating = document.getElementById("rating").value;
      const comments = document.getElementById("comments").value;

      if (!name || !email || !comments) {
          alert("Please fill in all required fields.");
          return;
      }

      // Send data to backend (you need a backend for database & email handling)
      console.log("Submitting:", { name, email, feedbackType, rating, comments });

      alert("Thank you for your feedback!");
      form.reset();
  });
});

//volunteer form
document.getElementById("volunteerForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;
    let role = document.getElementById("role").value;
    let availability = document.getElementById("availability").value;
    let message = document.getElementById("message").value;

    if (name && email && phone && message) {
        alert("Thank you for volunteering! We will get back to you soon.");
        this.reset();
    } else {
        alert("Please fill out all required fields.");
    }
});

// //  Bootstrap JS 
// //    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>-->
// //     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    

// // Handle response and show result dynamically
// const resultSection = document.getElementById('result-section');
// const resultText = document.querySelector('.result');

// // Example to update result dynamically (mock response)
// function showResult(data) {
//     resultSection.classList.remove('d-none');
//     resultText.textContent = `Your cirrhosis risk is: ${data.cirrhosis_risk > 0.5 ? 'High' : 'Low'}`;
// }

// document.addEventListener("DOMContentLoaded", function() {
//     setTimeout(() => {
//         document.querySelector(".predict-container").style.opacity = "1";
//     }, 2000);
// });





    






  