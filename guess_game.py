#       NUMBER GUESSING GAME

import random

print("=" * 45)
print("     WELCOME TO MY GUESS GAME")
print("=" * 45)

# Random number generate karna
secret_number = random.randint(1, 100)

# Variables
user_guess = 0
total_attempts = 0
guess_history = []

print("\nI have selected a number between 1 and 100.")
print("Try to guess the correct number!\n")

while user_guess != secret_number:

    try:
        user_guess = int(input("Enter your guess: "))

        # Attempts count
        total_attempts += 1

        # Store history
        guess_history.append(user_guess)

        # Conditions
        if user_guess > secret_number:
            print("📉 Lower number please!\n")

        elif user_guess < secret_number:
            print("📈 Higher number please!\n")

        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the correct number: {secret_number}")

            print(f"✅ Total Attempts: {total_attempts}")

            print("\n📝 Your Guess History:")
            print(guess_history)

    except ValueError:
        print("⚠ Invalid input! Please enter numbers only.\n")

print("\nThanks for playing my Guess Game!")
print("=" * 45)