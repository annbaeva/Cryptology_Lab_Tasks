from tkinter import *
import pandas as pd
import numpy as np
import string

def erase_func():
    text_content.delete("1.0", END)
    window.update()

def import_func():
    with open("files/text.txt") as file:
        all_sentences = file.readlines()
        all_sentences.reverse()
        for line in all_sentences:
            text_content.insert("1.0", line)


def get_table():
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

text_content = Text(window, height=15, width=100, background="#DA9760", font=("Bodoni MT Black", 10))
text_content.pack(padx=0, pady=20, side=TOP)

button_table = Button(window, width=19, bg="#641E16", command= get_table, text="Get Table", fg="#FEF9E7", font=("Optima", 10, "bold"))
button_table.pack(pady=0)

button_erase = Button(window, width=19, bg="#641E16", command= erase_func, text="Erase", fg="#FEF9E7", font=("Optima", 10, "bold"))
button_erase.place(rely=0.843, relx=0.3, anchor=E)

button_import = Button(window, width=19, command=import_func, bg="#641E16", text="Import", fg="#FEF9E7", font=("Optima", 10, "bold"))
button_import.place(rely=0.843, relx=0.867, anchor=E)

window.mainloop()
