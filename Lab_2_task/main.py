from tkinter import *
import string
from random import shuffle
numbers = [i for i in range(10,99)]

shuffle(numbers)
a = [k for k in string.ascii_letters]
alphabet = {k:v for k,v in zip(a,numbers)}
alphabet_reverse = {v:k for k,v in alphabet.items()}


def translate():
    sentence = get_entry()
    result_trn = ""
    for i in sentence:
        if i in alphabet.keys():
            result_trn += str(alphabet[i])
        else:
            pass
    entry_end.insert(0, result_trn)

def inverse_translate():
    numbers = get_entry_r()

    result_stn = ""
    counter = 0
    while counter<len(numbers)-1:
        a =numbers[counter]
        b =numbers[counter+1]
        chyslo = int(a+b)
        if chyslo in alphabet_reverse:
            result_stn += str(alphabet_reverse[chyslo])
        else:
            pass
        counter += 2
    entry_end_r.insert(0, result_stn)


window = Tk()
window.configure(background="#FDEBD0")
window.geometry("1000x650")
window.resizable(height=False, width=False)

frame1 = Frame(window, height=1000, width=500, bg="#641E16")
frame1.pack_propagate(False)
frame1.pack(side=LEFT)

label_in_window = Label(window, height=5, width=73, text="Decode", bg="#641E16", font=("CASTELLAR", 16, "bold"),
                        fg="#F5EED3")
label_in_window.pack_propagate(False)
label_in_window.pack()

# LEFT SIDE
lable_in_frame1 = Label(frame1, height=5, width=73, text="Encode", bg="#FDEBD0", font=("CASTELLAR", 16, "bold"))
lable_in_frame1.pack_propagate(False)
lable_in_frame1.pack(side=TOP)

lable_in_frame2 = Label(frame1, height=1, width=33, text="Enter sentence", bg="#FDEBD0", font=("Gentium Basic", 14))
lable_in_frame2.pack_propagate(False)
lable_in_frame2.pack(pady=45)

entry_start = Entry(frame1, background="#381A07", width=30, font=("Bodoni MT Black", 13), fg="#FAD7A0")
entry_start.pack()


def get_entry():
    inform = entry_start.get()
    print(inform)
    return inform


button = Button(frame1, width=19, bg="#FDEBD0", text="Translate", command=translate, fg="black", font=("Optima", 10, "bold"))
button.pack(pady=90)

lable_in_frame3 = Label(frame1, height=1, width=33, text="Result", bg="#FDEBD0", font=("Gentium Basic", 14))
lable_in_frame3.pack_propagate(False)
lable_in_frame3.pack(side=BOTTOM, pady=45)

entry_end = Entry(frame1, background="#381A07", width=35, font=("Century", 13), fg="#FAD7A0")
entry_end.pack(side=BOTTOM)

# RIGHT SIDE
# width=33, text="Enter sentence", bg="#FDEBD0", font=("Gentium Basic",14)

lable_in_window2 = Label(window, height=1, width=33, text="Enter sentence", bg="#641E16", font=("Gentium Basic", 14),
                         fg="#FEF9E7")
lable_in_window2.pack_propagate(False)
lable_in_window2.pack(pady=45)

entry_start_r = Entry(window, background="#DA9760", width=35, font=("Century", 13))
entry_start_r.pack()


# Zamina
def get_entry_r():
    infa = entry_start_r.get()
    print(infa)
    return infa


button_right = Button(window, width=19, bg="#641E16", text="Translate", fg="#FEF9E7", font=("Optima", 10, "bold"), command=inverse_translate)
button_right.pack(pady=90)

lable_in_window3 = Label(window, height=1, width=33, text="Result", bg="#641E16", font=("Gentium Basic", 14),
                         fg="#FEF9E7")
lable_in_window3.pack_propagate(False)
lable_in_window3.pack(side=BOTTOM, pady=45)

entry_end_r = Entry(window, background="#DA9760", width=30, font=("Bodoni MT Black", 13))
entry_end_r.pack(side=BOTTOM)


inverse_translate()

window.mainloop()
