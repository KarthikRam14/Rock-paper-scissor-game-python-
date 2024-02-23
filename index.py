import random

def generate_random_number(min, max):
    return random.randint(min, max)

def randomly_select_rock_paper_scissors():
    choices = ["Rock", "Paper", "Scissors"]
    random_index = generate_random_number(0, 2)
    return choices[random_index]

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "Player"
    else:
        return "Computer"

def display_choices(player_choice, computer_choice):
    print("Player chose: " + player_choice)
    print("Computer chose: " + computer_choice)

def display_result(winner):
    if winner == "Tie":
        print("It's a tie!")
    else:
        print(winner + " wins!")

def play_rock_paper_scissors():
    player_choice = input("Enter your choice (Rock/Paper/Scissors): ").capitalize()
    
    # Validate user input
    while player_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        player_choice = input("Enter your choice (Rock/Paper/Scissors): ").capitalize()

    computer_choice = randomly_select_rock_paper_scissors()
    winner = determine_winner(player_choice, computer_choice)

    display_choices(player_choice, computer_choice)
    display_result(winner)

# Example usage:
play_rock_paper_scissors()
