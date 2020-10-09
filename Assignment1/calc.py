# Python program for arithmetic operations on two numbers

# Function to Add two numbers
def add(num1, num2):
    return num1 + num2

# Function to Subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to Multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to Divide two numbers
def divide(num1, num2):

# Raise a ZeroDivisionError if a number is divided by 0
    try:
        x = num1 / num2
    except ZeroDivisionError:
        return "ZeroDivisionError"
    else:
        return x

# Main Function
def main():
    print("Please select Arithmetic Operation -\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n")

# Take input from the user
select = int(input("Select operations from 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")

# Call main function
    if __name__ == '__main__':
        main()
