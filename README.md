# Custom-Prebuilts
This is a web app that finds or compiles a list of adequate pc parts based on specified gaming needs. The app's goal solves the following:
"As a Gamer, My Gpu is too slow for playing Indiana Jones and the Great Circle at recommended settings on my 1440p monitor. I need to identify a new GPU that satisfies the recommendation, and won't be bottlenecked by my cpu."

The scope of the final project is to allow the user to pick their current graphics card and cpu as well as their display resolution, pick a game with minimum or recommmended game play specifications, and the app determines whether the graphics card meets the game specification standard for the intended gaming experience. If the user's selected graphics card is not adequate, suggested graphics card option(s) on the market is presented.

## Prerequisites

* Python 3.12 or higher
* pip (Python package installer)
* A virtual environment (recommended)
* sqlite3

## Setup

1.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**

   

## Features:

* filter your hardware by make and model
* select a game from list, and choose between minimum or recommended hardware spec
* hardware spec by game will be displayed, and whether your equipment is currently compatible
* if your equipment is not compatible, we suggest the next necessary upgrade

3. **What funtionality is included**

* this is a read-only app that presents common hardware equipment that matches what you might have in your pc
* we use local storage to save your equipment configuration to prevent repeated data entry
* the database is populated using csv data and python scripts that interface didectly with the model
  * since parts change constantly, this is a good approach to keep equipment lists current

4. **In Progress**

* hardware quantifications to measure capabilities against game specs
  * (game spec provides one model, but there exists older and newer copmatible models)
* provide current system compatibility information (yes or no)
* formatting game specifications, and providing a steam link + thumbnail for each game
* some final touches
  * app title
  * css
  * page title
  * page icon
* test coverage
