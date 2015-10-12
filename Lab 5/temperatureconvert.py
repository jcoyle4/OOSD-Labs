def cel_to_fah(degC):
    return degC * (9/5) + 32

def cel_to_kel(degC):
    return degC + 273.15

def cel_to_rank(degC):
    return (degC + 273.15) * (9/5)

def main():
    """
    for degC in range (-30, 70, 10):
        degF = cel_to_fah(degC)
        degK = cel_to_kel(degC)
        degR = cel_to_rank(degC)
        print("Celcius:", degC, "Kelvin:", round(degK, 2), "Fahrenheit:", round(degF, 2), "Rankine:", round(degR, 2))
    """
    degC = float(input("How hot is it?"))
    degF = cel_to_fah(degC)
    print("It is", round(degF, 2), "degrees Fahrenheit")
    if degC > 25:
        print("GO OUTSIDE NOW!!")
    elif degC <= 25 and degC > 15:
        print("Its quite Hot")
    elif degC <= 15 and degC > 10:
        print("I'd still have a BBQ")
    elif degC <= 10 and degC > 5:
        print("Id still only wear a hoodie.")
    elif degC <= 5 and degC > 0:
        print("Time for a coat")
    elif degC <= 0:
        print("Now THATS an Irish summer")
    else:
        print("Are you sure you know what a degree celcius is?")


main()