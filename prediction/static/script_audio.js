document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        let audio = document.getElementById("liverAudio");
        let button = document.getElementById("testPlayButton");

        if (audio) {
            audio.muted = false;  // Ensure audio is not muted
            audio.volume = 1.0;   // Set volume

            // Try to autoplay
              audio.play().catch(error => {
                console.log("Autoplay blocked, requiring user interaction.");
                if (button) {
                    button.style.display = "block"; // Show button if needed
                    button.addEventListener("click", function () {
                        audio.play();
                        button.style.display = "none"; // Hide after playing
                    });
                }
            });
        }
    }, 1500);
});
