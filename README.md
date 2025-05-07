# Project Name: Custom-Prebuilts

## Description

This is a web app that finds or compiles a list of adequate pc parts based on specified gaming needs. The app's goal solves the following:

"As a Gamer, My Gpu is too slow for playing Indiana Jones and the Great Circle at recommended settings on my 1440p monitor. I need to identify a new GPU that satisfies the recommendation, and won't be bottlenecked by my cpu."

The scope of the final project is to allow the user to pick their current graphics card and cpu as well as their display resolution, pick a game with minimum or recommmended game play specifications, and the app determines whether the graphics card meets the game specification standard for the intended gaming experience. If the user's selected graphics card is not adequate, suggested graphics card option(s) on the market is presented.

Functionality:
* Filter your GPU hardware by make and model
* Select a game from list, and choose between minimum or recommended hardware spec
* Hardware spec by game will be displayed, and whether your equipment is currently compatible
* If your equipment is not compatible, we list the game publisher's recommended graphics card

## Features Implemented

### Backend
Data Modeling:
- Created models for games, hardware (GPU, CPU, motherboard), and specs with relational links (ForeignKey) and constraints (UniqueConstraint).
- Supported nullable fields and specific data types for flexibility and integrity.

REST API:
- Built read-only API endpoints using ReadOnlyModelViewSet for all models.
- Used ModelSerializer for JSON serialization, with custom fields and computed data (e.g., GPU performance metrics).
- Enabled filtering on game specs by game ID and spec type.

Admin Interface:
- Customized admin views for GPU, game specs, and specs with tailored list displays, search, filters, and sorted dropdowns.

Data Import Automation:
- Scraped GPU performance data (e.g., FPS metrics, specs) from Tom's Hardware graphics card performance test metrics.
- Developed AI-generated Python scripts to automate GameSpec data import from CSV, minimizing manual entry.
- Included error handling for missing records and invalid data, with logging for troubleshooting.


### Front End

Data Fetching and State Management:
- Built React hooks (useGpus, useGameSpecs, useGames) to fetch backend data via REST API.
- Used useState for GPUs, games, specs, filters, loading, and errors; useEffect for API calls and side effects.

Dynamic Filtering and User Interaction:
- Enabled GPU filtering by manufacturer and game spec filtering by game ID/spec type.
- Added dropdowns and radio buttons for selecting GPU, game, and spec type with real-time updates.

Local Storage Persistence:
- Saved user selections (GPU, game) in localStorage for session persistence.
- Pre-populated selections from localStorage on mount.

UI and Styling:
- Created responsive UI with CSS flexbox and container design.
- Styled tables, dropdowns, and radio buttons; supported dark mode with prefers-color-scheme.
- Used color-coded indicators (green check, yellow ~, red X) for GPU comparisons.

Performance Comparison Logic:
- Compared user GPU FPS vs. game requirements with 10% threshold for visual feedback.
- Showed publisher’s recommended GPU specs in a table.

Error and Loading Handling:
- Displayed “Loading…” UI and error messages for failed API calls as taught in class.

---

### First Time Environment Setup

This project requires setting up both a backend with Django and a frontend with Node.js, React, and Vite. Follow these steps after cloning the repository:

#### Backend
Prerequisites:
* Python 3.12 or higher
* pip (Python package installer)
* A virtual environment (recommended)
* sqlite3

Setup:
1. Open a terminal window dedicated to backend operations
2. Navigate to the backend directory:   ```bash   cd Reminders/backend   ```
3. Set up a virtual environment and activate it. See the following for Mac/Unix like systems
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. Apply migrations and start the Django development server:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

#### Frontend 

Prerequisites:
- Node.js 18.x or higher
- npm (Node package manager, included with Node.js)
- Vite (bundled via npm install)

Setup
1. Open a separate terminal for frontend operations
2. Navigate to the frontend directory:
   ```bash
   cd Reminders/frontend
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start the frontend development server:
   ```bash
   npm run dev
   ```
---

### Usage Instructions

Access the application at [http://localhost:5173](http://localhost:5173)

1. **Select GPU Hardware**:
   - Select a GPU Manufacturer and GPU Model from the Your Setup table

2. **Add Reminders**:
   - Select a Game and a Game Hardware Specification from the Game table

3. **Review Findings**:
   - Review the Compatibility Check table for runtime graphics card configurations that do and do not meet specifications made by the game publisher
   - Review the Game Publisher's Suggestion table for the GPU card the publisher recommends

---

### Known Issues & Future Enhancements
 
Features:
1. Implement React Query
2. Add Test Coverage

Functionality:
1. Add User input for Display Resolution, and CPU 
2. Add support for cpu gpu bottleneck warnings
3. Game compatibility more nuanced than a number
4. A search function that identifies a prebuilt pc to match user needs---

---
 
## Contacts 
- Matthew Kruse
 
To suggest a feature or submit an issue, [use this link](https://github.com/mattk6/Custom-Prebuilts/issues)
