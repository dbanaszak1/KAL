import time


def lcg(k: int) -> int:
    # LCG — glibc
    a = 1103515245
    c = 12345
    m = 2 ** 31

    # seed:
    seed = int(time.time() * 1_000_000) % m

    x = (a * seed + c) % m

    n = 2 ** k
    return x % n



print(lcg(8))  # 8 bit
