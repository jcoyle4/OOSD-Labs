def avg(a, b, c):
    return (a + b + c) / 3


def main():
    a = int(input("First Number:"))
    b = int(input("Second Number:"))
    c = int(input("Third Number:"))



    print("The average of", a, ",", b, "&", c, "is", avg(a, b, c))


main()