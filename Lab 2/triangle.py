from math import sqrt

opp = int(input("Side of Opposite: "))
adj = int(input("Side of Adjacent: "))

hyp = sqrt((opp ** 2) + (adj ** 2))
print("Hypotenuse =", hyp)