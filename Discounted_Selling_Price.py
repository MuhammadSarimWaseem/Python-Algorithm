# Discounted Selling price is to be calculated if original selling price and discount percentage
# is given. Write a program to calculate and print discounted selling price of the user given
# two inputs (1) original selling price and (2) discounted selling price.


original_price = int(input("Enter the Original price:"))
discount = int(input("Enter the discount:"))
discounted_selling_price = original_price*discount/100
after_discount_price = original_price-discounted_selling_price
print("your selling price after discount is:%f" % after_discount_price)


# Write a program to calculate and print the original selling price if the discounted selling
# price and discount percentage is entered by the user.


discounted_selling_price = int(input("Enter the discounted selling price:"))
discount = int(input("Enter the discount:"))
original_price = discounted_selling_price*100/discount
print("your selling price original price is:%f" % original_price)
