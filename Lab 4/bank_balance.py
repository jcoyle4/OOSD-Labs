def simple_interest(principle, rate, periods):
    return principle + ((principle * rate) * periods)


def compound_interest(principle, rate, periods, compounds):
    return principle * (1 + (rate/compounds))**(compounds*periods)


def quarter_compounds(principle, rate, periods, checker):
    for x in range (1, 4 * int(periods) + 1):
        balance = principle + (principle * rate)
        principle = balance

        if checker == True:
            print("Quarter", x, "Balance:", round(balance, 2))

    return balance


def main():
    print("A program to calculate Interest")
    principle = float(input("How much money did you put into the bank?"))
    rate = float(input("What interest are you getting?"))
    periods = float(input("How long will the money be in the bank for?"))
    checker = False

    rate /= 100

    interest_type = int(input("Enter type: 1: Quarterly Compound, 2: Simple, 3: Normal Compound"))

    if interest_type == 1:
        q3 = quarter_compounds(principle, rate, periods, checker)

        print(principle, "at", rate * 100, "percent, compounded quarterly for", periods, "years, yields", round(q3, 2))

        checker = True
        q3 = quarter_compounds(principle, rate, periods, checker)

    elif interest_type == 2:
        sim_inst = simple_interest(principle, rate, periods)
        print("You will have", round(sim_inst, 2), "after", periods, "years, if you initially put in", principle)

    elif interest_type == 3:
        compounds = float(input("How many compounding periods?(1 for yearly, 12 for monthly)"))
        ans1 = round(compound_interest(principle, rate, periods, compounds),2)
        print("You will have", ans1, "after", periods, "years, if you initially put in", principle)
        response = input("Want to calculate for different compounding periods?")

        if response == "yes":
            compounds = float(input("Enter new compounding periods:"))
            ans2 = round(compound_interest(principle, rate, periods, compounds),2)
            print("You will have", ans2, "after", periods, "years, if you initially put in", principle)
            print("There is a difference of", round(ans1 - ans2, 2), "between your different compounding periods")

        else:
            return 0

    else:
        return 0


main()
