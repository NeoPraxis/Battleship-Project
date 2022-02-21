import unittest
from battleship import Battleship


class TestBattleship(unittest.TestCase):

    def test_if_battleship_can_instantiate(self):
        battleship = Battleship()
        self.assertIsInstance(battleship, Battleship)

    def test_print_welcome_to_battleship(self):
        pass

    def test_print_board(self):
        pass

    def test_is_player_input_valid_should_return_false_if_not_valid(self):
        pass

    def test_is_player_input_valid_should_return_true_if_not_valid(self):
        pass

    def test_if_ai_input_valid_should_return_false_if_not_valid(self):
        pass

    def test_if_ai_input_valid_should_return_true_if_valid(self):
        pass
    
    def test_ship_placement(self):
        pass

if __name__ == '__main__':
    unittest.main()