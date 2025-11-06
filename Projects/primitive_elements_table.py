def order(a, p):
    """Find the multiplicative order of a mod p."""
    if a % p == 0:
        return 0
    k = 1
    val = a % p
    while val != 1:
        val = (val * a) % p
        k += 1
    return k

def primitive_elements(p):
    """Find all primitive elements of Z_p."""
    primitives = []
    for a in range(2, p):
        if order(a, p) == p - 1:
            primitives.append(a)
    return primitives

def print_table(p):
    """Prints a table of elements, their powers, and order."""
    print(f"\nMultiplicative group Z_{p}* (order {p-1})\n")
    print(f"{'a':>3} | {'Powers mod p':<40} | {'Order':>5} | Primitive")
    print("-" * 70)
    primitives = primitive_elements(p)
    
    for a in range(1, p):
        # Generate all powers up to order p-1
        powers = [str(pow(a, k, p)) for k in range(1, p)]
        ord_a = order(a, p)
        is_prim = "Yes" if a in primitives else "No"
        print(f"{a:>3} | {' '.join(powers):<40} | {ord_a:>5} | {is_prim}")

# Example run
if __name__ == "__main__":
    p = int(input("Enter a prime number p: "))
    print_table(p)
