from tkinter import *

main = Tk()
main.title('Шифр Цезаря')


def encrypt_button_click():
    encrypted_message = ""
    message = message_text_entry.get()
    key = int(key_entry.get())

    for index in range(message):
        kod = ord(index) + key
        encrypted_message += ord(kod)
    encrypted_text_entry.insert(0, encrypted_message)


canvas = Canvas(main, width=300, height=210)

message_text_label = Label(text='Текст Сообщение')
message_text_label.place(x=20, y=20)

message_text_entry = Entry()
message_text_entry.place(x=20, y=50, width=250)

key_label = Label(text='key')
key_label.place(x=20, y=80)

key_entry = Entry()
key_entry.place(x=70, y=80, width=50)

encrypt_button = Button(text='Шифрувати', command=encrypt_button_click)
encrypt_button.place(x=20, y=110, width=100)

encrypted_text_label = Label(text='Зашифроване повiдомлення')
encrypted_text_label.place(x=20, y=140)

encrypted_text_entry = Entry()
encrypted_text_entry.place(x=20, y=170, width=250)
