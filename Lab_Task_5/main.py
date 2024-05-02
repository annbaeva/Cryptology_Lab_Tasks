from timePad import OneTimePad

if __name__ == '__main__':
    a = OneTimePad(message="The program in all grades is designed to ensure that students build a solid foundation in mathematics", key="mathematics")

    print("Encoding: ")
    #існують символи, які Пайтон не підтримує і відображає їх як прямокутники
    print(a.encode())
    print()
    print("Decoding:")
    print(a.decode(key="mathematics"))
    print()
    print("False Decoding:")
    print(a.decode(key="triangle"))
