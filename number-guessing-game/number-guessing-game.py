import strings
import random

LOW_GUESS = "low"
HIGH_GUESS = "high"
CORRECT_GUESS = "guessed"

level_of_difficulty  = {
    "easy": 10,
    "hard": 5,
    "NA": 1,
}

def getNumberOfTries(difficulty):
    selection = input(f"{strings.prompt_difficulty}\n").lower()
    tries = 0
    if selection == "easy":
        tries = difficulty["easy"]
    elif selection == "hard":
        tries = difficulty["hard"]
    else:
        tries = difficulty["NA"]

    return tries

def get_attempts_remaining_message(tries):
    message = f"\n{strings.you_have}"
    message += f" {tries} "
    if tries > 1:
        message += f" {strings.attempts} {strings.remaining}"
    else:
        message += f" {strings.attempt} {strings.remaining}"
    return message

def validate_guess(guess, secret):
    if guess > secret:
        return HIGH_GUESS
    elif guess < secret:
        return LOW_GUESS
    else:
        return CORRECT_GUESS
    
def get_attempt_result_message(attempt):
    message = ""
    if attempt == HIGH_GUESS:
        message = strings.too_high
    elif attempt == LOW_GUESS:
        message = strings.too_low
    return message

def play_game():
    turns = getNumberOfTries(level_of_difficulty)
    secret_number = random.randint(1, 100)
    while turns >0:
        print(get_attempts_remaining_message(turns))
        guess = input(f"{strings.prompt_guess} ")
        attempt = validate_guess(int(guess), secret_number)
        if attempt != CORRECT_GUESS:
            print(get_attempt_result_message(attempt))
            turns = turns -1
        else:
            break   
    if attempt == CORRECT_GUESS:
        print(strings.result_won)
    else:
        print(strings.result_lost)
    print(f"{strings.reveal_number} {secret_number}")

def init():
    print("\n"* 3)
    print(strings.welcome_message1)
    print(strings.welcome_message2)
    play_game()

init()
