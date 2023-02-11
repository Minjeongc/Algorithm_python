class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack():
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("스택이 비워져있습니다")
        else:
            pop_object = self.head.data
            self.head = self.head.next
        return pop_object
    
    def top(self):
        top_object = None
        if self.isEmpty():
            print("스택이 비워져있습니다")
        else:
            top_object = self.head.data
        return top_object
    
    def isEmpty(self):
        is_Empty = False
        if self.head is None:
            is_Empty = True
        return is_Empty