# Quiz Management System

A simple Python console program to add quiz questions, take quizzes, and view past scores.

## Features

- Add new questions (4 options each)
- View all questions and delete any
- Take a quiz and see immediate feedback
- View score history with date, percentage, and grade
- Sample questions are added automatically on first run

## Requirements

- Python 3

## How to Run

1. Save the program as `quiz.py` (or any name)
2. Open a terminal in the same folder
3. Run:
   ```
   python quiz.py
   ```

## Data Files

The program creates these files automatically:

| File            | Purpose                          |
|-----------------|----------------------------------|
| `questions.txt` | Stores all quiz questions        |
| `scores.txt`    | Stores past quiz results         |

## Menu Options

1. **Add New Question** – Enter a question and 4 options
2. **View All Questions** – See all questions (option to delete)
3. **Start Quiz** – Answer questions one by one
4. **View Score History** – See previous attempts
5. **Exit**
