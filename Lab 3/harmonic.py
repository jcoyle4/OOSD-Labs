def harmonic(n):
    total = 0
    for k in range (1, n + 1):
        total += 1 / k
    return total

def main():
    n = int(input("Enter a positive integer:"))
    print("The sum of 1/k from k = 1 to", n, "is", round(harmonic(n), 1))

main()