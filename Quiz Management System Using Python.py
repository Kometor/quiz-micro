"""
Quiz Management System
A simple program to add questions, conduct quizzes
and check the scores of previous attempts.
"""

from datetime import datetime

DATA_FILE = "questions.txt"
SCORE_FILE = "scores.txt"


# Sample questions for the first time the program runs
def default_questions():
    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "def", "fun", "define"],
            "answer": 1
        },
        {
            "question": "What does the input() function return?",
            "options": ["A string", "An integer always", "A list", "Nothing"],
            "answer": 0
        },
        {
            "question": "Which symbol is used to write a comment in Python?",
            "options": ["//", "#", "/* */", "--"],
            "answer": 1
        },
        {
            "question": "What is the index of the first item in a list?",
            "options": ["1", "0", "-1", "2"],
            "answer": 1
        },
        {
            "question": "Which loop runs as long as a condition is true?",
            "options": ["for", "switch", "while", "repeat"],
            "answer": 2
        }
    ]

    return questions


# Read questions from the file
def load_questions():
    try:
        file = open(DATA_FILE, "r")
        data = file.read()
        file.close()
    except FileNotFoundError:
        return None

    questions = []

    if data.strip() == "":
        return questions

    blocks = data.strip().split("\n---\n")

    for block in blocks:
        lines = block.split("\n")

        if len(lines) == 3:
            question = lines[0]
            options = lines[1].split("|")

            if len(options) == 4 and lines[2] in ["0", "1", "2", "3"]:
                answer = int(lines[2])

                q = {
                    "question": question,
                    "options": options,
                    "answer": answer
                }

                questions.append(q)

    return questions


# Save questions in the file
def save_questions(questions):
    file = open(DATA_FILE, "w")

    for q in questions:
        file.write(q["question"] + "\n")
        file.write("|".join(q["options"]) + "\n")
        file.write(str(q["answer"]))

        if q != questions[-1]:
            file.write("\n---\n")

    file.close()


# Add a new question
def add_question(questions):
    print("\n--- Add New Question ---")

    question = input("Enter the question: ").strip()

    if question == "" or "|" in question:
        print("Invalid question.")
        return

    options = []

    for i in range(4):
        option = input("Enter option " + str(i + 1) + ": ").strip()

        if option == "" or "|" in option:
            print("Invalid option. Question not added.")
            return

        options.append(option)

    while True:
        correct = input("Enter the correct option number (1-4): ")

        if correct in ["1", "2", "3", "4"]:
            break

        print("Please enter a number between 1 and 4.")

    q = {
        "question": question,
        "options": options,
        "answer": int(correct) - 1
    }

    questions.append(q)
    save_questions(questions)

    print("Question added successfully!")


# Display all questions
def view_questions(questions):
    print("\n--- All Questions ---")

    if len(questions) == 0:
        print("No questions available.")
        return

    labels = ["A", "B", "C", "D"]

    for i in range(len(questions)):
        q = questions[i]

        print("\nQ" + str(i + 1) + ". " + q["question"])

        for j in range(4):
            print(labels[j] + ". " + q["options"][j])

    choice = input("\nEnter question number to delete (or press Enter to go back): ")

    if choice == "":
        return

    if not choice.isdigit():
        print("Invalid input.")
        return

    number = int(choice)

    if number < 1 or number > len(questions):
        print("Question not found.")
        return

    removed = questions.pop(number - 1)
    save_questions(questions)

    print("Question removed:", removed["question"])


# Calculate and display the result
def evaluate_score(score, total):
    if total == 0:
        percentage = 0
    else:
        percentage = (score / total) * 100

    if percentage >= 80:
        grade = "Excellent"
    elif percentage >= 60:
        grade = "Good"
    elif percentage >= 40:
        grade = "Average"
    else:
        grade = "Needs Improvement"

    print("\n========== Quiz Result ==========")
    print("Correct Answers:", score, "/", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Result:", grade)
    print("=================================")

    return percentage, grade


# Save the quiz result in a file
def save_score(score, total, percentage, grade):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    file = open(SCORE_FILE, "a")
    file.write(
        date + "|" + str(score) + "/" + str(total)
        + "|" + str(round(percentage, 2))
        + "|" + grade + "\n"
    )
    file.close()


# Start the quiz
def take_quiz(questions):
    print("\n--- Start Quiz ---")

    if len(questions) == 0:
        print("No questions available. Please add some questions first.")
        return

    score = 0
    total = len(questions)

    for i in range(total):
        q = questions[i]

        print("\nQuestion", i + 1, "of", total)
        print(q["question"])

        for j in range(4):
            print(str(j + 1) + ".", q["options"][j])

        while True:
            answer = input("Enter your answer (1-4): ")

            if answer in ["1", "2", "3", "4"]:
                break

            print("Invalid choice. Try again.")

        if int(answer) - 1 == q["answer"]:
            print("Correct answer!")
            score = score + 1
        else:
            correct_answer = q["options"][q["answer"]]
            print("Wrong answer.")
            print("Correct answer:", correct_answer)

    percentage, grade = evaluate_score(score, total)
    save_score(score, total, percentage, grade)

    print("Your result has been saved.")


# Display previous quiz results
def view_history():
    print("\n--- Score History ---")

    try:
        file = open(SCORE_FILE, "r")
        records = file.readlines()
        file.close()
    except FileNotFoundError:
        print("No quiz history found.")
        return

    if len(records) == 0:
        print("No quiz history found.")
        return

    count = 1

    for record in records:
        parts = record.strip().split("|")

        if len(parts) == 4:
            print("\nQuiz", count)
            print("Date:", parts[0])
            print("Score:", parts[1])
            print("Percentage:", parts[2], "%")
            print("Grade:", parts[3])

            count = count + 1

    if count == 1:
        print("No quiz history found.")


# Main menu
def show_menu():
    print("\n========== Quiz Management System ==========")
    print("1. Add New Question")
    print("2. View All Questions")
    print("3. Start Quiz")
    print("4. View Score History")
    print("5. Exit")
    print("============================================")


# Main function
def main():
    print("Welcome to the Quiz Management System!")

    questions = load_questions()

    if questions is None:
        questions = default_questions()
        save_questions(questions)
        print("Sample questions have been added.")
    else:
        print(len(questions), "questions loaded successfully.")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_question(questions)

        elif choice == "2":
            view_questions(questions)

        elif choice == "3":
            take_quiz(questions)

        elif choice == "4":
            view_history()

        elif choice == "5":
            print("Thank you for using the Quiz Management System.")
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")


main()