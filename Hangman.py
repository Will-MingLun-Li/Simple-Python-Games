from __future__ import print_function

HANGMANSTAGES = ["""
  *------*
  |      |
         |
         |
         |
         |
++++++++++""", """
  *------*
  |      |
  0      |
         |
         |
         |
++++++++++""", """
  *------*
  |      |
  0      |
  |      |
         |
         |
++++++++++""", """
  *------*
  |      |
  0      |
 /|      |
         |
         |
++++++++++""", """
  *------*
  |      |
  0      |
 /|\     |
         |
         |
++++++++++""", """
  *------*
  |      |
  0      |
 /|\     |
 /       |
         |
++++++++++""", """
  *------*
  |      |
  0      |
 /|\     |
 / \     |
         |
++++++++++"""]

WrongGuess = 1
UserInput = []
CorrectAnswer = []
alphaS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
          "V", "W", "X", "Y", "Z"]
alphaC = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
          "v", "w", "x", "y", "z"]
GuessedLetter = []
WrongLetter = []

print("Let's play Hangman!")
word = str(input("Enter a word to get started: ")).upper()

print(HANGMANSTAGES[0])
print()

for i in range(len(word)):
    if word[i] == " ":
        CorrectAnswer.append("  ")
    else:
        CorrectAnswer.append("_ ")
        UserInput.append(word[i])

for answer in CorrectAnswer:
    print(" ".join(answer), end="")

print()
print()
print("Don't hang him! Good luck!")
while WrongGuess < 7:
    guess = str(input("Guess a Letter: ")).upper()
    alphaTest = False
    guessedL = False
    guessedRight = False

    for S in alphaS:
        if guess == S:
            alphaTest = True
            break
    for C in alphaC:
        if guess == C:
            alphaTest = True
            break

    for G in GuessedLetter:
        if guess == G:
            guessedL = True
            break

    for letter in UserInput:
        if guess == letter:
            guessedRight = True
            break

    if len(guess) > 1:
        print("That's more than ONE character!!!")
        WrongGuess += 1
    elif alphaTest == False:
        print("That's not a LETTER!!!")
        WrongGuess += 1
    elif guessedL == True:
        print("You guessed that one already!!!")
    elif guessedRight == True:
        print("You got that letter right!")
        GuessedLetter.append(guess)
        print(HANGMANSTAGES[WrongGuess - 1])

        for i in range(len(word)):

            if word[i] == guess:
                CorrectAnswer[i] = guess + " "

        for answer in CorrectAnswer:
            print(" ".join(answer), end="")

        print()
        print(WrongLetter)
        print()
    else:
        print("Oops, looks like that's not one of the letters!")
        WrongLetter.append(guess)
        GuessedLetter.append(guess)
        print(HANGMANSTAGES[WrongGuess])

        for answer in CorrectAnswer:
            print(" ".join(answer), end="")

        print()
        print(WrongLetter)
        print()
        WrongGuess += 1

    WinCount = 0
    for items in CorrectAnswer:
        if items == "_ ":
            WinCount += 1

    if WinCount == 0:
        print("Congratulations! You have won the game!")
        input("Press 'Enter' to Exit")
        break
else:
    print("Game Over! He's hanged!")
    input("Press 'Enter' to Exit")
