# bubbleSort
# 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
# n과 n+1의 값을 비교하여 정렬합니다. 
# 그래서 맨 마지막 가장 큰수를 찾고 다시 앞부터 돌려서 그다음큰 숫자 찾고 이런식으로 정렬함.
def bubbleSort(num,n):
    temp = 0
    for i in range(n): 
        for j in range(n-1-i): 
            if (num[j]>num[j+1]):
                temp = num[j] 
                num[j] = num[j+1]
                num[j+1] = temp
        print(num)
                
if __name__=="__main__":
    
    num = list(map(int, input().split()))
    n = len(num)
    bubbleSort(num,n)

