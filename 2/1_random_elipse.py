import secrets
from sympy import isprime

def generate_prime_3mod4(bits=300):
    """Generuje losową liczbę pierwszą p ≡ 3 (mod 4) o zadanej długości bitów."""
    while True:
        # losuj kandydata w odpowiednim zakresie
        p = secrets.randbits(bits)
        # ustaw najwyższy bit (żeby miała dokładnie 'bits' bitów)
        p |= (1 << (bits - 1)) | 3  # zapewnia też p ≡ 3 (mod 4)
        if isprime(p):
            return p

def generate_curve(p: int):
    """Generuje losową krzywą eliptyczną y² = x³ + A x + B nad F_p."""
    while True:
        A = secrets.randbelow(p)
        B = secrets.randbelow(p)
        # dyskryminant Δ = -16(4A³ + 27B²), wystarczy sprawdzić wewnętrzny czynnik
        if (4 * pow(A, 3, p) + 27 * pow(B, 2, p)) % p != 0:
            return A, B

if __name__ == "__main__":
    p = generate_prime_3mod4(300)
    A, B = generate_curve(p)
    print("Wygenerowano krzywą eliptyczną nad F_p:")
    print(f"p = {p}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"Równanie: y^2 = x^3 + {A}x + {B} (mod {p})")
