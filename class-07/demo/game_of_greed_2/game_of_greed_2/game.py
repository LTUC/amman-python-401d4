from game_of_greed_2.game_logic import GameLogic

class Game:
    def __init__(self, roller=None):
        self.roller = roller

    def play(self):
        print("Welcome to Game of Greed")
        user_input = input("Wanna play? ")
        if user_input == 'n':
            print("OK. Maybe another time")
        else:
            print('Starting round 1')
            print('Rolling 6 dice...')
            dice = self.roller(6)
            printable_dice = ','.join([str(d) for d in dice])
            print(printable_dice)
            do_quit = input("Enter dice to keep (no spaces), or (q)uit: ")
            if do_quit == 'q':
                print('Thanks for playing. You earned 0 points')

if __name__ == "__main__":
    roller = GameLogic.roll_dice
    game = Game(roller)
    game.play()