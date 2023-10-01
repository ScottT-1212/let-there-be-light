document.addEventListener('DOMContentLoaded', function() {

    // Select all buttons whose data-type is "game"
    let light = document.querySelectorAll("button[data-type='game']");
    let nClicks = 0;

    // function to toggle light switch when clicked
    for (let i = 0; i < light.length; i++) {

        light[i].addEventListener('click', toggleLight)

        function toggleLight() {

            // increase click counter
            nClicks++;

            // toggle clicked light
            if (this.className == 'off') {
                this.className = 'on';
            } else {
                this.className = 'off';
            }

            // get id of current light
            let currentLightId = light[i].id;
            let coordinates = currentLightId.split(',');
            coordinates[0] = Number(coordinates[0]);
            coordinates[1] = Number(coordinates[1]);

            // find coordinates of adjacent lights
            let topCoordinates = coordinates.slice();
            let bottomCoordinates = coordinates.slice();
            let leftCoordinates = coordinates.slice();
            let rightCoordinates = coordinates.slice();

            topCoordinates[0] -= 1;
            topLightId = topCoordinates.toString();

            bottomCoordinates[0] += 1;
            bottomLightId = bottomCoordinates.toString();

            leftCoordinates[1] -= 1;
            leftLightId = leftCoordinates.toString();

            rightCoordinates[1] += 1;
            rightLightId = rightCoordinates.toString();

            // toggle adjacent lights
            adjacentLights = [topLightId, bottomLightId, leftLightId, rightLightId];

            for (let j = 0; j < adjacentLights.length; j++) {
                let neighbourLight = document.getElementById(adjacentLights[j]);

                if (neighbourLight == null) {

                } else {
                    if (neighbourLight.className == 'off') {
                        neighbourLight.className = 'on';
                    } else {
                        neighbourLight.className = 'off';
                    }
                }
            }

            // update click counter
            document.querySelector("#clicks").innerHTML = nClicks;

            // alert player when all lights are on
            let nLightsOn = 0;
            for (let j = 0; j < light.length; j++) {
                if (light[j].className == "on") {
                    nLightsOn++;
                }
            }
            if (nLightsOn == light.length) {
                winSection = document.getElementById("win-section").style.display = "block";

                document.querySelector("#win").innerHTML = "You've turned on all the lights!";
                document.querySelector("#win-message").innerHTML = "You did it in " + nClicks + " clicks";

                // disable light switches
                for (let j = 0; j < light.length; j++) {
                    light[j].outerHTML = light[j].outerHTML;
                }

                // set html score input to nClicks
                document.querySelector('#score').value = nClicks;

                return;
            }

            return;
        }
    }
});