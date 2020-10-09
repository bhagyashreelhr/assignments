# Python program for binary search
def binarySearch(sorted_list, length, key):
    start = 0
    end = length - 1

    while start <= end:
        mid = int((start + end)/2)

        if key == sorted_list[mid]:
            print("The entered number %d is present at position: %d" % (key, mid))
            return -1
        elif key < sorted_list[mid]:
            end = mid - 1
        elif key > sorted_list[mid]:
            start = mid + 1
    print("Element not found")
    return -1

# Take a list of numbers from user & sort it then search the element
list2 = []

size = int(input("Enter size of the list: "))

for n in range(size):
    digits = int(input("Enter any number: "))
    list2.append(digits)

list2.sort()
print('\nThe sorted list is: ', list2)

num = int(input("\nEnter the number to search: "))

binarySearch(list2, size, num)

