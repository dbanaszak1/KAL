# 1. suma(a, b)
def suma(a, b):
    return a ^ b

# 2. xtime(a)
def xtime(a):
    a <<= 1
    if a & 0b1_0000_0000:
        a ^= 0b1_0001_1011
    return a & 0b1111_1111

def iloczyn(a, b):
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0b1_0000_0000:
            a ^= 0b1_0001_1011
        a &= 0b1111_1111
        b >>= 1
    return result

def odwrotnosc(a):
    if a == 0:
        return 0
    result = 1
    base = a
    power = 254
    while power:
        if power & 1:
            result = iloczyn(result, base)
        base = iloczyn(base, base)
        power >>= 1
    return result

if __name__ == "__main__":
    a = 0b01010111
    b = 0b10000011

    print("suma =", bin(suma(a, b)))
    print("xtime =", bin(xtime(a)))
    print("iloczyn =", bin(iloczyn(a, b)))
    print("odwrotnosc =", bin(odwrotnosc(a)))
