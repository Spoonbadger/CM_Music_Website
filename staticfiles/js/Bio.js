var aud = document.getElementById("ASong").children[0];
        var isPlaying = false;
        aud.pause();

            // Event listener to ensure audio is ready
        aud.addEventListener('canplaythrough', function() {
            console.log("Audio is ready to play");
        });

        function playPause() {
            var musicButton = document.getElementById('ASong')

        if (isPlaying) {
            aud.pause();
            musicButton.textContent = "Music ON";
        } 
        else {
            aud.play();
            musicButton.textContent = "Music OFF";
            console.log("Button clicked on!")
        }
        isPlaying = !isPlaying;
        }