# Data Redundancy Removal System

## CodeAlpha Cloud Computing Internship - Task 1

A Python-based system that identifies and prevents redundant data
from being added to a database, ensuring data accuracy and efficiency.

## Features
- Validates new data entries against existing records before insertion
- Detects and blocks duplicate/redundant entries (case-insensitive email check)
- Appends only unique, verified data to the database
- Prevents false positives from entering the cloud database

## Tech Stack
- Python 3
- SQLite (simulating a cloud database)

## How to Run

python3 app.py

## Sample Output
The system automatically tests with sample data, then lets the user
interactively add and validate new entries in real time.
