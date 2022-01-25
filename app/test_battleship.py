import unittest
from battleship import Battleship


class TestBattleship(unittest.TestCase):

    def test_if_battleship_can_instantiate(self):
        battleship = Battleship()
        self.assertIsInstance(battleship, Battleship)

    def test_is_player_input_valid_should_return_false_if_not_valid(self):
        pass

    def test_is_player_input_valid_should_return_true_if_not_valid(self):
        pass

    def test_is_board_set_should_return_true_if_set(self):
        pass

    def test_is_board_set_should_return_false_if_not_set(self):
        pass











if __name__ == '__main__':
    unittest.main()