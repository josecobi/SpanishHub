# SpanishHub - Learn Spanish Verb Forms

Welcome to SpanishHub, a web application designed to help you boost your Spanish language skills by practicing verb forms! This web app is built using Flask, HTML, JavaScript, CSS, and utilizes an SQLite database to store questions and answers. Whether you're a beginner or looking to refine your language skills, SpanishHub is your go-to destination for practicing verb forms in an interactive way.


## Table of Contents

- [Features](#features)
- [How Flask Powers SpanishHub](#how-flask-powers-spanishhub)
- [Asynchronous Data Fetching](#asynchronous-data-fetching)
- [Getting Started](#getting-started)

- [Installation](#installation)
- [License](#license)
- [Contact Information](#contact-information)

## Features

### Practice Verb Forms
SpanishHub offers a user-friendly interface to practice verb forms in different tenses. Users can choose from various tenses such as Present, Present Stem-Changing, and Preterit, all while avoiding the complexities of grammar jargon.

### Drag-and-Drop or Tap
We understand that not all devices have drag-and-drop capabilities, so I've made SpanishHub accessible to all devices. Users can either drag and drop the correct verb form or simply tap the correct choice to fill in the blanks.

### Real-Time Feedback
Get immediate feedback on your answers. SpanishHub lets you know if you've answered correctly. It also calculates your score and displays it at the end of the quiz, motivating you to improve with each practice session.

### Change Answers on the Fly
Don't worry if you change your mind before submitting your answer. SpanishHub allows you to change your answers before submitting them for scoring, providing a dynamic learning experience.

## How Flask Powers SpanishHub

SpanishHub leverages Flask, a lightweight Python web framework, to handle the server-side logic and serve the web application to users. Here's how Flask is used in this app:

1. **Routing**: Flask is used to define the app's routes, such as the homepage ("/") and routes for different tenses ("/tenses/<tense>"). These routes determine what content is displayed to the user.

2. **Database Interaction**: Flask interacts with an SQLite database to retrieve questions and answer choices for each selected tense. It uses SQLite queries to fetch the necessary data and serve it to the front end.

3. **Session Management**: Flask manages user sessions, ensuring that data is kept secure and accessible only to authorized users. The app's secret key is generated for session security.

4. **Rendering Templates**: Flask renders HTML templates using Jinja2 templating engine. These templates define the structure of web pages, making it easy to maintain a consistent design across the app.

## Asynchronous Data Fetching

SpanishHub uses asynchronous JavaScript and the Fetch API to dynamically load quiz data without refreshing the entire page. Here's how it works:

1. **Event Listeners**: JavaScript event listeners are used to detect user actions, such as selecting a tense or clicking the start button.

2. **Asynchronous Fetch**: When a user selects a tense or starts a quiz, JavaScript asynchronously fetches data from the server without causing the page to reload. The Fetch API sends an HTTP request to the Flask backend to retrieve questions and answer choices.

3. **Real-Time Updates**: The fetched data is dynamically updated on the page, allowing users to interact with the quiz seamlessly.

By using asynchronous data fetching, SpanishHub delivers a smooth and responsive user experience, making learning Spanish verb forms enjoyable and effective.

# Files and Design Choices

### Project Files

- **app.py**: This is the core of the web application, built using the Flask framework. It handles routing, database interactions, and session management.

- **/static/js/verbsMultChoiceQuiz.js**: This JavaScript file is responsible for fetching questions and answers asynchronously, displaying them using query selectors, providing feedback, and rewarding points to users. It plays a crucial role in creating a responsive and interactive user experience.

- **/templates/layout.html**: This HTML template serves as the main page structure and is extended by other pages. I also created specific templates, including:

  - **/templates/index.html**: The landing page template.
  
  - **/templates/verbsMultChoiceQuiz.html**: This template contains the boilerplate code for the web app, including the interface for practicing verb forms.

### Design Choices

- **Bootstrap**: I used Bootstrap for the basic design elements, providing a responsive and visually appealing layout.

- **Custom Styles**: I created custom styles for most of the elements in the /templates/verbsMultChoiceQuiz.html template. This customization adds a unique and personalized touch to the design.

- **Hero Section Image**: The captivating image used in the hero section of the web app (index.html) is credited to Thomas Park and was downloaded from [Unsplash](https://unsplash.com). It enhances the visual appeal of the landing page.

My design choices and file organization reflect the attention to detail and dedication to creating an engaging learning experience for users.

## Getting Started

To start using SpanishHub, simply clone this repository and follow the setup instructions in the [Installation](#installation) section below. You'll be practicing Spanish verb forms in no time!

## Installation

To run SpanishHub locally, follow these steps:

1. Clone the repository to your local machine using your terminal/shell:

   git clone https://github.com/your-username/spanish-hub.git

## Open your terminal/command window and navigate to the project directory:

cd spanish-hub

## Create a virtual environment (recommended):

`python -m venv venv`

## Activate the virtual environment:

**On macOS and Linux**:

`source venv/bin/activate`

**On Windows (PowerShell)**:

`.\venv\Scripts\Activate.ps1`

**Install the required dependencies:**

`pip install -r requirements.txt`

**Run the Flask app:**

`python app.py`

Open your web browser and navigate to http://localhost:5000 to start practicing Spanish verb forms.`


## License

Copyright <2023> <Jose Lopez Cobano "CobiDev">

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

## Contact Information

cobitremolo@gmail.com
