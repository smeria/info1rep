# Please do not modify this part of the code!
price_banana = 1.5
price_milk = 2.0
number_of_bananas_purchased = 4
number_of_milks_purchased = 3

# Your code goes here
# Define the hight of the promotion
promotion_percentage = int(input('Enter a integer number from 0 to 100:'))

#subtotal of the purchase
subtotal_price = (price_banana*number_of_bananas_purchased +price_milk*number_of_milks_purchased)
print ("The subtotal of your purchase is " + str(subtotal_price))

# savings given the promotion
savings = promotion_percentage/100 *subtotal_price
print("Your savings are "+str(savings))

# total price
total_price = subtotal_price-savings
print("The total price of your purchase is "+str(total_price))




