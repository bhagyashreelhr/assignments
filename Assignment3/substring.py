# Program to check if a substring is present in a given string

# Function to check if a substring is present in a given string

def check(str1, sstr):
   
    if (str1.find(sstr) == -1):
        print(sstr,"SUBSTRING IS NOT PRESENT IN THE GIVEN STRING")
   
    else:
        print(sstr,"SUBSTRING IS PRESENT IN THE GIVEN STRING")

# Take input from the user 

str1 = input("Enter the string ::>")
sstr = input("Enter Substring ::>")
check(str1, sstr)

