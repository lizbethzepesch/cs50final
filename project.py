import string
from tkinter import *


def is_word_guessed(secret, letters_guessed):
    for letter in secret:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret, letters_guessed):
    guessed_list = list(len(secret) * '_')
    for i in range(len(secret)):
        if secret[i] in letters_guessed:
            guessed_list[i] = secret[i]
    return ' '.join(guessed_list)


def get_available_letters(letters_guessed, available_letters):
    for letter in available_letters:
        if letter in letters_guessed:
            available_letters.remove(letter)
    return available_letters


def main():
    root = Tk()
    root.geometry('800x600')
    root.title('Hangman')

    secret = 'secret'
    attempt = '1'
    letters_guessed = ['', ]
    available_letters = list(string.ascii_lowercase)

    def get_letter():
        print(inputt.get())
        print(attempt)

        if len(inputt.get().lower()) != 1 or not inputt.get().lower().isalpha():
            oops.pack()
            attempt = str(int(attempt) + 1)
            chel.config(image=hangs_pics[attempt])
            return
        if inputt.get().lower() not in available_letters:
            oops2.pack()
            attempt = str(int(attempt) + 1)
            chel.config(image=hangs_pics[attempt])
            return
        else:
            if inputt.get().lower() in secret:
                word.config(text=get_guessed_word(secret, letters_guessed))
            else:
                oops3.pack()
                attempt = str(int(attempt) + 1)
                chel.config(image=hangs_pics[attempt])
                return
        letters_guessed.append(inputt.get().lower())

        if attempt == 8:
            inputt.destroy()
            space3.destroy()
            available_letters_tk.destroy()
            available_letters_list_tk.destroy()
            button.destroy()

            lose = Label(root, text="You lose!", font=('Courier New', 35, 'bold'), anchor="center")
            lose.pack()

        if '_' not in get_guessed_word(secret, letters_guessed):
            inputt.destroy()
            space3.destroy()
            available_letters_tk.destroy()
            available_letters_list_tk.destroy()
            button.destroy()
            oops.destroy()
            oops2.destroy()
            oops3.destroy()
            word.config(text=get_guessed_word(secret, letters_guessed))
            win.pack()

    hangs_pics = {'1': PhotoImage(file='./img/1.png'),
            '2': PhotoImage(file='./img/2.png'),
            '3': PhotoImage(file='./img/3.png'),
            '4': PhotoImage(file='./img/4.png'),
            '5': PhotoImage(file='./img/5.png'),
            '6': PhotoImage(file='./img/6.png'),
            '7': PhotoImage(file='./img/7.png'),
            '8': ''}

    label = Label(root, text='Hangman', font=('Courier New', 35, 'bold'), anchor="center")
    word = Label(root, text=get_guessed_word(secret, letters_guessed), font=('Courier New', 20, 'bold'), anchor="center")
    space = Label(root, text=" ", font=('Courier New', 15, 'bold'), anchor="center")
    available_letters_tk = Label(root, text="Available letters:", font=('Courier New', 16, 'bold'), anchor="center")
    available_letters = ' '.join(get_available_letters(letters_guessed, available_letters))
    available_letters_list_tk = Label(root, text=available_letters, font=('Courier New', 15, 'bold'), anchor="center")
    space2 = Label(root, text=" ", font=('Courier New', 15, 'bold'), anchor="center")
    chel = Label(root, image=hangs_pics[attempt], anchor="center")
    space3 = Label(root, text=" ", font=('Courier New', 20, 'bold'), anchor="center")
    inputt = Entry(root, font=('Courier New', 15, 'bold'), relief=RIDGE)
    button = Button(root, text='submit', font=('Courier New', 10, 'bold'), command=get_letter)

    oops = Label(root, text="Oops, you didn't write the letter!", font=('Courier New', 10, 'bold'), anchor="center")
    oops2 = Label(root, text="Oops, you already tried this letter!", font=('Courier New', 10, 'bold'), anchor="center")
    oops3 = Label(root, text="Oops! That letter is not in my word!", font=('Courier New', 10, 'bold'), anchor="center")
    win = Label(root, text="You win!", font=('Courier New', 35, 'bold'), anchor="center")

    label.pack()
    word.pack()
    space.pack()
    available_letters_tk.pack()
    available_letters_list_tk.pack()
    space2.pack()
    chel.pack()
    space3.pack()
    inputt.pack()
    button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()