from sympy import *
import cv2
import pytesseract
from tkinter import *
from tkinter import filedialog
from browse import *
def start():


    main_window = Tk()
    main_window.geometry("500x500")
    main_window.config(background="black")

    Label(main_window, text="This is the Integralitator. Follow the instructions.").grid(row_=0, column_=0)
    Label(main_window, text="Take a picture of your Integral").grid(row_=0, column_=0)

    browseFiles()

    main_window.mainloop()
