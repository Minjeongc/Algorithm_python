def quickSort(arr , i , j):
    if i < j :
        pivot = parition(arr , i , j)
        quickSort(arr , i , pivot - 1)
        quickSort(arr , pivot+1 , j)

def parition (arr, s, e):
    pivot_index = s 
    pivot = arr[pivot_index]

    while s < e:
        while s < len(arr) and arr[s] <= pivot:
            s += 1
        
        while arr[e] > pivot:
            e -= 1

        if s < e:
            arr[s], arr[e] = arr[e] , arr[s]
        
    arr[e] , arr[pivot_index] = arr[pivot_index], arr[e]

    return e


if __name__ == "__main__":
    arr = [3,5,1,8,7,6,2,4]
    num = len(arr)
    quickSort(arr, 0, num-1)
    print(arr)