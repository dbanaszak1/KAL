def power(b: int, k: int, n: int) -> int:
    """
    Efektywne potęgowanie modularne: oblicza b^k mod n
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


def is_quadratic_residue(b: int, p: int) -> bool:
    """
    Sprawdza, czy b jest resztą kwadratową modulo liczby pierwszej p.
    """
    if b % p == 0:
        return True

    # Obliczamy b^((p-1)//2) mod p
    euler_value = power(b, (p - 1) // 2, p)

    return euler_value == 1

p = 23
for b in range(1, p):
    print(f"{b:2d} -> {is_quadratic_residue(b, p)}")