import random

class Game:
    def __init__(self):
        self.items = ['rock', 'paper', 'scissors']
    
    def get_user_item(self):
        while True:
            user_input = input("choose rock/paper/scissors: ").lower()
            if user_input in self.items:
                return user_input
            else:
                print("invalid choice, please try again")
    
    def get_computer_item(self):
        return random.choice(self.items)
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "scissors" and computer_item == "paper") or \
             (user_item == "paper" and computer_item == "rock"):
            return "win"
        else:
            return "loss"
    
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"you selected {user_item}, computer selected {computer_item}")
        if result == "draw":
            print("It's a draw !")
        elif result == "win":
            print("congratulations, you win !")
        else:
            print("You lost!")

        return result
