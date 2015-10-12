book_price = eval(input("How much is the book?"))

store_discount = eval(input("From 0 to 100 percent, do you get a discount?"))

store_discount = (100 - store_discount)/100


store_price = 24.94 * store_discount

total_copies = eval(input("How many copies did you buy?"))

shipping_cost = 3 + (total_copies - 1) * .75

print("The total cost for the books and shipping is", shipping_cost + (store_price * total_copies))