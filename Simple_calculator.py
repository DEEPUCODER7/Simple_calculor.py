# 📌 This is a calculator that adds, subtracts, multiplies, or divides two numbers

# Ask the user what they want to do
print("Welcome to My Calculator! 😃")
print("Choose one: +  -  *  /")

# Save their choice in a box
operation = input("What do you want to do? ")

# Ask for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Now check which operation they picked
if operation == "+":
    print("Answer is:", num1 + num2)
elif operation == "-":
    print("Answer is:", num1 - num2)
elif operation == "*":
    print("Answer is:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Answer is:", num1 / num2)
    else:
        print("Oops! Cannot divide by 0.")
else:
    print("Sorry, I don't understand this operation.")
