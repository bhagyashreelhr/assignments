# Python Program to remove duplicate words from a sentence

from collections import Counter
# Function to remove duplicate words from a sentence
def removeDuplicate(string):
   if string == 'x':
       print("Exit")
       exit();
   else:
       string = string.split(" ")
       for i in range(0, len(string)):
           string[i] = "".join(string[i])
           duplicate = Counter(string)
           s = " ".join(duplicate.keys())
       print ("After removing duplicate words, the sentence is :",s)

# Take input from user 
if __name__ == "__main__":
   string = input("Enter any sentence\n")
   removeDuplicate(string)

