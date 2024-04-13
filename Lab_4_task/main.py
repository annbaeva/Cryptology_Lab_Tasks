printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~'

symbols = {}

for i in range(len(printable)):
    symbols[printable[i]] = i + 1

symbols_reversed = {}
for key, value in symbols.items():
    symbols_reversed[value] = key

text = input("Enter text: ")
key = input ("Enter key: ")


def stretch_key(key, text):
    i = 0
    new_key = ""
    text_without_spaces = len(text.replace(" ",""))
    starter_key_lenght = len(key)
    while len(new_key) <= len(text):
        if i == starter_key_lenght:
            i -= starter_key_lenght
        new_key += key[i]
        i += 1
    return new_key


def encrypt(text, key):
    new_text = ""
    new_key = stretch_key(key, text)
    text_without_spaces = text.replace(" ", "")
    for i in range(len(text_without_spaces)):
        a = symbols[text_without_spaces[i]]
        b = symbols[new_key[i]]
        c = a + b
        if c > len(symbols):
            c -= len(symbols)
        new_text += symbols_reversed[c]

    return new_text


def decrypt(text, key):
    original_text = ""
    new_key = stretch_key(key, text)
    text_without_spaces = text.replace(" ", "")
    for i in range(len(text_without_spaces)):
        d = symbols[text_without_spaces[i]]
        e = symbols[new_key[i]]
        f = d - e
        if f <= 0:
            f += len(symbols)
        original_text += symbols_reversed[f]

    return original_text


text_d = encrypt(text, key)
print(text_d)
print(decrypt(text_d, key))

