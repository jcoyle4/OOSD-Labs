def area(L, W): # defining a new function with two parameters
    return L * W # the return of the function, i.e. go back to the main function with the result of this equation


def perimeter(L, W):
    return L + L + W + W


def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    Area = area(length, width) # tell the main function to go to the function "area" and bring length and width with it
    Perimeter = perimeter(length, width) # as per the last function

    print("The area =", Area, "and the perimeter =", Perimeter)

main()