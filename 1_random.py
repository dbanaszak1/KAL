import secrets

def random_element(k: int) -> int:
    a = 1103515245
    c = 12345
    m = 2 ** 31

    seed = secrets.randbits(31)

    x = (a * seed + c) % m
    n = 2 ** k
    return x % n

for _ in range(100):
    print(random_element(8))
