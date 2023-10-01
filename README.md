# Let There Be Light
#### Video demo <https://youtu.be/BqvifkPijmo>

### Description
Let There Be Light is a web-based puzzle game. The player is given a 3x3 grid of buttons. Each button is either on (yellow) or off (grey). Clicking a button will not only toggle it, but toggle the adjacent buttons too. The game is complete when all buttons in the grid are on.

Each level has a unique configuration of on/off buttons, and the difficulty increases with ascending level number. The challenge is to switch all the buttons on in the fewest number of clicks.

#### Access
You can play Let There Be Light directly in your web browser, no installation required. Navigate to https://scottt-1212-refactored-memory-v44977rgrvghxxxg-5000.app.github.dev/ to start playing.

#### How to Play
Once you're on the home page, here's how to get started:
1. Click Login to give yourself a username. This allows you to submit your scores to the leaderboard.
2. You'll now be able to select a level from the dropdown on the homepage. Choose one and click Play.
3. Click a button to toggle the switch. Remember that the adjacent switches will also toggle! Here's an example where X represents an off switch and O represents an on switch:
| --- | --- | --- |
| X | X | X |
| X | X | X |
| X | X | X |
When the center button is clicked, it becomes:
| --- | --- | --- |
| X | O | X |
| O | O | O |
| X | O | X |

4. Your score will be displayed when all of the buttons are switched on.
5. Now you can either navigate to Home to play another level, or submit your score to the Leaderboard.

If you want to see how the game works before playing, click Practice to play on a grid of blank switches. You can also navigate to the Leaderboard to see the highscores for each level.

#### Project Structure
- **app.py:** The main file in the Flask application. It defines the routes of the web application and the back-end programming. I chose Flask because the website is dynamic. For example, when game.html is rendered, the configuration of the switches will depend on which level was selected by the user on index.html.
- **levels.csv:** This csv file contains data for each of the levels. The level data is broken down into the following columns:
    - **number:** A unique identifier for each level.
    - **status:** This must be "active" for the level to appear in the dropdown boxes on index.html and leaderboard.html.
    - **button coordinates, e.g., "0,0":** The remaining columns establish the starting configuration of the buttons in the 3x3 grid. The buttons are labelled according to their coordinates. The first digit is the row, 0 being the top row and 2 being the bottom row. The second digit refers to the column, left-most being 0 and right-most being 2. Each button can either be "on" or "off".
- **leaderboard.db:** A SQLite database containing a leaderboard table. When a level is finished and all buttons are on, the player is offered to submit their score to the leaderboard. This inserts the player's name and score into the table for that level. In the leaderboard.html webpage, the player can select a level to view it's best scores. This retrieves the top 10 scores for the selected level.
- **static/:** This directory contains files that do not need to be processed by the server before sending to the client.
    - **style.css:** Contains the CSS rules that style the elements in the web application.
    - **script.js:** Contains the javascript for the game. When the DOM is loaded, this adds event listeners to the game buttons, changing the class of the button when clicked to create the illusion of a light bulb toggling. It also counts the number of clicks the buttons receive so that a score can be generated. When the win condition is met (all lights are on), script.js will display the win message to the player.
    - **leaderboard.sql:** Contains the schema for the leaderboard table in the leaderboard.db database.
    - **favicon.ico:** Provides the light bulb icon that appears in the browser tab.
- **templates/:** This directory contains the html files for the website pages.
    - **layout.html:** Contains the information stored in the HTML head, navigation bar information, a section for flashed messages to appear (used as alerts for certain conditions, e.g., logged in/out successfully), and for the Game title.
    - **index.html:** Contains the homepage information; instructions on how to play the game, button to the practice page. If the user is logged in, it will display the list of levels available to play, else it will prompt the user to log in.
    - **game.html:** This is where the main gaimplay takes place. GET requests will display the level selected on the index page. POST requests can be made once the lights all turn on, it submits the score and player name to the leaderboard database.
    - **login.html:** This page contains a form for the player to input their name. This name is stored in the session and used to record an identifier when submitting a highscore.
    - **logout.html:** Contains a form to end the user's session.
    - **practice.html:** Displays a blank grid of game buttons used to demonstrate how the gameplay mechanics work.
    - **leaderboard.html:** GET requests to this page will display a selection form displaying options for each game level in levels.csv. When the form is submitted, leaderboard.html retrieves data from leaderboard.db, to display the 10 lowest scores in ascending order for the selected level, along the associated player's name.

#### Contributing
Contributions are welcomed. Here's how you can contribute:
1. Fork the repository to your own GitHub account.
2. Clone the project to your machine.
3. Create a branch in your local repository.
4. Make your changes and commit them to your local repository.
5. Push your changes to your fork.
6. Create a pull request to my repository.

#### Credits
This project was made possible with the help of the following tools and libraries:
- [CS50](https://cs50.harvard.edu): Special thanks to Harvard University's Introduction to Computer Science course, for providing the foundational knowledge and skills used in this project.
- [Flask](https://flask.palletsprojects.com/en/2.3.x/): A lightweight web application framework for Python.
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/): A modern and designer-frendly templating language for Python.
- [SQLite](https://www.sqlite.org/index.html): A C library that provides a lightweight disk-based database.
- [Twemoji](https://twemoji.twitter.com/): For the use of the light bulb emoji as a favicon under the CC-BY 4.0 license.

This project was inspired by:
- [Spyro 2: Gateway to Glimmer](https://insomniac.games/game/spyro-the-dragon/): In Idol Springs, Spyro is presented with a minigame to unlock an optional door to a collectable orb. This mechanics of this project was inspried by that minigame.