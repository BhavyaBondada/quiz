def quiz_game():
    # List of questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which programming language is known as the language of AI?",
            "options": ["A) Java", "B) Python", "C) C++", "D) Ruby"],
            "answer": "B"
        },
        {
            "question": "What is 5 + 3?",
            "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
            "answer": "C"
        }
    ]

    print("Welcome to the Quiz Game!")
    score = 0

    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}: {question['question']}")
        for option in question["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")

    print(f"\nYour final score is {score}/{len(questions)}.")
    if score == len(questions):
        print("Excellent! You got all the answers right!")
    elif score > len(questions) // 2:
        print("Good job! Keep practicing to improve further.")
    else:
        print("Better luck next time! Study and try again.")
if __name__=="__main__":
    quiz_game()


