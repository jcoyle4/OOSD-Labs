def surface_area(x):
    return 6 * (x ** 2)


def volume(x):
    return x ** 3


def main():

    for x in range (1, 1000):
        s_a = surface_area(x)
        vol = volume(x)
        if s_a == vol:
            print("Surface area and volume are equal,", vol, ", when width =", x)
            break
        elif s_a != vol:
            print("Surface Area =", s_a, "and volume =", vol, "for width =", x)
        else:
            return 0

main()