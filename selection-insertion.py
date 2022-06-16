def insertionSort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count += 1
        arr[j + 1] = key
    print(count)
    return arr
        
def selectionSort(arr):
    count = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            count += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(count)
    return arr

if __name__ == "__main__":
    U = [1, 2, 3, 4, 5, 6]
    V = [6, 5, 4, 3, 2, 1]
    W = [1, 3, 4, 5, 2, 6]
    X = [1, 1, 1, 1, 1, 1]
    print("Insertion Sort: ")
    print(insertionSort(X))
    print("Selection Sort: ")
    print(selectionSort(X))

    # # Get the array to sort
    # arr = input("Enter the array to sort: ")
    # # Convert the array to a list
    # arr = arr.split()
    # # Convert the list to an integer list
    # arr = [int(i) for i in arr]
    # # Sort the array
    # for i in range(1, len(arr)):
    #     j = i
    #     while j > 0 and arr[j] < arr[j-1]:
    #         arr[j], arr[j-1] = arr[j-1], arr[j]
    #         j -= 1
    # # Print the sorted array
    # print("The sorted array is: ", arr)
