def mod_exp(b: int, k: int, n: int) -> int:
    """
    Efektywne potęgowanie modularne: oblicza b^k mod n
    przy użyciu algorytmu iterowanego podnoszenia do kwadratu.
    """
    result = 1
    base = b % n  # redukujemy bazę modulo n

    while k > 0:
        # Jeśli najmłodszy bit wykładnika to 1 → mnożymy
        if k % 2 == 1:
            result = (result * base) % n
        # Przechodzimy do kolejnego bitu (dzielimy przez 2)
        k //= 2
        base = (base * base) % n  # podnosimy bazę do kwadratu

    return result

b = 7
k = 128
n = 31

print(f"{b}^{k} mod {n} = {mod_exp(b, k, n)}")