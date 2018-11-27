def add_values(a, b=None):
    if not b:
        return a+1
    else:
        return a+b

number = add_values(1)
print(number)


