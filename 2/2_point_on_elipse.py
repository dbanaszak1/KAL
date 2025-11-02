import secrets

def legendre_symbol(a, p):
    """Zwraca symbol Legendre’a (a|p): 1 jeśli reszta kwadratowa, -1 jeśli nie, 0 jeśli a ≡ 0."""
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def sqrt_mod_p(a, p):
    """Zwraca pierwiastek kwadratowy z a mod p, dla p ≡ 3 (mod 4)."""
    return pow(a, (p + 1) // 4, p)

def random_point_on_curve(A, B, p):
    """Znajduje losowy punkt P=(x,y) na krzywej y² = x³ + A x + B nad F_p."""
    while True:
        x = secrets.randbelow(p)
        rhs = (pow(x, 3, p) + A * x + B) % p  # prawa strona równania
        if legendre_symbol(rhs, p) == 1:      # sprawdzamy, czy istnieje pierwiastek
            y = sqrt_mod_p(rhs, p)
            return x, y

# Przykład (można połączyć z wcześniejszym kodem):
if __name__ == "__main__":
    # przykładowe dane z poprzedniego zadania
    from sympy import isprime
    import secrets

    # generujemy małe p dla demonstracji
    p = 7  # p ≡ 3 (mod 4)
    A, B = 3, 6
    x, y = random_point_on_curve(A, B, p)
    print(f"Punkt P = ({x}, {y}) należy do krzywej y² = x³ + {A}x + {B} (mod {p})")
