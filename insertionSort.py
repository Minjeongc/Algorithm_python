def insertionSort (num):
    for i in range(1, len(num)):
        for j in range(i, 0, -1):
            if num[j] < num[j-1]:
                num[j], num[j-1] = num[j-1], num[j]
            else:
                break
        print(num)
    return num

if __name__ == "__main__":
    array = list(map(int, input().split()))
    insertionSort(array)
