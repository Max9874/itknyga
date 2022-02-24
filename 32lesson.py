from tkinter import *

main = Tk()
main.geometry('250x350')
main.title('Сортировка')


def btn_click():
    a = [number for number in Entry_1.get().split(" ")]
    Listbox_1.clear()
    for i in range(1, len(a)):
        Listbox_1.insert(END, a[i])


btn1 = Button(text='Фортунами', command=btn_click)
btn1.place(x=150, y=45)

Entry_1 = Entry()
Entry_1.place(x=20, y=50, width=105)

Listbox_1 = Listbox(width=17, height=10)
Listbox_1.place(x=20, y=120)

Lbl_input_s = Label(text='Входной список:')
Lbl_input_s.place(x=20, y=20)
Lbl_output_box = Label(text='Результат:')
Lbl_output_box.place(x=20, y=90)

# a = [int(input('Число: ')) for i_counter in range(5)]
# print(a)
# for j_index in range(1, 5):
#     for i_index in range(5 - j_index):
#        if a[i_index] > a[i_index + 1]:
#             a[i_index], a[i_index+1] = a[i_index+1], a[i_index]
# print(a)
