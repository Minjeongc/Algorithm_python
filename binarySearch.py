def binarySearch(target, data):
    data.sort() #데이터를 오름차순으로 정렬
    start = 0
    end = len(data) - 1

    while start <= end :
        mid = (start+end) // 2

        if data[mid] == target :
            return mid
        elif data[mid]< target :
            start = mid+1
        else:
            end = mid - 1
    return None

#이진탐색 재귀

def binarySearchRecursion(target, start, end, data):
    if start > end :
        return None
    mid = (start+ end) //2 
    
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    return binarySearchRecursion (target, start, end, data)