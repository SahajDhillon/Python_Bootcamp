from game_data import data
from art import logo, vs
import random
import os


def clear_console():
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')


def get_random_data():
    """Generates random data for comparison"""
    return random.choice(data)


def format_data(account):
    """Formats into printable statement"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name} a {description} from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks whether a has more followers or b has more"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    game_count = 0
    game_continue = 'true'

    account_a = get_random_data()
    account_b = get_random_data()

    while game_continue == 'true':
        account_a = account_b
        account_b = get_random_data()
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        a_followers_count = account_a['follower_count']
        b_followers_count = account_b['follower_count']
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        is_correct = check_answer(guess, a_followers_count, b_followers_count)
        print(logo)
        if is_correct:
            game_count += 1
            print(f"You got that right , Current Score : {game_count}")

        else:
            game_continue = 'false'
            print(f"Game Over !! Your answer is incorrect . Final Score : {game_count}")


game()
# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
# Get follower count.
# If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
