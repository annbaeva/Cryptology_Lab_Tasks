import string

# l = [ ord(a) ^ ord(b) for a,b in zip(s1,s2)

LETTERS = ''.join(chr(i) for i in range(128))
unicode_letters = [ord(i) for i in LETTERS]


def make_key_like_message(key, message):
    key_new = (key * (len(message) // len(key) + 1))[:len(message) + 1]
    return key_new

class OneTimePad:
    dict_letters = {k: v for k, v in zip(LETTERS, unicode_letters)}
    reversed_letters = {v: k for k, v in dict_letters.items()}

    def __init__(self, message, key):
        self.message = message.replace(" ","")
        self.key = key

    def encode(self):
        encoded_message = ""
        stret_key = make_key_like_message(self.key,self.message)
        for i in range(len(self.message)):
            new_symbol = OneTimePad.dict_letters[self.message[i]] ^ OneTimePad.dict_letters[stret_key[i]]
            encoded_message+=OneTimePad.reversed_letters[new_symbol]

        return encoded_message



    def decode(self,key):
        decoded_message = ""
        encoded_message = self.encode()
        stret_key = make_key_like_message(key, self.message)
        for i in range(len(self.message)):
            new_symbol = OneTimePad.dict_letters[encoded_message[i]] ^ OneTimePad.dict_letters[stret_key[i]]
            decoded_message += OneTimePad.reversed_letters[new_symbol]
        return decoded_message



