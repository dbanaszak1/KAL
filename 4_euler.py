def mod_exp(b: int, k: int, n: int) -> int:
    result = 1
    base = b % n
    while k > 0:
        if k % 2 == 1:
            result = (result * base) % n
        k //= 2
        base = (base * base) % n
    return result


def is_quadratic_residue(b: int, p: int) -> bool:
    """
    Sprawdza, czy b jest resztą kwadratową modulo liczby pierwszej p.
    Wykorzystuje twierdzenie Eulera.
    """
    if b % p == 0:
        return True  # 0 zawsze jest resztą kwadratową (0^2 ≡ 0 mod p)

    # Obliczamy b^((p-1)//2) mod p
    euler_value = mod_exp(b, (p - 1) // 2, p)

    # Jeśli wynik == 1 → reszta kwadratowa
    return euler_value == 1

p = 23  # liczba pierwsza
for b in range(1, p):
    print(f"{b:2d} -> {is_quadratic_residue(b, p)}")