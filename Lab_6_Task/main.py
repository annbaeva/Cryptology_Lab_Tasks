def euclid_extended(a, b, c_a=0, c_b=1):
    """шукає коефи для нсд ну і саме нсд"""
    if a % b == 0:
        return b, c_a, c_b
    else:
        q = a // b
        formula = a - b * q
        return euclid_extended(b, formula, c_a=c_b, c_b=(c_a - q * c_b))

def binpow(number, pow):
    if pow == 0:
        return 1
    elif pow % 2 == 1:
        return binpow(number, pow-1) * number
    else:
        b = binpow(number, pow//2)
        return b * b



def eiler_function(a, b):
    return (a - 1) * (b - 1)


a = binpow(10,10)
print(f"Binary power: {a}")

b, c_a, c_b = euclid_extended(19,9)
print(f"Euclid extended: {b}, {c_a}, {c_b}")

d = eiler_function(13,5)
print(f"Eiler function: {d}")

