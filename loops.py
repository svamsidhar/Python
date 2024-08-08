
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
word = ['one','two','three','four']
for number in word:
   print(f"{number}")

#while break continue statements

count = 2

while count <= 20:
    if count == 10:
        print("count is equal to 10 iteration stops")
        break
    elif count % 2 == 0:
         print("count is even,moving to next iteration")
         count += 1
         continue
    print(f"current count is {count}")
    count += 1



