import random
print("welcome to Rock-Paper-Scissor") 

def main():
    computer_options = ["rock", "paper", "scissors"]
    print(f"Computer chose: {computer_options[random.randint(0,2)]}")

if __name__ == "__main__":
    main() 

