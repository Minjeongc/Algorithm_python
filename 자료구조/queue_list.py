class Queue():
    def __init__(self):
        self.queue = []

    def enqueue (self, data):
        self.queue.append(data)

    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is empty")
        else:
            dequeue_object = self.queue[0]
            self.queue = self.queue[1:]
        return dequeue_object
    
    def peek(self):
        peek_object = None
        if self.isEmpty():
            print("Queue is empty")
        else:
            peek_object = self.queue[0]
        return peek_object
    
    def isEmpty(self):
        is_Empty = False
        if len(self.queue) == 0:
            is_Empty = True
        return is_Empty

        

