import unittest
from app.bowling import *

# Test the dependencies with unittest
class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_hookup(self):
        self.assertTrue(True)

    def test_gutter_balls(self):
        self.__many_open_frames__(10,0,0)
        self.assertEqual(0, self.game.score())

    def test_threes(self):
        self.__many_open_frames__(10,3,3)
        self.assertEqual(60, self.game.score())

    def test_spare_1(self):
        game = self.game
        game.spare(4,6)
        game.open_frame(3,5)

        self.__many_open_frames__(8,0,0)
        self.assertEqual(21, self.game.score())

    def test_spare_2(self):
        game = self.game
        game.spare(4,6)
        game.open_frame(5,3)

        self.__many_open_frames__(8,0,0)
        self.assertEqual(23, self.game.score())

    def test_strike(self):
        game = self.game
        game.strike()
        game.open_frame(4,3)

        self.__many_open_frames__(8,0,0)
        self.assertEqual(24, game.score())

    def __many_open_frames__(self, count, firstThrow, secondThrow):
        for i in range(0, count):
            self.game.open_frame(firstThrow, secondThrow)

if __name__ == '__main__':
    unittest.main()