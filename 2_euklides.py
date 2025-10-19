def extended_gcd(a: int, b: int):
    """
    Zwraca (d, x, y) takie, że d = gcd(a, b) oraz a*x + b*y = d
    """
    if b == 0:
        return (a, 1, 0)
    else:
        d, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (d, x, y)


def mod_inverse(b: int, n: int):
    """
    Oblicza odwrotność elementu b w grupie Φ(n), czyli b^(-1) mod n
    """
    d, x, y = extended_gcd(b, n)
    if d != 1:
        # Nie istnieje odwrotność, jeśli b i n nie są względnie pierwsze
        raise ValueError(f"Odwrotność nie istnieje: gcd({b}, {n}) = {d}")
    else:
        # x może być ujemne — redukujemy mod n
        return x % n


n = 26
b = 7

inv = mod_inverse(b, n)
print(f"Odwrotność {b} modulo {n} to {inv}")
print(f"Sprawdzenie: {(b * inv) % n} == 1")

