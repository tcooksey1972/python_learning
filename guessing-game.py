# a combination of while loops, if statements, variables using a gamificaton.
# Game explained:  We specify a secret word and the user can interact and guess the word
# Setting up the secret word and initializing variables


secret_word = "Learning"  # The secret word that the user needs to guess
guess = ""               # Variable to store the user's current guess
guess_count = 0         # Number of guesses the user has made
guess_limit = 3         # Maximum number of guesses allowed
out_of_guesses = False   # Flag indicating if the user is out of guesses

# Start of the guessing game loop
while guess != secret_word and not(out_of_guesses):
    # Check if the user has remaining guesses
    if guess_count < guess_limit:
        guess = input("Enter guess:  ")  # Prompt the user for a guess
        guess_count += 1                # Increment the guess count
    else:
        out_of_guesses = True           # If out of guesses, set the flag to True

# Determine the outcome of the game
if out_of_guesses:
    print("Out of guesses, You lose!")  # Inform the user they've run out of guesses
else:
    print("Winner!")                   # Congratulate the user for guessing the secret word
