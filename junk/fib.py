
def fib():
    n1 = 0
    n2 = 1
    user = float(input("Alegeti numarul limita pentru sirul lui Fibonacci: "))
    n3 = n1 + n2
    print("_______________________________________________________________________________________")
    print(f"Numarul din sirul Fibonacci este: {n1}")
    print("_______________________________________________________________________________________")
    print(f"Numarul din sirul Fibonacci este: {n2}")
    while n3 < user:
        print("_______________________________________________________________________________________")
        print(f"Numarul din sirul Fibonacci este: {n3}")
        n1 = n2
        n2 = n3
        n3 = n1 + n2
    print("_______________________________________________________________________________________")
    print("All done!")
    print("_______________________________________________________________________________________")

fib()

