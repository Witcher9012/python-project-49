from brain_games.cli import welcome_user
import prompt

MAX_ROUNDS = 3


def run_game(game_name):
    print("Welcome to the Brain Games!")
    welcome_user()
    print(game_name.DESCRIPTION)
    round_number = 1
    while round_number <= MAX_ROUNDS:
        question, correct_answer = game_name.make_question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if not (user_answer == correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {user_name}!")
            return
        print("Correct!")
        round_number += 1