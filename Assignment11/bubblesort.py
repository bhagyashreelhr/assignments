# Python program for bubble sort
def bubbleSort(array):
    n = len(array)

    # Traverse through all array elements 
    for i in range(n-1):
        # Last i elements are already in place 
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1 
            # Swap if the element found is greater than the next element
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

def main():
    array = list()
    Number = input('Enter how many elements you want: ')
    print('Enter numbers in array: ')
    for i in range(int(Number)):
        n = input('Number : ')
        array.append(int(n))
    print('Given array is:',array)
    bubbleSort(array)

    # Print the sorted array
    print('Sorted array is: ')
    for i in range(len(array)):
        print("%d" %array[i])

if __name__ == "__main__":
    main()

