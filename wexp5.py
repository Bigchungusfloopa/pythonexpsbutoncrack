# Conditional statements
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(str(num) + " is even")
else:
    print(str(num) + " is odd")

# For loop
num1 = int(input("Enter a range limit for for-loop: "))
for i in range(num1):
    if i % 2 == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")

# While loop
num2 = int(input("Enter a number for while-loop countdown: "))
while num2 != 0:
    if num2 % 2 == 0:
        print(str(num2) + " is even")
    else:
        print(str(num2) + " is odd")
    num2 -= 1

# Special handling for 0
print("0 is even")
