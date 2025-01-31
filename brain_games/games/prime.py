from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        false
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            false
    return true


def make_question_and_correct_answer():
    min_number = 1
    max_number = 21
    number = randint(min_number, max_number)
    question = str(number)
    return question, is_prime(number)