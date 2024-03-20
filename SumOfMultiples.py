x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the limit: "))
sum_of_x = 0
sum_of_y = 0
for i in range(z):
    if i % x == 0:
        sum_of_x += i
    if i % y == 0:
        sum_of_y += i
        
sum = sum_of_x + sum_of_y 

print(f"The sum of multiples of {x} or {y} up to {z} is", sum)