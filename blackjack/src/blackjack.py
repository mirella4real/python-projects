import random
import art
import strings

def init():
    want_to_play = input(f"{strings.invitation_to_play} \n").lower()
    if want_to_play == 'y':
        print(art.blackjack)
        start_game()
    elif want_to_play == 'n':
        end_game()
    else:
        init(strings, art)

def get_cards_and_score(turn, hand):
    if 11 in hand["cards"] and sum(hand["cards"]) > 21:
        hand["cards"].remove(11)
        hand["cards"].append(1)
    revealed_cards = "[ "
    for index, card in enumerate(hand["cards"]):
        if index == len(hand["cards"])-1:
            if turn == "player" and hand["id"] != "player":
                revealed_cards += "? ]"
            else:
                revealed_cards += f"{card} ]"
        else:
            revealed_cards += f"{card}, "
    hand["cards_string"] = revealed_cards
    hand["score"] = sum(hand["cards"])
    return(hand)

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def init_player(player):
    new_hand = {
        "id": player,
        "cards": [],
        "cards_string": "",
        "score": 0,
    }
    return new_hand

def get_game_state(game, player, dealer):
    if game["turn"] == "player":
        if player["score"] == 21 and len(player["cards"]) == 2:
            game["isOver"] = True
            game["reason"] = "Blackjack"
            game["winner"] = player
            game["loser"] = dealer
        elif player["score"] > 21:
            game["isOver"] = True
            game["reason"] = "Over21"
            game["winner"] = dealer
            game["loser"] = player
    else:
        if dealer["score"] == 21 and len(dealer["cards"]) == 2:
            game["isOver"] = True
            game["reason"] = "Blackjack"
            game["winner"] = dealer
            game["loser"] = player
        elif dealer["score"] > 21:
            game["isOver"] = True
            game["reason"] = "Over21"
            game["winner"] = player
            game["loser"] = dealer
        else:
            if dealer["score"] > 16:
                if dealer["score"] > player["score"]:
                    game["isOver"] = True
                    game["reason"] = "HighScore"
                    game["winner"] = dealer
                    game["loser"] = player
                elif dealer["score"] < player["score"]:
                    game["isOver"] = True
                    game["reason"] = "HighScore"
                    game["winner"] = player
                    game["loser"] = dealer
                else:
                    game["isOver"] = True
                    game["reason"] = "Draw"
    return game

def game_over(game_state):
    winner = game_state["winner"]
    loser = game_state["loser"]
    if game_state["reason"] == "Draw":
        print(f"   {strings.you_draw}")
    elif game_state["reason"] == "Over21":
        if winner["id"] == "player":
            print(f"   {strings.dealer_went_over}")
        else:
            print(f"   {strings.you_went_over}")
    elif game_state["reason"] == "Blackjack":
        if winner["id"] == "player":
            print(f"   {strings.you_won_with_blackjack}")
        else:
            print(f"   {strings.dealer_won_with_blackjack}")
    else:
        if winner["id"] == "player":
            print(f"   {strings.you_win}")
        else:
            print(f"   {strings.you_lose}")
    print("\n\n")

def end_game():
    print("\n" * 20)
    print(strings.declines_invitation_response)
    print("\n\n")

def start_game():
    game_state = {
        "turn": "player",
        "isOver": False,
        "reason": "",
        "winner": {},
        "loser": {}
    }
    take_a_card = "n"
    player_hand = init_player("player")
    dealer_hand = init_player("dealer")
    # initial deal - player's turn
    while len(player_hand["cards"]) < 2:
        player_hand["cards"].append(deal_card())
        dealer_hand["cards"].append(deal_card())
    # first check - player's turn
    player_hand = get_cards_and_score(game_state["turn"], player_hand)
    dealer_hand = get_cards_and_score(game_state["turn"], dealer_hand)
    game_state = get_game_state(game_state, player_hand, dealer_hand)

    if game_state["isOver"] == False:
        print(f"{strings.game_start}\n")
        print(f"   {strings.your_cards}        {player_hand['cards_string']} {strings.current_score} {player_hand['score']}")
        print(f"   {strings.dealers_card} {dealer_hand['cards_string']}\n")
        take_a_card = input(f"{strings.new_card_or_pass}\n").lower()
    
    while game_state["isOver"] == False and take_a_card == 'y':
        player_hand["cards"].append(deal_card())
        player_hand = get_cards_and_score(game_state["turn"], player_hand)
        game_state = get_game_state(game_state, player_hand, dealer_hand)
        if game_state["isOver"] == False:
            print(f"   {strings.your_cards}        {player_hand['cards_string']} {strings.current_score} {player_hand['score']}")
            print(f"   {strings.dealers_card} {dealer_hand['cards_string']}\n")
            take_a_card = input(f"{strings.new_card_or_pass}\n").lower()
            
    if game_state["isOver"] == False:
        game_state["turn"] = "dealer"
        while game_state["isOver"] == False:
            dealer_hand["cards"].append(deal_card())
            dealer_hand = get_cards_and_score(game_state["turn"], dealer_hand)
            game_state = get_game_state(game_state, player_hand, dealer_hand)
    
    if game_state["isOver"] == True:
        print(f"   {strings.your_cards}        {player_hand['cards_string']} {strings.current_score} {player_hand['score']}")
        print(f"   {strings.dealers_card} {dealer_hand['cards_string']} {strings.dealer_score} {dealer_hand['score']}\n")
        game_over(game_state)
        init()

init()