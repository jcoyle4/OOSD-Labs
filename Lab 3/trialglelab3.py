from math import sqrt


def hypotenuse(opp, adj):
    return sqrt((opp ** 2) + (adj ** 2))


def main():
    opp = int(input("Side of Opposite:"))
    adj = int(input("Side of Adjacent:"))

    print("Hypotenuse =", hypotenuse(opp, adj))


main()