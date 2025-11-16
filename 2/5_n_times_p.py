def add_points(P, Q, A, p):
    """
    Oblicza sumę punktów R = P xo Q na krzywej eliptycznej y2 = x3 + A x + B nad F_p.
    """
    # Punkt w nieskończoności reprezentujemy przez None
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    # Przypadek: P = -Q -> wynik to punkt w nieskończoności
    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    # Obliczenie lambda
    if P != Q:
        numerator = (y2 - y1) % p
        denominator = pow((x2 - x1) % p, -1, p)
        lam = (numerator * denominator) % p
    else:
        numerator = (3 * x1 * x1 + A) % p
        denominator = pow((2 * y1) % p, -1, p)
        lam = (numerator * denominator) % p

    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return x3, y3

def scalar_mult(n, P, A, p):
    """
    Oblicza Q = nP na krzywej eliptycznej y² = x³ + A x + B nad F_p.
    Algorytm double-and-add.
    """
    R = None          # Punkt w nieskończoności (neutralny element)
    Q = P

    while n > 0:
        if n & 1:     # jeśli najmłodszy bit to 1 → dodaj Q
            R = add_points(R, Q, A, p)
        Q = add_points(Q, Q, A, p)  # podwój Q
        n >>= 1       # przesunięcie bitowe (dzielenie przez 2)
    return R

if __name__ == "__main__":
    p = 7
    A, B = 3, 6
    P = (3, 5)
    n = 9
    Q = scalar_mult(n, P, A, p)
    print(f"{n}P = {Q}")
