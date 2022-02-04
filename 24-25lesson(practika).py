from tkinter import *
from random import randint

main = Tk()
main.geometry('400x250')
main.title('Метереологическое иследование')


def button_click():
    temperatures_S = []

    temperature_listbox.delete(0, END)

    for index in range(7):
        temperatures_S.append(randint(10, 26))
        temperature_listbox.insert(END, temperatures_S[index])

    for ii in range(6):
        canvas_zone.create_line(OX[ii], 200 - temperatures_S[ii] * 5, OX[ii + 1], 200 - temperatures_S[ii + 1] * 5,
                                fill='green')
        if temperatures_S[ii] == max(temperatures_S):
            canvas_zone.create_oval(OX[ii]-3, 200-temperatures_S[ii]*5-3, OX[ii]-3, 200-temperatures_S[ii]*5+3, fill='red')
        elif temperatures_S[ii] == min(temperatures_S):
            canvas_zone.create_oval(OX[ii]-3, 200-temperatures_S[ii]*5-3, OX[ii]-3, 200-temperatures_S[ii]*5+3, fill='blue')


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
# Позначки на оси OX
OX = []
for i in range(60, 250, 30):
    OX.append(i)

for i in range(7):
    canvas_zone.create_line(OX[i], 195, OX[i], 205)
    canvas_zone.create_text(OX[i], 215, text=i + 1)
# Позначки на оси OY
for i in range(5, 36, 5):
    canvas_zone.create_line(25, 200 - i * 5, 35, 200 - i * 5)
    canvas_zone.create_text(15, 200 - i * 5, text=i)
# Постройка графика
