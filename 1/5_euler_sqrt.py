def power(b: int, k: int, n: int) -> int:
    """
    Efektywne potęgowanie modularne
    """
    result = 1
    base = b % n

    while k > 0:
        # ostatni bit = 1 -> mnożenie
        if k % 2 == 1:
            result = (result * base) % n
        # next bit
        k //= 2
        base = (base * base) % n

    return result


def sqrt_mod_p(b: int, p: int) -> int:
    """
    Oblicza pierwiastek kwadratowy b w ciele Zp,
    """
    if p % 4 != 3:
        raise ValueError("p musi spełniać warunek p = 3 (mod 4)")

    # Pierwiastek kwadratowy
    a = power(b, (p + 1) // 4, p)
    return a

p = 7
b = 2

a = sqrt_mod_p(b, p)
print(f"Pierwiastek kwadratowy {b} w Z{p} to {a}")
