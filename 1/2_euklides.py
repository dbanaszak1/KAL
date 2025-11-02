def extended_euklides(a: int, b: int):
    """
    Zwraca (d, x, y) takie, że d = gcd(a, b) oraz a*x + b*y = d
    """
    if b == 0:
        return (a, 1, 0)
    else:
        d, x1, y1 = extended_euklides(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (d, x, y)


def mod_inverse(b: int, n: int):
    d, x, y = extended_euklides(b, n)
    if d != 1:
        raise ValueError(f"Odwrotność nie istnieje: gcd({b}, {n}) = {d}")
    else:
        # x może być ujemne — redukujemy mod n
        return x % n


n = 29
b = 8

inv = mod_inverse(b, n)
print(f"Odwrotność {b} mod {n} to {inv}")

