from banker import Banker
from game_logic import GameLogic

class Game:
    def __init__(self, roller=None):
        self.round = 0
        self.banker = Banker()
        self.roller = roller or GameLogic.roll_dice
        self.total = 0

    def play(self):
        # Playing the game:
        # 1. print welcome message
        # 2. ask if they want to play (y or n)
        
        # Starting the game:
        # 3. Rolling (starting the game)
        # 4. Ask for a choice (dice or q) => will be sent to calculate_score
        # 5. Show round score
        # 6. Ask for r, b, or q
        # 7. if r: go to .....
        #    if q: go to quitting
        #    if b: go to banking
        
        # Quitting:
        #   a. Show total score
        #   b. Thanks message

        # Banking:
        #   a. Save the current score in total 
        #   b. Show the banked points
        #   c. Show total score
        #   d. Go to step #3 above
        pass


# When Flo init Game, it passes roller (customized one)
game = Game(customized_roller)

# When we play the game, we don't pass a roller
# Because we have our own roller in GameLogic (roll_dice)
game = Game()
