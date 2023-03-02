#풀이 1 (메모리 사용 효율 떨어짐)
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_ = mergeSort(left)
    right_ = mergeSort(right)

    return merge(left_, right_)

def merge(left, right):
    i = j = 0
    sorted_list = []
    while (i< len(left) and j < len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list



#풀이2
def mergeSort2(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low,mid,high)
    
    def merge(low, mid, high):
        temp = []
        l , h = low , mid
        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1

        while h  < high :
            temp.append(arr[h])
            h += 1
        
        for i in range(low, high):
            arr[i]  = temp[i-low]
        
    return sort(0,len(arr))

        


if __name__ == "__main__":
    arr = [3,5,1,6,8,7,2,4]
    print(mergeSort(arr))

