
# for loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

word = ["hello world"]
for leter in word:
    print(leter)

# While loop
count = 1
while count <= 6:
 print(count)
 count += 1

# for 
word = ['one','two','three']
for number in word:
   print(number)

# if
word = ['one','two','three']
if 'one' in word:
   print("it is there")
else:
   print("it is not there")

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

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if is_odd(number):
        print(f"{number} is odd")
    else:
        print(f"{number} is even")






