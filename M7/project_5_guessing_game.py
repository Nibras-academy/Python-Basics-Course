import random
# Step 1: Generate a random number between 1 and 10
secret_number = random.randint(1, 10)


# Step 2: Initialize a variable to keep track of the user's guess
guess = 0

while guess != secret_number:
    # Step 4: Prompt the user to guess the number
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess == secret_number:
        # If the guess is correct,end the loop
        print("Congratulations! You guessed correct:", secret_number)
        break