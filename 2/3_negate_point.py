def negate_point(P, p):
    """
    Oblicza punkt przeciwny do danego punktu P = (x, y) na krzywej nad F_p.
    Zwraca -P = (x, -y mod p).
    """
    x, y = P
    return x, (-y) % p

if __name__ == "__main__":
    p = 7
    P = (3, 5)
    negP = negate_point(P, p)
    print(f"P = {P}")
    print(f"-P = {negP}")
