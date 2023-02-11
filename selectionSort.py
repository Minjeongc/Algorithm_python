## 0번째 인덱스 ~ n-1번째 인덱스 값을 비교
## 가장 작은 값을 0번 인덱스의 값과 바꿈. 
## 1번째 인덱스 ~ n-1번째 인덱스 값을 비교
## 가장 작은 값을 1번 인덱스의 값과 바꿈. 

def selectionSort (input) :
  length = len(input)
  tmp = 0
  for i in range(length) :
    for j in range(length) :
      if (input[i] > input[j]) :
        ##swap
        tmp = input[j]
        input[j] = input[i]
        input[i] = tmp
        tmp = 0


if __name__=="__main__":
    num = []

    num = list(map(int, input().split()))
    
    selectionSort(num)
    for i in num:
        print(i)
