print("=" * 50)
print("          PYTHON QUIZ APPLICATION")
print("=" * 50)

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. create", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data type stores multiple values?",
        "options": ["A. int", "B. list", "C. float", "D. bool"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "Which loop repeats while a condition is True?",
        "options": ["A. for", "B. repeat", "C. while", "D. loop"],
        "answer": "C"
    }
]

while True:

    print("\nChoose an option:")
    print("1. Start Quiz")
    print("2. View Rules")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":

        while True:

            score = 0
            wrong = 0

            print("\nStarting Quiz...\n")

            for i, q in enumerate(questions, start=1):

                print("=" * 50)
                print(f"Question {i}")
                print(q["question"])

                for option in q["options"]:
                    print(option)

                answer = input("\nYour Answer (A/B/C/D): ").strip().upper()

                if answer == q["answer"]:

                    print("\n✅ Correct!\n")
                    score += 1

                else:

                    print(f"\n❌ Wrong!")
                    print(f"Correct Answer : {q['answer']}\n")
                    wrong += 1

            percentage = (score / len(questions)) * 100

            if percentage >= 90:
                grade = "A+"
                remark = "Outstanding!"
            elif percentage >= 80:
                grade = "A"
                remark = "Excellent!"
            elif percentage >= 70:
                grade = "B"
                remark = "Very Good!"
            elif percentage >= 60:
                grade = "C"
                remark = "Good!"
            elif percentage >= 50:
                grade = "D"
                remark = "Needs Improvement."
            else:
                grade = "F"
                remark = "Keep Practicing!"

            print("=" * 50)
            print("             QUIZ RESULT")
            print("=" * 50)

            print(f"Correct Answers : {score}")
            print(f"Wrong Answers   : {wrong}")
            print(f"Final Score     : {score}/{len(questions)}")
            print(f"Percentage      : {percentage:.2f}%")
            print(f"Grade           : {grade}")
            print(f"Remark          : {remark}")

            print("=" * 50)

            again = input("\nPlay Again? (Y/N): ").strip().upper()

            if again != "Y":
                break

    elif choice == "2":

        print("\nQUIZ RULES")
        print("-" * 40)
        print("1. Each correct answer = 1 mark")
        print("2. No negative marking")
        print("3. Type A, B, C or D")
        print("4. Percentage will be calculated")
        print("5. Grade will be displayed")
        print("6. You can play multiple times")

    elif choice == "3":

        print("\nThank you for playing!")
        break

    else:

        print("\n❌ Invalid choice!")