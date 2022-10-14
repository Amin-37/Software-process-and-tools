import unittest
from game import game


class MyTestCase(unittest.TestCase):
    games = game()

    def test_game1(self):
        self.assertEqual('Draw', self.games.rock_paper_scissor('1', '1'))
        self.assertEqual('Draw', self.games.rock_paper_scissor('2', '2'))
        self.assertEqual('Draw', self.games.rock_paper_scissor('3', '3'))
        
    def test_game2(self):
        self.assertEqual('True', self.games.rock_paper_scissor('1', '3'))
        self.assertEqual('True', self.games.rock_paper_scissor('2', '1'))
        self.assertEqual('True', self.games.rock_paper_scissor('3', '2'))
    
    def test_game3(self):
        self.assertEqual('False', self.games.rock_paper_scissor('3', '1'))
        self.assertEqual('False', self.games.rock_paper_scissor('1', '2'))
        self.assertEqual('False', self.games.rock_paper_scissor('2', '3'))



if __name__ == '__main__':
    unittest.main()
