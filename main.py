from tkinter import *
from set_ui import setUI
from paint import Paint


def main():
    root = Tk()
    root.geometry("850x500+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()