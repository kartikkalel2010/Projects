import random

def get_user_choice():
    choice = ''
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Choose rock, paper, or scissors: ").lower()
    return choice

def get_ai_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, ai):
    if player == ai:
        return "It's a tie!"
    elif (player == 'rock' and ai == 'scissors') or \
         (player == 'paper' and ai == 'rock') or \
         (player == 'scissors' and ai == 'paper'):
        return "You win!"
    else:
        return "AI wins!"

def play_game():
    print("🎮 Welcome to Rock Paper Scissors!")
    while True:
        player_choice = get_user_choice()
        ai_choice = get_ai_choice()
        print(f"\nYou chose: {player_choice}")
        print(f"AI chose: {ai_choice}")
        result = determine_winner(player_choice, ai_choice)
        print("Result:", result)

        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
