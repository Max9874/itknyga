from tkinter import *
from random import randint

main = Tk()
main.geometry('400x250')
main.title('Метереологическое иследование')


def button_click():
    temperatures_S = []

    temperature_listbox.delete(0, END)

    for index in range(7):
        temperatures_S.append(randint(15, 25))
        temperature_listbox.insert(END, temperatures_S[index])


temperature_label = Label(text='Температура')
temperature_label.place(x='20', y='20')

temperature_listbox = Listbox(width=10, height=7)
temperature_listbox.place(x=20, y=50)

build_button = Button(text='Построить', command=button_click)
build_button.place(x=20, y=180)

canvas_zone = Canvas(main, width=290, height=250)
canvas_zone.place(x=110, y=0)
# Весь x:
canvas_zone.create_line(30, 200, 270, 200, arrow=LAST)
# Весь y:
canvas_zone.create_line(30, 200, 30, 10, arrow=LAST)
