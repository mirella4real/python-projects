import random
import strings
import art 
import gamedata

def get_game_data(game):
    if len(game) == 0:
        game['a'] = random.choice(gamedata.data)
    game['b'] = random.choice(gamedata.data)
    if game['a']['name'] == game['b']['name']:
        get_game_data(game)
    else:
        return game

def get_correct_answer(game):
    if game['a']['follower_count'] > game['b']['follower_count']:
        return 'a'
    else:
        return 'b'

def play_game():
    correct_guess = True
    game = {}
    while correct_guess == True:
        game = get_game_data(game)
        if "score" not in game:
            game['score'] = 0
        else:
            print("\n" * 5)
            print(f"{strings.correct_answer} {strings.current_score} {game['score']}")        

        choice_a = f"{strings.compare_a} "
        choice_a += f"{game['a']['name']}, {game['a']['description']}, from {game['a']['country']}."
       
        choice_b = f"{strings.against_b} "
        choice_b += f"{game['b']['name']}, {game['b']['description']}, from {game['b']['country']}."
        
        print(choice_a)
        print("vs")
        print(choice_b)
        print("\n")

        guess = input(f"{strings.ask_for_guess}\n").lower()

        if guess == 'a' or guess == 'b':
            higher = get_correct_answer(game)
            if guess == higher:
                game['a'] = game[guess]
                game['score'] = game['score']+ 1
                correct_guess = True
            else:
                print(f"{strings.wrong_answer} {strings.final_score} {game['score']}")
                correct_guess = False
        else:
            print(strings.wrong_answer)
            correct_guess = False

def init():
    print(art.logo)
    has_lost = False
    while has_lost == False:
        has_lost = play_game()
    
init()