# Python Program to merge two dictionaries

# Function to merge two dictionaries
def mergeDictionary(dict1, dict2): 
   return(dict2.update(dict1)) 

# Driver code 
d1 = dict()
d2 = dict()
data = input('Enter Name & Roll separated by ":" ')
temp = data.split(':')
d1[temp[0]] = int(temp[1])
for key, value in d1.items():
   print('Name: {}, Roll: {}'.format(key, value))

data = input('Enter Name & Roll separated by ":" ')
temp = data.split(':')
d2[temp[0]] = int(temp[1])
for key, value in d2.items():
   print('Name: {}, Roll: {}'.format(key, value))

# Calling merge function
(mergeDictionary(d1, d2)) 
print("Dictionary after merging ::",d2)
