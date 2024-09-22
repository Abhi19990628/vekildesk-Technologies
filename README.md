# Technical Assessment Test

Welcome to the Technical Assessment Test repository! This project contains solutions to a series of programming tasks that assess proficiency in Python and the Django framework.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Solutions](#solutions)
- [License](#license)
  

## Overview

This assessment evaluates foundational knowledge in Python programming and Django through practical problem-solving. Each question is designed to test different skills, from web scraping to data processing and API development.

## Project Structure

```
PROJECT/
│
├── src/
│   ├── task3_django_app/    # Django application for Task 3
│   ├── task1_web_scraper.py
│   ├── task2_csv_processor.py
│   ├── task4_rate_limiter.py
│   ├── task5_aggregate_data.py
│   ├── task6_duplicate.py
│   └── user_data.csv        # CSV file for data processing tasks
│
├── .gitignore
└── requirements.txt         # Project dependencies
```

## Requirements

- Python 3.x
- Django 3.x or higher
- BeautifulSoup4
- Requests
- Pandas


## Running the Tasks

### Task 1: Web Scraper
```
python src/Q1_web_scraping.py
```

### Task 2: CSV Processor
```
python src/Q2_csv_data_cleaning.py
```


### Task 3: Django App

Install the required packages using:

```bash
pip install -r requirements.txt
```
Clone the repository:
```bash
https://github.com/Abhi19990628/vekildesk-Technologies.git
```

Navigate to the project directory:
```bash
cd your-repository-name
```

(Optional) Create and activate a virtual environment:
```bash
pip install virtualenv
virtualenv and name for env for example:- (Env)
cd Env/scripts/./activate
```
Install the dependencies:
```bash
pip install -r requirements.txt
```

Run database migrations:
```bash
python manage.py migrate
```

Start the development server:
```bash
python manage.py runserver
```




### Task 4: Rate Limiter
```
python src/Q4_rate_limiter.py
```

### Task 5: Data Aggregator
```
python src/Q5_data_aggregation.py
```

### Task 6: Duplicate Handler
```
python src/Q6_find_duplicate.py
```

## Task Descriptions

### Task 1: Web Scraper
A Python script that scrapes news headlines from a specified news website.

### Task 2: CSV Processor
A script that processes the user_data.csv file, performing data manipulation and analysis.

### Task 3: Django App
A Django application that implements a specific functionality (details to be added).

### Task 4: Rate Limiter
A Python implementation of a rate limiting algorithm.

### Task 5: Data Aggregator
A script that aggregates and analyzes data from multiple sources.

### Task 6: Duplicate Handler
A script that identifies and handles duplicate data entries.

## Additional Notes

- Ensure you have Python 3.7+ installed on your system.
- The `user_data.csv` file in the `src/` directory is used for data processing tasks. Ensure it's present and correctly formatted before running related scripts.
- The `.vscode/` directory contains VS Code specific settings. You can ignore this if you're using a different IDE.
- If you encounter any issues with the Django app, make sure you've applied all necessary migrations and that the database is properly set up.
-Feel free to modify or expand any sections** to better reflect your work or additional features.

This structure should help present your project clearly and attractively! Let me know if you need further customization.
