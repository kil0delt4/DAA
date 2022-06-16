#### MERGE SORT ####
def mergeSort(arr):
    if(len(arr) < 2):
        return arr;
    
    mid = len(arr)//2;
    left = mergeSort(arr[:mid]);
    right = mergeSort(arr[mid:]);
    return merge(left, right);

def merge(left, right):
    result = []
    while(len(left) > 0 and len(right) > 0):
        if(left[0] <= right[0]):
            result.append(left[0]);
            left = left[1:];
        else:
            result.append(right[0]);
            right = right[1:];
    while(len(left) > 0):
        result.append(left[0]);
        left = left[1:];
    while(len(right) > 0):
        result.append(right[0]);
        right = right[1:];
    return result;
        
        
#### QUICK SORT ####
def quickSort(arr, left, right):
    if(left < right):
        pivot = partition(arr, left, right);
        quickSort(arr, left, pivot-1);
        quickSort(arr, pivot+1, right);
        
def partition(arr, left, right):
    pivot = arr[right];
    i = left;
    for j in range(left, right):
        if(arr[j] <= pivot):
            arr[i], arr[j] = arr[j], arr[i];
            i += 1;
    swap(arr, i, right);
    return i;

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i];

#### MAIN ####
if __name__ == "__main__":
    arr = [5,4,3,2,1];
    print(mergeSort(arr));
    quickSort(arr, 0, len(arr)-1)
    print("Sorted Array is: ", arr);