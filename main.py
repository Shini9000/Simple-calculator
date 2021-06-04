from tkinter import *

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():

    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""

window = Tk()
window.title("Simple Calculator - https://github.com/Shini9000")
window.geometry("400x500")
window.config(bg="#9D9D9D")
window.iconbitmap('icon.ico')

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 25), width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

# Numbers

button1 = Button(frame, text=1, height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

# Functions // Symbols

plus = Button(frame, text="+", height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press("+"))
plus.grid(row=0, column=3)

subtract = Button(frame, text="-", height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press("-"))
subtract.grid(row=1, column=3)

divide = Button(frame, text="/", height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press("/"))
divide.grid(row=2, column=3)

multiply = Button(frame, text="*", height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press("*"))
multiply.grid(row=3, column=3)

equal = Button(frame, text="=", height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=equals)
equal.grid(row=3, column=2)

dot = Button(frame, text=".", height=4, width=9, font=35, bg="#5A5A5A", fg="white",
                 command=lambda: button_press("."))
dot.grid(row=3, column=1)

clear = Button(window, text="clear", height=4, width=12, font=35, bg="#3B3B3B", fg="red",
                 command=clear)
clear.pack()

window.mainloop()
