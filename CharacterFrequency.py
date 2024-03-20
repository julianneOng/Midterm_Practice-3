my_string = input("Enter a string : ")
my_string = "HelloWorld"
count = {}

for letter in my_string:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

print("Character frequency:")
for key, value in count.items():
    print(f"{key} {value}")
