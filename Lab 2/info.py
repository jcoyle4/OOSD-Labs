print("I will tell you your life Story, but I need to know a bit about you:")

age = int(input("How old will you be on your next birthday?"))
pet = input("Do you own a cat or a dog? (Enter C, D)")
siblings = input("Do you have brothers or Sisters? (Enter B, S)")

print("You were", age - 1, "on your last birthday! An interesting start!")

if pet == "C":
    print("You were always more of a Dog person")

elif pet == "D":
    print("You were always more of a Cat person")

else:
    print("A Snake person eh?!")

if siblings == "B" or "S":
    print("You really were always the center of attention!")

else:
    print("Like me, you always did prefer the company of others!")
