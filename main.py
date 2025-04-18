import os
import random
from utils.game_utils import load_questions, ask_question, speak

DATA_DIR = "data"
SUBJECTS = {
    "1": "english_questions.json",
    "2": "math_questions.json",
    "3": "science_questions.json"
}

def select_subject():
    print("\n🎓 Welcome to your learning game!")
    speak("Welcome Rajvika and Trishika to your learning game!")
    speak("Use your keyboard to select a subject. Press 1 for English, 2 for Math, 3 for Science, or 9 to quit.")
    print("Choose a subject:")
    print("1. English")
    print("2. Math")
    print("3. Science")
    print("9. Quit")
    choice = input("Enter the number: ").strip()

    if choice == "9":
        print("Exiting the game. Goodbye!")
        speak("Exiting the game. Goodbye!")
        exit()

    return SUBJECTS.get(choice)

def ask_question_with_retry(question_data,score):
    attempt = 0
    max_attempts = 3
    correct_answers = [ans.lower() for ans in question_data["answers"]]
    
    while attempt < max_attempts:
        ask_question(question_data)
        user_answer = input("Your answer: ").strip().lower()

        if user_answer in correct_answers:
            print("🟢 Correct! Great Job!")
            speak("Your answer is absolutely correct! Awesome pawsome job!")
            score += 1
            return True
        else:
            attempt += 1
            if attempt < max_attempts:
                print(f"❌ Oh no! You are really close. This was an incorrect! You can try again. You have {max_attempts - attempt} attempt(s) left.")
                speak(f"Oh no! You are really close. This was an incorrect! You can try again. You have {max_attempts - attempt} attempt(s) left.")

    print(f"❌ The correct answer is: {correct_answers[0]}")
    speak(f"No problem! The correct answer is: {correct_answers[0]}")
    return False

def play_game():
    while True:
        subject_file = select_subject()
        if not subject_file:
            print("Invalid choice. Please try again.")
            continue

        path = os.path.join(DATA_DIR, subject_file)
        questions = load_questions(path)
        print(len(questions))
        random.shuffle(questions)

        speak("Let's begin!")
        score = 0
        for question_data in questions:  # Ask 5 random questions
            ask_question_with_retry(question_data,score)

        # Once all questions are done, go back to the main menu
        print("\nAll questions are finished! Returning to the main menu.")
        speak("Awesome job! You finished this section.")
        speak("You got {score} out of {len(questions)} questions correct.")

if __name__ == "__main__":
    play_game()
