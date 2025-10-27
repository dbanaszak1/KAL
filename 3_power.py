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

b = 7
k = 128
n = 31

print(f"{b}^{k} mod {n} = {power(b, k, n)}")