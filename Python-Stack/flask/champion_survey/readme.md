# Champion Survey - Flask Application

## Overview

A simple web application built with Flask that collects user input through a form and displays the submitted data on a result page.

## Features

- Collect user name
- Select dojo location
- Choose favorite programming language
- Optional comment input
- Display submitted data on a separate result page
- Styled using Bootstrap and custom CSS

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5

## Project Structure

```

project/
│
├── server.py
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── index.css
│   └── result.css

```

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   ```

````

2. Navigate to the project directory:

   ```bash
   cd project
   ```
3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
4. Activate the environment:

   * macOS/Linux:

     ```bash
     source venv/bin/activate
     ```
   * Windows:

     ```bash
     venv\Scripts\activate
     ```
5. Install dependencies:

   ```bash
   pip install flask
   ```

## Running the Application

```bash
python server.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

## Usage

* Fill out the form on the home page
* Click the "Result" button
* View submitted data on the result page

## Routes

* `/` → Displays the survey form
* `/result` → Handles form submission and displays results

## Notes

* Form submission uses POST method
* Data is accessed via `request.form`
* Basic validation is handled using HTML attributes

## License

This project is for educational purposes.
````
