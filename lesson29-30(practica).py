from tkinter import *

main = Tk()
main.title("Символьный калькулятор")
main.geometry("440x280")


def button_click():
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    text = input_text.get(1.0, END)
    text = text.replace("\n", "")

    first_list.delete(END, 0)
    second_list.delete(END, 0)

    for letter in alphabet:
        counter = 0
        for letter_index in text:
            if letter_index == letter:
                counter = counter + 1
        if counter > 0:
            first_list.insert(END, letter + ' - ' + str(counter))
            second_list.insert(END, letter + ' - ' + str(round(counter/len(text), 3)))


input_text_label = Label(text='Введіть текст:')
input_text_label.place(x=20, y=20)
in_text_label1 = Label(text="Kількість входжень")
in_text_label1.place(x=160, y=20)
in_text_label2 = Label(text="Частоти входжень")
in_text_label2.place(x=300, y=20)

input_text = Text(wrap=WORD)
input_text.place(x=20, y=50, width=120, height=160)
first_list = Listbox()
first_list.place(x=160, y=50, height=160, width=120)
second_list = Listbox()
second_list.place(x=300, y=50, height=160, width=120)
button = Button(text="Обчислити", command=button_click)
button.place(x=20, y=230)

# Scroll Lbox1{
Scroll_first__ = Scrollbar(first_list, command=first_list.yview)
Scroll_first__.place(x=100, height=160)
first_list.config(yscrollcommand=Scroll_first__.set)
# Scroll Lbox1}

# Scroll Lbox2{
Scroll_second = Scrollbar(second_list, command=second_list.yview)
Scroll_second.place(x=100, height=160)
second_list.config(yscrollcommand=Scroll_second.set)
# Scroll Lbox2}
