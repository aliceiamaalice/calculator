import time
from tkinter import *
import random

wnd = Tk()
wnd.title("Калькулятор")
wnd.resizable(True, True)
wnd.geometry("600x600")
numbers = ""
text = ""


def number(value):
  global numbers
  numbers += str(value)
  label1.configure(text=numbers)


def evall():
  global numbers
  global t_start
  try:
    result = eval(numbers)
    numbers = str(result)
    label1.configure(text=str(numbers))
  except:
    numbers = ""
    label1.configure(text="Ошибка")
  


for i in range(1, 4):
  for f in range(1, 3):
    btn = Button(wnd,text=f"{f + (i-1)*3}",command=lambda f=f + (i - 1) * 3: number(f))
    btn.grid(row=i, column=f)
    f += 1
  btn2 = Button(wnd,text=f"{f + (i-1)*3}",command=lambda f=f + (i - 1) * 3: number(f))
  btn2.grid(row=i, column=f + 1)


def delete():
  global numbers
  numbers = ""
  label1.configure(text=numbers)


eauqle = Button(wnd, text="=", command=evall)
plus = Button(wnd, text="+", command=lambda: number("+"))
minus = Button(wnd, text="--", command=lambda: number("-"))
multiply = Button(wnd, text="*", command=lambda: number("*"))
divide = Button(wnd, text="/", command=lambda: number("/"))
power = Button(wnd, text="^", command=lambda: number("**"))
dot = Button(wnd, text=".", command=lambda: number("."))
eauqle.grid(row=5, column=5)
plus.grid(row=4, column=5)
minus.grid(row=3, column=5)
multiply.grid(row=2, column=5)
divide.grid(row=1, column=5)
zero = Button(wnd, text="0", command=lambda: number(0))
zero.grid(row=4, column=2)
delete = Button(wnd, text="del", command=delete)
delete.grid(row=1, column=6)
power.grid(row=4, column=1)
dot.grid(row=4, column=4)
label1 = Label(wnd, text="", font=("Times New Roman", 14))
label1.grid(row=0, column=0, columnspan=4)
wnd.mainloop()