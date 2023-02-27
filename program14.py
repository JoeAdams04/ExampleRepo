# Program 14: Guessing Game
flowerGuess = input("What is the best flower?")
numberOfGuesses = 1

while flowerGuess != "Rose":
    numberOfGuesses = numberOfGuesses + 1
    if numberOfGuesses > 3:
        print("Sorry! You have guessed wrong, beter luck next time!")
        break
    flowerGuess = input("Guess Again.")
if numberOfGuesses <= 3:
    print("You guessed it. One of the best flowers is a Rose. It took you rose" + str(numberOfGuesses) + " guesses!")