import random

class SnakeAndLadders:
    def __init__(self):
        self.board_size = 100
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 71: 91, 80: 100}
        self.player_positions = [0, 0]
        self.player_turn = 0

    def move_player(self, player, steps):
        new_position = self.player_positions[player] + steps
        if new_position > self.board_size:
            new_position = self.player_positions[player]

        if new_position in self.ladders:
            print(f"Player {player + 1} hit a ladder! Climbing up from {new_position} to {self.ladders[new_position]}.")
            new_position = self.ladders[new_position]
        elif new_position in self.snakes:
            print(f"Player {player + 1} hit a snake! Sliding down from {new_position} to {self.snakes[new_position]}.")
            new_position = self.snakes[new_position]

        self.player_positions[player] = new_position
        print(f"Player {player + 1} is now on square {new_position}.")

    def play_turn(self):
        input(f"Player {self.player_turn + 1}, press Enter to roll the dice.")
        dice_roll = random.randint(1, 6)
        print(f"Player {self.player_turn + 1} rolled a {dice_roll}.")
        self.move_player(self.player_turn, dice_roll)

        if self.player_positions[self.player_turn] == self.board_size:
            print(f"Player {self.player_turn + 1} wins!")
            return True

        self.player_turn = 1 - self.player_turn
        return False

    def play_game(self):
        print("Welcome to Snakes and Ladders!")
        while True:
            if self.play_turn():
                break

if __name__ == "__main__":
    game = SnakeAndLadders()
    game.play_game()
