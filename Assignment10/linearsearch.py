# Python program for linear search

def linearSearch(list1, key):
   #Return index of key in list1 & return -1 if key not present
   for i in range(len(list1)):
       if list1[i] == key:
           return i
   return -1

list1 = input('Enter the list of numbers: ')
list1 = list1.split()
list1 = [int(x) for x in list1]
key = int(input('The number to search for: '))

index = linearSearch(list1, key)
if index < 0:
   print('{} is not present in the list'.format(key))
else:
   print('{} is present in the list at index {}'.format(key, index))


