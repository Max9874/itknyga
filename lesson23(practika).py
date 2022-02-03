from tkinter import *
from random import randint as random_number

tk = Tk()
tk.title("Метеорологическое иследование")
tk.geometry('350x230')


def button_click():
    get_data_S = []
    counter = 0

    first_S_box.delete(END, 0)
    second_S_box.delete(END, 0)

    for value in range(7):
        get_data_S.append(random_number(-5, 8))
        first_S_box.insert(END, get_data_S[value])
        if get_data_S[value] > 0:
            counter += 1
            second_S_box.insert(END, str(value+1)+'-'+str(get_data_S[value]))

    k_value_label['text'] = 'k=' + str(counter)
    max_temperature_label['text'] = 'max=' + str(max(get_data_S))
    min__temperature_label['text'] = 'min=' + str(min(get_data_S))


temperature_label = Label(text='Температура')
temperature_label.place(x='20', y='20')

warm_days_label = Label(text='Тёплые дни')
warm_days_label.place(x='120', y='20')

button = Button(text='Обчислить', command=button_click)
button.place(x='220', y='20')

max_temperature_label = Label(text='max=')
min__temperature_label = Label(text='min=')
k_value_label = Label(text='k=')
max_temperature_label.place(x='220', y='50')
min__temperature_label.place(x='220', y='80')
k_value_label.place(x='220', y='110')

first_S_box = Listbox(width='10')
first_S_box.place(x='20', y='50')
second_S_box = Listbox(width='10')
second_S_box.place(x='120', y='50')
