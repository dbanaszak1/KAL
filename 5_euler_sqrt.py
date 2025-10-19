def mod_exp(b: int, k: int, n: int) -> int:
    result = 1
    base = b % n
    while k > 0:
        if k % 2 == 1:
            result = (result * base) % n
        k //= 2
        base = (base * base) % n
    return result


def sqrt_mod_p(b: int, p: int) -> int:
    """
    Oblicza pierwiastek kwadratowy b w ciele Zp,
    dla liczby pierwszej p ≡ 3 (mod 4), zakładając że b jest resztą kwadratową.
    """
    if b % p == 0:
        return 0  # pierwiastek 0 to 0
    if p % 4 != 3:
        raise ValueError("p musi spełniać warunek p ≡ 3 (mod 4)")

    # Pierwiastek kwadratowy
    a = mod_exp(b, (p + 1) // 4, p)
    return a

p = 7  # 7 ≡ 3 mod 4
b = 2  # 2 jest resztą kwadratową w Z7, bo 3^2 = 2 mod 7

a = sqrt_mod_p(b, p)
print(f"Pierwiastek kwadratowy {b} w Z{p} to {a}")
print(f"Sprawdzenie: {a}^2 mod {p} = {(a*a) % p}")