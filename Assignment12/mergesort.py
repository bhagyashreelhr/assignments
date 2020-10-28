# Python program for mergesort 
def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements into two halves
        L = arr[:mid]
        R = arr[mid:]
        # Sorting the two halves
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1

        # Check if any element was left 
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1

# Function to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end =' ')
    print()

def main():
    arr = list()
    Number = input('Enter how many elements you want: ')
    print('Enter numbers in array: ')
    for i in range(int(Number)):
        n = input('Number : ')
        arr.append(int(n))
    print ('Given array is: ', end ='\n')
    printList(arr)
    mergeSort(arr)

    # Print the sorted array
    print('Sorted array is: ', end ='\n')
    printList(arr)

if __name__ == "__main__":
    main()

