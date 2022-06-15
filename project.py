import string


def is_word_guessed(secret, letters_guessed):
    for letter in secret:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret, letters_guessed, guessed_word):
    for i in range(len(secret)):
        if secret[i] in letters_guessed:
            guessed_word[i] = secret[i]
    return guessed_word


def get_available_letters(letters_guessed, available_letters):
    for letter in available_letters:
        if letter in letters_guessed:
            available_letters.remove(letter)


def hangman(secret):
    tries = 8
    lets = 0
    letter = ''

    guessed_word = len(secret) * '_'
    letters_guessed = []
    available_letters = list(string.ascii_lowercase)

    print("Welcome to the game, Hangman!\n")
    print("I am thinking of a word that is {} letters long.\n".format(len(secret)))

    while tries:
        print("-------------\n")
        print("You have {} guesses left.\n".format(tries))
        print("Available letters: ")
        get_available_letters(letters_guessed, available_letters)
        print(available_letters)
        print('\n')

        print("Please guess a letter: ")
        letter = input()
        letters_guessed[lets] = letter
        lets += 1
        if is_word_guessed(secret, letters_guessed):
            print("-------------\nCongratulations, you won!")
            return
        else:
            if letter not in available_letters:
                print("Oops, you already tried this letter!")
                continue
            else:
                if letter in secret:
                    guessed_word = get_guessed_word(secret, letters_guessed, guessed_word)
                    print("Good guess:")
                    print(guessed_word)

                else:
                    print("Oops! That letter is not in my word:")
                    tries -= 1
                    print(guessed_word)

            if secret == letter:
                print("-------------\nCongratulations, you won!")
                return


def main():
    secret = 'purples'
    hangman(secret)

if __name__ == '__main__':
    main()