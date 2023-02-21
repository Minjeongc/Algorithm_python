# priorityQueue 클래스 이용해서 구현

from queue import PriorityQueue

que = PriorityQueue() #maxsize를 이용하여 사이즈를 조정할 수 있음. 

# put : 큐에 원소를 추가할 수 있음. 
# get : 큐에 원소를 삭제할 수 있음. 

que.get(7)
que.get(4)
que.put(1)
que.put(3)

print(que.get())


#heapq 이용해서 구현 가능
import heapq

hq = []

#heapq.heqppush(heqp, item) : 원소 추가
heapq.heappush(hq,4)

#heapq.heappop(heap) : 원소 삭제
heapq.heappop(hq)

#heapify(x) : 리스트 x를 선형시간으로 제자리에서 heap으로 변환
