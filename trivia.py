from console import clear_console, format_text, print_heading

import json
import random

LETTERS = ['a', 'b', 'c', 'd', 'e'] # letters for question numbering
COLORS = ['magenta', 'blue', 'cyan', 'green', 'red'] # order for options to be colored

def get_questions(filename):

    with open(filename) as file:
        return json.load(file)

def randomize_choices(question):
    questions = question['incorrect']
    questions.append(question['correct'])
    random.shuffle(questions)
    return questions

def print_question(question, question_number, current_score):
    """Should not be called directly. \n
    Print a question and its options, return the correct choice and the order of choices."""

    clear_console()
    print_heading(current_score)

    print(format_text(f'{question_number+1}: {question["question"]}', color='orange', bold=True))
    print() # line
    choice_order = randomize_choices(question)
    for i, option in enumerate(choice_order):
        print(format_text(f'{LETTERS[i]} : {option}', COLORS[i]))

    print()

    return question['correct'], choice_order

def ask_question(question, question_number, current_score):
    """Print the question, take user's input, and then notify if they are right. Return True if correct."""

    correct, choice_order = print_question(question, question_number, current_score)
    choice = input('Your choice: ')

    while len(choice) != 1 or choice not in LETTERS or LETTERS.index(choice) > len(choice_order):
        print('Enter a valid letter.')
        choice = input('Your choice: ') # if user doesn't enter a valid choice, ask again

    if choice_order[LETTERS.index(choice)] == correct: # get the actual choice, not just the letter, and compare it
        print(format_text('Correct! +1\n', 'green', bold=True))
        input('Press any key to move to the next question.')
        return True
    else:
        print(format_text('Incorrect.', 'red', bold=True))
        print(f'The correct choice was {format_text(correct, color="green", bold=True)}\n')
        input('Press any key to move to the next question.')
        return False

if __name__ == "__main__":

    questions = get_questions('questions.json')
    question_order = random.sample(range(len(questions)), 10) # create a random order of questions

    score = 0 # store the user's score for printing
    for i, question_number in enumerate(question_order):
        if ask_question(questions[question_number], i, score):
            score += 1

    clear_console()
    print(format_text('Thanks for playing!\n', 'orange'))
    print(format_text(f'Final Score: {format_text(score, "cyan")} out of 10\n', bold=True))
    input('Press any key to exit.')