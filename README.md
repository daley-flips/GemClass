# GemClass

GemClass is an AI-powered tutoring system that uses Google's Generative AI to provide personalized educational assistance. The system is designed to guide students through their learning process without simply giving away answers, encouraging critical thinking and deep understanding. Made by Sebastian Castro (sec204@pitt.edu) and Daley Fraser (drf58@pitt.edu)

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Setup Instructions](#setup-instructions)
6. [Usage](#usage)
7. [Customization](#customization)
8. [Planned Updates](#planned-updates)

## Project Overview

GemClass is built to simulate a knowledgeable tutor that adapts to different courses and helps students learn effectively. It uses a chat-based interface where students can ask questions, and the AI responds with guidance, hints, and explanations tailored to the selected course.

## Features

- Course-specific AI tutoring
- General AI tutoring
- Chat-based interface for easy interaction
- Markdown support for formatted responses


## Technology Stack

- Backend: Python with Flask
- Frontend: HTML, CSS, JavaScript
- AI: Google's Generative AI (Gemini model)
- Markdown Parsing: Marked.js library

## Project Structure

```
gemclass/
│
├── app.py                 # Main Flask application
├── gemini_test.py         # Gemini API integration
├── frontend/
│   └── index.html         # Main HTML template
├── static/
│   └── steelhacker.png    # Logo image
└── class_data/
    ├── cs50.json          # Harvard CS50 course data
    └── cs447.json         # Pitt CS0447 course data
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gemclass.git
   cd gemclass
   ```

2. Install the required packages:
   ```
   pip install flask flask-cors google-generativeai
   ```

3. Set up Google Cloud credentials:
   - Create a Google Cloud project and enable the Generative AI API (follow instructions at `https://ai.google.dev/gemini-api/docs/quickstart`)
   - Download the JSON key file and set the path in `gemini_test.py`:
     ```python
     key_path = "/path/to/your/credentials.json"
     os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
     ```

5. Prepare course data:
   - Create JSON files in the `class_data` directory for each course you want to support
   - Follow the structure in existing `cs50.json` and `cs447.json` files

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000` or (if on windows) `http://localhost:5000`

3. Select a course from the dropdown menu

4. Start chatting with the AI tutor by typing your questions in the input box

## Customization

### Adding New Courses

1. Create a new JSON file in the `class_data` directory (e.g., `new_course.json`)
2. Follow the structure of existing course files:
   ```json
   {
     "lectures": [
       {"lecture": "1", "content": "Lecture content..."},
       ...
     ],
     "extra": [
       {"content": "Extra content..."},
       ...
     ]
   }
   ```
3. Update the `generate_text` function in `gemini_test.py` to include the new course

### Modifying AI Behavior

- Adjust the `system_prompt` in `gemini_test.py` to change the AI's personality or behavior
- Modify the `generation_config` and `safety_settings` in `gemini_test.py` to fine-tune the AI's responses


## Planned Updates

- Allow user to specifically choose from which specific lectures for each class the AI should base its answer off from (it currently uses every single lecture) 
- Reset functionality to start fresh conversations
- Streamlining process to make adding different classess more user-friendly
- Conversation history management

