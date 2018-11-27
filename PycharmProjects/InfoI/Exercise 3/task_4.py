

n = int(input("Enter a number: "))

# while is_prime:
#     if yournumber > 1:
#         for i in range(2,yournumber):
#             if (yournumber % i == 0):
#                 is_prime = False
#     else:
#         print(yournumber, "is not a prime number, as it is smaller than 1")
#     break
#
# if is_prime == True and yournumber > 1:
#     print(yournumber, "is a prime number")
# elif is_prime == False and yournumber > 1:
#     print(yournumber, "is not a prime number")




is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False





