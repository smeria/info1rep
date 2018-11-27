# Please do not modify this part of the code!
special_character_set = "@/%&*_-"

is_valid = False

# Your code goes here
password = input('Your password: ')

countupper = 0
for i in password:
    if (i.isupper()):
        countupper=countupper+1

countlower = 0
for i in password:
    if (i.islower()):
        countlower=countlower+1

countdigits = 0
for i in password:
    if (i.isnumeric()):
        countdigits=countdigits+1

countspecialcharac = 0
for i in password:
    if i in special_character_set:
        countspecialcharac = countspecialcharac +1


while is_valid == False:

    if len(password) >= 8 and len(password) <= 30 and countupper >= 2 and countupper >= 2 and countdigits >= 1 and countspecialcharac == 1:
        is_valid=True
        print("Your password is valid!")
        break
    else:
        print("Your password is not valid!")
        break



