def is_prime(n: int) -> bool:
    """
    Sprawdza, czy n jest liczbą pierwszą.
    Prosta wersja: dzielenie przez wszystkie liczby od 2 do sqrt(n)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for n in [1, 2, 3, 4, 17, 19, 20]:
    print(f"{n} -> {is_prime(n)}")
