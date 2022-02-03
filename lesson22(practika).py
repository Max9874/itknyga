from tkinter import *

tk = Tk()
tk.geometry('100x100')


def button_click():
    resave_data_S = [int(i) for i in entry_values.get().split(",")]
    counter = 0

    for temperature in range(len(resave_data_S)):
        if resave_data_S[temperature] > 0:
            counter += 1

    print(resave_data_S)
    print(f'Максимальная температура {max(resave_data_S)}, минимальная температура {min(resave_data_S)}')
    print('Температура поднималась выше 0 - {} раз'.format(counter))


entry_values = Entry()
entry_values.pack()

button = Button(text='Вычеслить', command=button_click)
button.pack()

print('Выполнено')
