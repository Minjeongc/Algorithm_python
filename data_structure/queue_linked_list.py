class Node:
    def __init__(self,data) : 
        self.data = data
        self.next = None

class Queue():
    def __init__(self) : 
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        
        else:
            self.rear = self.rear.next
            self.rear.next = new_node

    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is empty")
        else:
            dequeue_object = self.front.data 
            self.front = self.front.next
        return dequeue_object

    def peek(self):
        front_object = None
        if self.isEmpty():
            print("Queue is empty")
        else:
            front_object = self.front.data
        return front_object
    
    def isEmpty(self):
        is_empty = False
        if self.front is None:
            is_empty = True
        return is_empty