import random

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Variable to keep track of the number of attempts
    attempts = 0
    
    while True:
        # Get the user's guess
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        # Check if the guess is correct
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
        
        # Provide additional hints
        if number_to_guess % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
        
        if is_prime(number_to_guess):
            print("Hint: The number is prime!")
        else:
            print("Hint: The number is not prime.")
        
        if number_to_guess % 3 == 0:
            print("Hint: The number is divisible by 3.")
        if number_to_guess % 5 == 0:
            print("Hint: The number is divisible by 5.")

# Run the game
number_guessing_game()
