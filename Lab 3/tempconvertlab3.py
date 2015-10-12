def convert(C):
    return (C * 1.8) + 32


def main():
    Cdeg = float(input("How hot is it in celsius?"))
    print("It is this temp in Farenhite:", convert(Cdeg))

main()