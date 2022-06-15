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
    hangs_pics = [PhotoImage(file='./img/1.png'),
                  PhotoImage(file='./img/2.png'),
                  PhotoImage(file='./img/3.png'),
                  PhotoImage(file='./img/4.png'),
                  PhotoImage(file='./img/5.png'),
                  PhotoImage(file='./img/6.png'),
                  PhotoImage(file='./img/7.png')]

    letters_guessed = ['', ]
    available_letters = list(string.ascii_lowercase)

    def get_letter():

        if inputt.get().lower() in secret:
            letters_guessed.append(inputt.get().lower())
            word.config(text=get_guessed_word(secret, letters_guessed))
            available_letters.remove(inputt.get())
            available_letters_list_tk.config(text=' '.join(available_letters))
        else:
            hangs_pics.pop(0)
            chel.config(image=hangs_pics[0])

            letters_guessed.append(inputt.get().lower())
            if len(hangs_pics) == 1:
                inputt.destroy()
                space3.destroy()
                available_letters_tk.destroy()
                available_letters_list_tk.destroy()
                button.destroy()
                lose = Label(root, text="You lose!", font=('Courier New', 35, 'bold'), anchor="center")
                lose.pack()


            available_letters.remove(inputt.get())
            available_letters_list_tk.config(text=' '.join(available_letters))


        if secret == get_guessed_word(secret, letters_guessed).replace(' ', ''):
            inputt.destroy()
            space3.destroy()
            available_letters_tk.destroy()
            available_letters_list_tk.destroy()
            button.destroy()
            win = Label(root, text="You won!", font=('Courier New', 35, 'bold'), anchor="center")
            word.config(text=get_guessed_word(secret, letters_guessed))
            win.pack()


    label = Label(root, text='Hangman', font=('Courier New', 35, 'bold'), anchor="center")
    word = Label(root, text=get_guessed_word(secret, letters_guessed), font=('Courier New', 20, 'bold'), anchor="center")
    space = Label(root, text=" ", font=('Courier New', 15, 'bold'), anchor="center")
    available_letters_tk = Label(root, text="Available letters:", font=('Courier New', 16, 'bold'), anchor="center")
    available_letters = get_available_letters(letters_guessed, available_letters)
    available_letters_list_tk = Label(root, text=' '.join(available_letters), font=('Courier New', 15, 'bold'), anchor="center")
    space2 = Label(root, text=" ", font=('Courier New', 15, 'bold'), anchor="center")
    chel = Label(root, image=hangs_pics[0], anchor="center")

    space3 = Label(root, text=" ", font=('Courier New', 20, 'bold'), anchor="center")
    inputt = Entry(root, font=('Courier New', 15, 'bold'), relief=RIDGE)
    button = Button(root, text='submit', font=('Courier New', 10, 'bold'), command=get_letter)




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