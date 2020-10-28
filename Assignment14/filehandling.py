# Python Program for File Handling operations
with open('mk.txt', 'w', encoding = 'utf-8') as f:
   #first line
   f.write('Most asked questions of 2020:\n')
   #second line
   f.write('1.When will the vaccine come?\n')
   #third line
   f.write('2.Am i audible?')

with open('mk.txt', 'r', encoding = 'utf-8') as f:
   content = f.readlines()

for line in content:
   print(line)

