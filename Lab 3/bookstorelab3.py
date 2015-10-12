def discount(dis):
    return (100 - dis)/100


def store_price(p, dis):
    return p * dis


def total_store_price(SP, copies):
    return SP * copies


def shipping_cost(c):
    return 3 + ((c - 1) * .75)


def total(shipping, price):
    return shipping + price


def main():
    price = float(input("How much is the book?"))
    store_discount = float(input("Enter the store discount:"))
    Dis = discount(store_discount)
    SP = store_price(price, Dis)
    copies = int(input("How many copies did you buy?"))
    TSP = total_store_price(SP,copies)
    SC = shipping_cost(copies)
    print("The total cost is:", total(SC, TSP))

main()