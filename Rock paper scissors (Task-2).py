import random

def get_hand_diagram(choice):
    diagrams = {
        'rock': """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """,
        'paper': """
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        """,
        'scissors': """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """
    }
    return diagrams[choice]

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()

        print("\nYou chose:")
        print(get_hand_diagram(user_choice))

        print("Computer chose:")
        print(get_hand_diagram(computer_choice))

        result = determine_winner(user_choice, computer_choice)

        if result == 'win':
            print("You win this round!")
            user_score += 1
        elif result == 'lose':
            print("You lose this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"\nScore: You {user_score} - {computer_score} Computer")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nFinal Score:")
    print(f"You {user_score} - {computer_score} Computer")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
