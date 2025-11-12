import random

def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower().strip()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please choose rock, paper, or scissors.")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    player_choice = get_player_choice()
    print(f"You chose: {player_choice}")

if __name__ == "__main__":
    main() 