from sympy import *
import cv2
import pytesseract
from tkinter import *
from tkinter import filedialog


def start():

    main_window = Tk()
    main_window.geometry("1240x160")
    main_window.config(background="white")

    Label(main_window, text="This is the Integralitator. Follow the instructions.").grid(row_=0, column_=0)

    def browseFiles():
        filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

        label_file_explorer.configure(text="File Opened: " + filename)

    button_explore = Button(main_window,
                        text="Browse Files",
                        command=browseFiles)

    button_exit = Button(main_window,
                     text="Exit",
                     command=exit)



    button_explore.grid(column=10, row=29)



    button_exit.grid(column=10, row=30)

    label_file_explorer = Label(main_window,
                                text="Browse For Integral Image",
                                width=100, height=4,
                                fg="black")
    label_file_explorer.grid(row = 25, column = 0)
    main_window.mainloop()