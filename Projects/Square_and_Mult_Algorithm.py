'''
Author: Collin Tautfest 
Date: 2025-11-06

Project: Computes a large modular exponent
'''
def squareandmult(a,b,n):
    binary_b = bin(b)  # Convert exponent to binary
    output = 1
    a = a % n # reduce base first

    for bit in binary_b:
        # Always square
        output = (output * output) % n
        # if bit is 1 multiply
        if bit == '1':
            output = (output * a) % n
    
    return output

def main():
    while True:
        print("")
        print("========================================")
        print('The format is a^b (mod n)')
        
        print("")
        try:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            n = int(input("Enter n: "))
            print("========================================")
            output = squareandmult(a,b,n)
            print(f"{a}^{b} (mod {n}) is congruent to {output} (mod {n})")

        except ValueError:
            print("Invalid Input, please enter integers only")
if __name__ == "__main__":
    main()