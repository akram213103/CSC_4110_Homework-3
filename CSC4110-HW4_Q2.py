import random

class PirateGame:
    def __init__(self, initial_bank, wager):
        self.treasure_chest = ['gold coin', 'silver coin', 'emerald', 'diamond', 'ruby', 'pearl']
        self.bank = initial_bank
        self.wager = wager

    def populate_treasure_chest(self, items):
        self.treasure_chest.extend(items)

    def play(self):
        while self.bank > 0:
            print(f"Bank balance: {self.bank}, Wagering: {self.wager}")
            # Ask the player if they want to continue before each spin
            choice = input("Press 'y' to spin the wheel and 'n' to quit: ").lower()
            if choice == 'n':
                print("Ye be quittin' early. Better safe than sorry!")
                break

            win = random.choice([True, False])  # Simulating a 50-50 chance to win
            if win:
                prize = random.choice(self.treasure_chest)
                print(f"Yarrr! Ye won a {prize}!")
                self.bank += self.wager  # Wins back the wager
            else:
                print("Shiver me timbers! Ye lost this round.")
                self.bank -= self.wager  # Loses the wager
            
            if self.bank <= 0:
                print("Arrr! Ye've run out of coins!")
                break

# Example usage
items_to_add = ['sapphire', 'topaz', 'amethyst']
initial_bank = 100  # Starting bank amount
wager = 10  # Wager per spin/grab

pirate_game = PirateGame(initial_bank, wager)
pirate_game.populate_treasure_chest(items_to_add)
pirate_game.play()
