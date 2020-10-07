# Program to sort python dictionary by key or value
def add(keys,values):
    dictionary={}
    dictionary[keys]= values
    return dictionary

#Function to sort dictionary by key 
def sortdictionary(num):
    d={}
    for i in range(num):
        keys = input("add keys=")
        values = input("add values=")
        d.update(add(keys,values))

    newkeys = sorted(d.keys())
    for i in newkeys:
        print((i, d.get(i)),end=" ")

# Take length of dictionary from user
num = int(input("Enter length of dictionary"))
sortdictionary(num)

