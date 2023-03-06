from tkinter import *
from tkinter import filedialog

import driver
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    label_file_explorer.configure(text="File Opened: " + filename)

label_file_explorer = Label(driver.main_window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "black")


button_explore = Button(driver.main_window,
                        text="Browse Files",
                        command=browseFiles)

button_exit = Button(driver.main_window,
                     text="Exit",
                     command=exit)

label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)
