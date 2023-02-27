#Program 14: Guessing Game
capitalGuess = input("What is the capital of Ohio? ").upper()
numberOfGuesses = 1

while capitalGuess != "COLUMBUS":
    numberOfGuesses = numberOfGuesses + 1
    if numberOfGuesses > 3:
        print("Game Over! You guesses incorrectly 3 times.")
        break
    capitalGuess = input("Guess again. ")
if numberOfGuesses <= 3:    
    print("You guessed it. The capital of Ohio is Columbus. It took you " + str(numberOfGuesses) + " guesses.")
