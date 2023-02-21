# 각 원소들이 우선순위를 가지고 있어 높은 우선순위를 가진 원소가 먼저 처리됨. 
# 만약 같은 우선순위라면, 먼저 들어온 원소를 처리.
# push : 원소의 우선순위를 지정하여 추가하는 함수
# pop: 가장 높은 우선순위를 가진 원소를 큐에서 제거하고 반환하는 함수
# 리스트를 이용한 방법보다 힙 자료구조를 이용해 구현 -> 시간복잡도 면에서 효율적임. 


# 양방향 리스트 이용한 구현
# enqueue 할때 우선순위를 유지하도록

#양방향 연결리스트
class Node:
    def __init__(self, item):
        self.data = item 
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.head.prev = self.head
        self.tail.next = None
    
    def traverse(self):
        result = []
        curr = self.head 
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result
    
    def reverse(self):
        result = []
        curr = self.head
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result
    
    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True
    
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        
        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos :
                curr = curr.next
                i += 1
    def popAfter(self, prev):
        curr = prev.next
        prev.next = curr.next
        curr.next.prev = prev
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos - 1)

        return self.popAfter(prev)




class PriorityQueue:
    def __init__(self, x):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.queue.getLength() 
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue (self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr.next != self.queue.tail and x < curr.next.data:
            curr = curr.next
        
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())
    

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data
