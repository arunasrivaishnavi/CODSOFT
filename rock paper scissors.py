import random
def game():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        print(f"\nUser chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! User wins!")
            else:
                print("Paper covers rock! Computer wins!")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! User wins!")
            else:
                print("Scissors cuts paper! Computer wins!")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! User wins!")
            else:
                print("Rock smashes scissors! Computer wins!")
        play_again = input("Play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Please enter yes or no: ").lower()
        if play_again != "yes":
            break
game()