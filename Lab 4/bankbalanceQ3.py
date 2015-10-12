print("A program to calculate Interest")
principle = float(input("How much money did you put into the bank?"))
rate = float(input("What interest are you getting?"))
periods = float(input("How long will the money be in the bank for?"))

rate /= 100

for x in range (1, 4 * int(periods)):
    quarter_balance = principle + (principle * rate)
    principle = quarter_balance
    print(quarter_balance)


