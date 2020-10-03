from __future__ import print_function

HANGMAN_STAGES = ["""
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

wrong_guess = 1
user_input = []
correct_answer = []
alpha_s = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
          "V", "W", "X", "Y", "Z"]
alpha_c = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
          "v", "w", "x", "y", "z"]
guessed_letter = []
wrong_letter = []

print("Let's play Hangman!")
word = str(input("Enter a word to get started: ")).upper()

print(HANGMAN_STAGES[0])
print()

for i in range(len(word)):
    if word[i] == " ":
        correct_answer.append("  ")
    else:
        correct_answer.append("_ ")
        user_input.append(word[i])

for answer in correct_answer:
    print(" ".join(answer), end="")

print()
print()
print("Don't hang him! Good luck!")
while wrong_guess < 7:
    guess = str(input("Guess a Letter: ")).upper()
    alphaTest = False
    guessed_l = False
    guessed_right = False

    for s in alpha_s:
        if guess == s:
            alphaTest = True
            break
    for c in alpha_c:
        if guess == c:
            alphaTest = True
            break

    for g in guessed_letter:
        if guess == G:
            guessed_l = True
            break

    for letter in user_input:
        if guess == letter:
            guessed_right = True
            break

    if len(guess) > 1:
        print("That's more than ONE character!!!")
        wrong_guess += 1
    elif alphaTest == False:
        print("That's not a LETTER!!!")
        wrong_guess += 1
    elif guessed_l == True:
        print("You guessed that one already!!!")
    elif guessed_right == True:
        print("You got that letter right!")
        guessed_letter.append(guess)
        print(HANGMAN_STAGES[wrong_guess - 1])

        for i in range(len(word)):

            if word[i] == guess:
                correct_answer[i] = guess + " "

        for answer in correct_answer:
            print(" ".join(answer), end="")

        print()
        print(wrong_letter)
        print()
    else:
        print("Oops, looks like that's not one of the letters!")
        wrong_letter.append(guess)
        guessed_letter.append(guess)
        print(HANGMAN_STAGES[wrong_guess])

        for answer in correct_answer:
            print(" ".join(answer), end="")

        print()
        print(wrong_letter)
        print()
        wrong_guess += 1

    win_count = 0
    for items in correct_answer:
        if items == "_ ":
            win_count += 1

    if win_count == 0:
        print("Congratulations! You have won the game!")
        input("Press 'Enter' to Exit")
        break
else:
    print("Game Over! He's hanged!")
    input("Press 'Enter' to Exit")
