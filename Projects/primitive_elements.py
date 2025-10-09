'''
Author: Collin Tautfest
Date: 2025-10-09

Project: Modtabs Primitive elements
'''
import math

def is_prime(x):
    """
    checks if a element is prime
    """
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# Helper: check if n = p^k for some prime p
def is_prime_power(n, require_odd=False):
    # Try every possible prime base up to sqrt(n)
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0 and is_prime(p):
            if require_odd and p == 2:
                continue  # skip even prime if we need odd only

            m = n
            # Divide out all factors of p
            while m % p == 0:
                m //= p

            # If we reduced all the way to 1, it's a perfect prime power
            if m == 1:
                return True

    # Special case: n itself is prime (p^1)
    if is_prime(n):
        if require_odd and n == 2:
            return False
        return True

    return False

def euler_totient(n):
    """
    Compute Euler's Totient φ(n).
    """
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def prime_factors(num):
    """
    Return the set of prime factors of number.
    """
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 2:
        factors.add(num)
    return factors

def gcd(a, b):
    """
    Gets the Greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

def get_primitive_elements(n):
    # output
    primitives = []
    # check if n is in set {2, 4, p^k or 2p^k} where p is a prime number
    if n in {2, 4} or is_prime_power(n) or (n % 2 == 0 and is_prime_power(n // 2, require_odd=True)):
        # compute euler's totient formula for prime factors
        phi_n = euler_totient(n)

        factors = prime_factors(phi_n)
        

        for g in range(2, n):
            if gcd(g, n) != 1:
                # must be coprime
                continue
            is_primitive = True
            for p in factors:
                # If g^(φ(n)/p) ≡ 1 (mod n), g is NOT primitive
                if pow(g, phi_n // p, n) == 1:
                    is_primitive = False
                    break

            if is_primitive:
                primitives.append(g)


        if primitives:
            print(f"Primitive elements in Z_{n}: {primitives}")
    else:
        # if not in the set it cannot have primitves
        print("No primitives for Z_", n)

def main():
    """
    main function of program, will include multiple menu options in final version
    """

    x = 23 # placeholder number for input

    get_primitive_elements(x) # call primitive function


if __name__ == "__main__":
    main()