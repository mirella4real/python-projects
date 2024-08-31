import unittest

from blackjack import get_game_state

class TestGetGameState(unittest.TestCase):

    def test_player_blackjack(self):
        game = {
            "turn": "player",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        player = {
            "id": "player",
            "cards": [10, 11],
            "cards_string": "[10, 11]",
            "score": 21,
        } 
        dealer = {
            "id": "dealer",
            "cards": [2, 2],
            "cards_string": "[2, 2]",
            "score": 4,
        } 
        expected_game_state = {
            "turn": "player",
            "isOver": True,
            "reason": "Blackjack",
            "winner": player,
            "loser": dealer,
        }
        self.assertEqual(get_game_state(game, player, dealer), expected_game_state)

    def test_player_over21(self):
        game = {
            "turn": "player",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        player = {
            "id": "player",
            "cards": [10, 11, 3],
            "cards_string": "[10, 11, 3]",
            "score": 24,
        } 
        dealer = {
            "id": "dealer",
            "cards": [2, 2],
            "cards_string": "[2, 2]",
            "score": 4,
        } 
        expected_game_state = {
            "turn": "player",
            "isOver": True,
            "reason": "Over21",
            "winner": dealer,
            "loser": player,
        }
        self.assertEqual(get_game_state(game, player, dealer), expected_game_state)  

    def test_player_canPlayAgain(self):
        game = {
            "turn": "player",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        player = {
            "id": "player",
            "cards": [10, 4, 3],
            "cards_string": "[10, 4, 3]",
            "score": 17,
        } 
        dealer = {
            "id": "dealer",
            "cards": [2, 2],
            "cards_string": "[2, 2]",
            "score": 4,
        } 
        expected_game_state = {
            "turn": "player",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        self.assertEqual(get_game_state(game, player, dealer), expected_game_state) 

    def test_dealer_blackjack(self):
        game = {
            "turn": "dealer",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        player = {
            "id": "player",
            "cards": [10, 3],
            "cards_string": "[10, 3]",
            "score": 13,
        } 
        dealer = {
            "id": "dealer",
            "cards": [10, 11],
            "cards_string": "[10, 11]",
            "score": 21,
        } 
        expected_game_state = {
            "turn": "dealer",
            "isOver": True,
            "reason": "Blackjack",
            "winner": dealer,
            "loser": player,
        }
        self.assertEqual(get_game_state(game, player, dealer), expected_game_state)  

    def test_dealer_over21(self):
        game = {
            "turn": "dealer",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        player = {
            "id": "player",
            "cards": [10, 3],
            "cards_string": "[10, 3]",
            "score": 13,
        } 
        dealer = {
            "id": "dealer",
            "cards": [10, 11, 4],
            "cards_string": "[10, 11, 4]",
            "score": 25,
        } 
        expected_game_state = {
            "turn": "dealer",
            "isOver": True,
            "reason": "Over21",
            "winner": player,
            "loser": dealer,
        }
        self.assertEqual(get_game_state(game, player, dealer), expected_game_state) 

    def test_dealer_highScore(self):
        game = {
            "turn": "dealer",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        player = {
            "id": "player",
            "cards": [10, 3],
            "cards_string": "[10, 3]",
            "score": 13,
        } 
        dealer = {
            "id": "dealer",
            "cards": [10, 5, 4],
            "cards_string": "[10, 5, 4]",
            "score": 19,
        } 
        expected_game_state = {
            "turn": "dealer",
            "isOver": True,
            "reason": "HighScore",
            "winner": dealer,
            "loser": player,
        }
        self.assertEqual(get_game_state(game, player, dealer), expected_game_state)

    def test_player_highScore(self):
        game = {
            "turn": "dealer",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        player = {
            "id": "player",
            "cards": [10, 5, 5],
            "cards_string": "[10, 5, 5]",
            "score": 20,
        } 
        dealer = {
            "id": "dealer",
            "cards": [10, 5, 4],
            "cards_string": "[10, 5, 4]",
            "score": 19,
        } 
        expected_game_state = {
            "turn": "dealer",
            "isOver": True,
            "reason": "HighScore",
            "winner": player,
            "loser": dealer,
        }
        self.assertEqual(get_game_state(game, player, dealer), expected_game_state) 

    def test_draw(self):
        game = {
            "turn": "dealer",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        player = {
            "id": "player",
            "cards": [10, 5, 5],
            "cards_string": "[10, 5, 5]",
            "score": 20,
        } 
        dealer = {
            "id": "dealer",
            "cards": [10, 5, 5],
            "cards_string": "[10, 5, 5]",
            "score": 20,
        } 
        expected_game_state = {
            "turn": "dealer",
            "isOver": True,
            "reason": "Draw",
            "winner": {},
            "loser": {},
        }
        self.assertEqual(get_game_state(game, player, dealer), expected_game_state) 

    def test_dealer_canPlayAgain(self):
        game = {
            "turn": "dealer",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        player = {
            "id": "player",
            "cards": [10, 5, 5],
            "cards_string": "[10, 5, 5]",
            "score": 20,
        } 
        dealer = {
            "id": "dealer",
            "cards": [10, 5, 1],
            "cards_string": "[10, 5, 1]",
            "score": 16,
        } 
        expected_game_state = {
            "turn": "dealer",
            "isOver": False,
            "reason": "",
            "winner": {},
            "loser": {}
        }
        self.assertEqual(get_game_state(game, player, dealer), expected_game_state) 

if __name__ == "__main__":
    unittest.main()


