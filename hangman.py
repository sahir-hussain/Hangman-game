import random
def Hangman():
    word = random.choice(["itachi","naruto","minato","jiraya","sasuke","madara","pain","hashirama","obito","kakashi"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main +"_" + " "
        if main == word:
            print(main)
            print("Congo Weebo.....I see you are a man of culture!")
            break
        print("Guess the character to save the hostage: ", main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("-------------")
            if turns == 8:
                print("8 turns left")
                print("-------------")
                print("     O       ")
            if turns == 7:
                print("7 turns left")
                print("-------------")
                print("     O       ")
                print("     |       ")
            if turns == 6:
                print("6 turns left")
                print("-------------")
                print("     O       ")
                print("     |       ")
                print("    /        ")
            if turns == 5:
                print("5 turns left")
                print("-------------")
                print("     O       ")
                print("     |       ")
                print("    / \      ")
            if turns == 4:
                print("4 turns left")
                print("-------------")
                print("   \ O       ")
                print("     |       ")
                print("    / \      ")
            if turns == 3:
                print("3 turns left")
                print("-------------")
                print("   \ O /     ")
                print("     |       ")
                print("    / \      ")
            if turns == 2:
                print("2 turns left")
                print("-------------")
                print("   \ O /|    ")
                print("     |       ")
                print("    / \      ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting...")
                print("-------------")
                print("   \ O _|/   ")
                print("     |       ")
                print("    / \      ")
            if turns == 0:
                print("You lose weeblet!")
                print("You let the hostage die")
                print("-------------")
                print("     O_|     ")
                print("    /|\      ")
                print("    / \      ")
                break


name = input("Enter your name : ")
print("Welcome", name)
print("-------------------")
print("Try to guess the character from Naruto in less than 10 attempts")
Hangman()
print()