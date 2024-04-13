from tkinter import *
import pandas as pd
import numpy as np
import tkinter.ttk as ttk
import string

letters_english = [i for i in string.ascii_lowercase]


def erase_func():
    text_content.delete("1.0", END)
    window.update()


def import_func():
    with open("files/text.txt") as file:
        all_sentences = file.readlines()
        all_sentences.reverse()
        for line in all_sentences:
            text_content.insert("1.0", line)


def back_to_text_button(text):
    print(text)
    text_content.delete("1.0", END)
    text_content.insert('1.0', text)


def change_letters():
    letter_old = letter_to_change.get()
    letter_new = change_to.get()
    all_text = text_content.get('1.0', END)
    letter_map = {letter_old: letter_new, letter_new: letter_old}
    translation_table = str.maketrans(letter_map)
    all_text = all_text.translate(translation_table)
    text_content.delete('1.0', END)
    text_content.insert('1.0', all_text)


def get_table():
    current_text = text_content.get("1.0", END)
    button_back = Button(window, width=19, bg="#641E16", command=lambda: back_to_text_button(text), text="Back",
                         fg="#FEF9E7", font=("Optima", 10, "bold"))
    button_back.place(rely=0.27, relx=0.799, anchor=N)
    df = pd.DataFrame()

    language = "ENG"

    if language == "UKR":
        alphabet = [chr(i) for i in range(1072, 1104)]

    elif language == "ENG":
        alphabet = [letter for letter in string.ascii_lowercase]

    hash_table = dict.fromkeys(alphabet, 0)
    text = text_content.get("1.0", END)
    text = text.strip("!.,")

    for j in text:
        j = j.lower()
        if j.isalpha():
            if j in hash_table.keys():
                hash_table[j] += 1
        relative = np.array(list(hash_table.values()))
        relative_sum = relative.sum()

    erase_func()
    df.insert(0, "Letter", hash_table.keys())
    df.insert(1, "Absolute Frequency", hash_table.values())
    df.insert(2, "Relative Frequency", list(map(lambda x: round(x / relative_sum, 3), relative)))
    text_content.delete("1.0", END)
    text_content.insert("1.0", df.sort_values('Absolute Frequency', ascending=False))


window = Tk()
window.configure(background="#FDEBD0")
window.geometry("1000x650")
window.resizable(height=False, width=False)

label_in_window = Label(window, height=5, width=73, text="Frequency Table Text", bg="#641E16",
                        font=("CASTELLAR", 16, "bold"), fg="#F5EED3")
label_in_window.pack_propagate(False)
label_in_window.pack()

lable_in_window2 = Label(window, height=1, width=33, text="Enter Text", bg="#641E16", font=("Gentium Basic", 14),
                         fg="#FEF9E7")
lable_in_window2.pack_propagate(False)
lable_in_window2.pack(pady=45)

text_content = Text(window, height=10, width=90, background="#DA9760", font=("Garamond", 14))
text_content.pack(padx=0, pady=20, side=TOP)

button_table = Button(window, width=19, bg="#641E16", command=get_table, text="Get Table", fg="#FEF9E7",
                      font=("Optima", 10, "bold"))
button_table.pack(pady=0)

button_erase = Button(window, width=19, bg="#641E16", command=erase_func, text="Erase", fg="#FEF9E7",
                      font=("Optima", 10, "bold"))
button_erase.place(rely=0.7975, relx=0.3, anchor=E)

button_import = Button(window, width=19, command=import_func, bg="#641E16", text="Import", fg="#FEF9E7",
                       font=("Optima", 10, "bold"))
button_import.place(rely=0.7975, relx=0.867, anchor=E)

button_submit = Button(window, width=19, bg="#641E16", text="Submit", fg="#FEF9E7", command=change_letters,
                       font=("Optima", 10, "bold"))
button_submit.place(rely=0.924, relx=0.58, anchor=E)

change_to = ttk.Combobox(window, values=letters_english, width=5, height=5, background="blue")
change_to.insert(0, "to")
change_to.place(relx=0.7, rely=0.9079, anchor=N)

letter_to_change = ttk.Combobox(window, values=letters_english, width=5, height=5, background="blue")
letter_to_change.insert(0, "from")
letter_to_change.place(relx=0.3, rely=0.908, anchor=N)

window.mainloop()
