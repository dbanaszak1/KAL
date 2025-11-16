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

if __name__ == "__main__":
    p = 7
    A, B = 3, 6
    P = (3, 5)
    Q = (3, 5)
    R = add_points(P, Q, A, p)
    print(f"P = {P}, Q = {Q}, P⊕Q = {R}")
