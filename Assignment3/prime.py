# Python program to check if a number is prime or not  
def isPrime(number):
    try:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    print(number, "this is not a prime number")
                    break
            else:
                print(number, "this is a prime number")

    except TypeError:
        print("Wrong Input")

# Take input from the user
number = int(input("Enter any number: "))
result = isPrime(number)
