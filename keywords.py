#and 

a = True
b = False

result = a and b
print(result)

#not

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return not is_even(num)

numbers = {1,2,3,4,5}

for number in numbers:
    if is_odd(number):
        print(f"the {number} is  odd")
    else:
        print(f"the {number} is even")







