# Python Program to find Largest Number in a List 

# Function to find largest number in a list
def largestNumber(x):
        List = []
        if x > 0:
            for i in range(x):
                ele = int(input("Enter elements :"))
                List.append(ele)

            List.sort()
            List.reverse()
            print("The Largest Element in this List is : ", List[0])
        else:
            print('Oops ! Wrong Input')

# Take input from user
Number = int(input("Please enter the Total Number of List Elements: "))
largestNumber(Number)

