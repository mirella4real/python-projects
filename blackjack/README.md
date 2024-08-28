#Blackjack Project

- [sample game](https://games.washingtonpost.com/games/blackjack)

### Project Requirements

- The deck is unilimted in size
- There are no jokers
- The Jack/Queen/King all count as 10
- The Ace an count as 11 or 1
- The cards in the list have equal probability of being drawn
- The computer is the dealer

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

### Rules of play
- Add cards to the largest number without going over 21
- If cards in a player's hand add up to over 21, it is called a bust and they lose IMMEDIATELY
- After each action cards are added
- Dealer deals 1 card each, both revealed
- Dealer deals 2nd card, but theirs is hidden
- Player can ask for another card or pass
- If ask for another card, cards are added to continue
- If pass, the deler reveals their card
- If the dealer ends up with a hand that is less than 17, they must take another card

### Logic

- Choice: display invitation to play with y or n choices
- Select n -> game ends, display message
- Select y ->
    - print art
    - randomly deal cards, 2 each and add player total
    - print player's cards and current score (CHECK for 21, automatic win)
    - print computer's cards (show only one) and current score
    - Choice 'y' to get another card, 'n' to pass
    - Select y ->
        - Get random card
        - Add and check score
        - if < 21, get choice of another card or pass

    - Select n ->
        - Dealer reveals hidden card and adds
        - if dealer is under 17, draw and add
        - If dealer is over 17, CHECK calculate scores and select winner
        - display final hands 
        - display player message
        - display choice to play again


        ((( CHECK)))
        - Running check
        - If player score is 21, player wins
        - Final check
        - If player and dealer === this is a draw
        - If player final hand > 21, player loses 
        - If dealer final hand > 21, player wins
        - If player final hand <= 21 and > than dealer, player wins
        - If dealer final hand <= 21 and > than player, dealer wins





