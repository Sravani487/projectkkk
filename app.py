import random

#change - 1
def number_guessing_game():
    """A simple number guessing game."""
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...\n")

    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"Attempts remaining: {remaining}")

        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("⚠️  Please enter a valid number.\n")
            continue

        attempts += 1

        if guess < secret:
            print("📈 Too low! Try higher.\n")
        elif guess > secret:
            print("📉 Too high! Try lower.\n")
        else:
            print(f"🎉 Correct! The number was {secret}.")
            print(f"   You got it in {attempts} attempt(s)!")
            return

    print(f"\n💀 Game over! The number was {secret}. Better luck next time!")


if __name__ == "__main__":
    number_guessing_game()

#change-2
print("change-2")
