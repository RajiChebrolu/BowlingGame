import unittest # imported unittest 
import BowlingGame # imported the class name 

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame() #Created a new instance of the BowlingGame class for each test

    def testGutterGame(self):
        for i in range(0, 20): # Rolling 20 times with 0 pins each time
            self.game.roll(0)
        assert self.game.score() == 0 # Assert the score value is 0 means a gutter game
        print("\nTest result1:",self.game.score()) # printed the test result to know the output

    def testAllOnes(self):
        self.rollMany(1, 20) # Rolling 20 times with 1 pin each time
        assert self.game.score() == 20 # Assert the score value is 20 for all ones
        print("\nTest Result2:",self.game.score())# printed the test result to know the output

    def testOneSpare(self):
        # Roll one spare means 5+5 =10, and folloed by 3
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17) # Roll remaining 17 times with 0 pins
        assert self.game.score() == 16 # Assert the score value is 16 for one spare
        print("\nTest Result3:",self.game.score())# printed the test result to know the output

    def testOneStrike(self):
        # Roll one strike means 10, and folloed by 3, 4
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)# Roll remaining 16 times with 0 pins
        assert self.game.score() == 24 # Assert the score value is 24 for one strike
        print("\nTest Result4:",self.game.score())# printed the test result to know the output

    def testPerfectGame(self):
        self.rollMany(10, 12) #Roll 12 strikes for a perfect game
        assert self.game.score() == 300 # Assert the total score is 300 for a perfect game
        print("\nTest Result5:",self.game.score())# printed the test result to know the output

    def testRandomPins(self):
        self.rollMany(5, 21) # Roll a combination of 5 and 0 for 21 rolls
        assert self.game.score() == 150 # Assert the total score is 150 for the random pins
        print("\nTest Result6:",self.game.score())# printed the test result to know the output

    def rollMany(self, pins, rolls):
        for i in range(rolls):# It is a helper function to roll a certain number of pins for a specified roll
            self.game.roll(pins)
            

