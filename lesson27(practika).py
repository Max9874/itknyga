from tkinter import *

main = Tk()
main.title('Шифр Цезаря')
main.geometry('350x320')


def encrypt_button_click():
    encrypted_message = ""
    message = message_entry_text.get(1.0, END)
    key = int(key_entry.get())

    encrypted_text.delete(1.0, END)
    message = message.replace('\n', '')

    for index in message:
        kod = ord(index) + key
        encrypted_message += chr(kod)
    encrypted_text.insert(1.0, encrypted_message)


def decipher_button_click():
    decipher_message = ""
    message = encrypted_text.get(1.0, END)
    key = int(key_entry.get())

    message_entry_text.delete(1.0, END)
    message = message.replace('\n', '')

    for index in message:
        kod = ord(index) - key
        decipher_message += chr(kod)
    message_entry_text.insert(1.0, decipher_message)


canvas = Canvas(main, width=300, height=210)

message_text_label = Label(text='Текст Сообщение')
message_text_label.place(x=20, y=20)

message_entry_text = Text(width=15, height=10)
message_entry_text.place(x=20, y=50)

key_label = Label(text='key')
key_label.place(x=20, y=230)

key_entry = Entry()
key_entry.place(x=70, y=230, width=70)

encrypt_button = Button(text='Шифрувати', command=encrypt_button_click)
encrypt_button.place(x=20, y=260, width=120)

decipher_button = Button(text='Розшифрувати', command=decipher_button_click)
decipher_button.place(x=170, y=260, width=120)

encrypted_text_label = Label(text='Зашифроване повiдомлення')
encrypted_text_label.place(x=170, y=20)

encrypted_text = Text(width=15, height=10)
encrypted_text.place(x=170, y=50)
