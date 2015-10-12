
book_price = eval(input("How much is the book? ")) # inputting a variable

store_discount = 0.6 # declaring a variable

store_price = 24.94 * store_discount # declaring a variable with an operation (multiplication)

total_copies = eval(input("Big Pink Elephant ")) # see line 2

shipping_cost = 3 + (total_copies - 1) * .75 # see line 6

print("The total cost for the books and shipping is", shipping_cost + (store_price * total_copies))
                # a print statement, where the output is a string and the result of an equation