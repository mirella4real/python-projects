import art
import strings

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def end_game(strings):
    print("\n" * 20)
    print(strings.declines_invitation_response)
    print("\n\n")

def start_game(strings):
    print("Game on")

def init(strings, art):
    want_to_play = input(f"{strings.invitation_to_play} \n").lower()
    if want_to_play == 'y':
        print(art.blackjack)
        start_game(strings)
    elif want_to_play == 'n':
        end_game(strings)
    else:
        int(strings, art)

init(strings, art)
