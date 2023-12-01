class BowlingGame:   # Defined class name as BowlingGame
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):# Looping through each frame in the 10-pin bowling game
            if self.isStrike(rollIndex):# It checks the current frame is a strike
                result += self.strikeScore(rollIndex)# Adds strike score to the next roll and move to the next frame
                rollIndex += 1
            elif self.isSpare(rollIndex):# It checks the current frame is a spare 
                result += self.spareScore(rollIndex)# Adds spare score to the next roll and move to the next frame
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)# Add normal frame to the next frame and move to the next frame
                rollIndex += 2
        return result # Returns the total score for the entire game

    def isStrike(self, rollIndex):
        #Checks the current roll is a strike then returns 10
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        #Checks the current roll is a spare then sum of two rolls is 10
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        # It calculates the score for a strike frame 10+ next two rolls
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        # It calculates the score for a spare frame 10+ next roll
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        # Calculates the regular frame score
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
