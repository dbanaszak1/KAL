import secrets

def legendre_symbol(a, p):
    """Sprawdza czy istnieje pierwisatek"""
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def sqrt_mod_p(a, p):
    """Zwraca pierwiastek kwadratowy z a mod p, dla p = 3 (mod 4)."""
    return pow(a, (p + 1) // 4, p)

def random_point_on_curve(A, B, p):
    """Znajduje losowy punkt P=(x,y) na krzywej y2 = x3 + A x + B nad F_p."""
    while True:
        x = secrets.randbelow(p)
        rhs = (pow(x, 3, p) + A * x + B) % p
        if legendre_symbol(rhs, p) == 1:
            y = sqrt_mod_p(rhs, p)
            return x, y

if __name__ == "__main__":
    p = 7  # p = 3 (mod 4)
    A, B = 3, 6
    x, y = random_point_on_curve(A, B, p)
    print(f"Punkt P = ({x}, {y}) należy do krzywej y2 = x3 + {A}x + {B} (mod {p})")
