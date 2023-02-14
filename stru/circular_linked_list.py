class Node:
    def __init__ (self):
        self.data = None
        self.next = None
    

class CircularLinkedList:
    def __init__(self):
        self.head = Node('head')
        self.head.next = self.head
    
    def insert(self, data, new):
        new_node = Node(new)
        current_node = self.find(data)
        new_node.next = current_node.next
        current_node.next = new_node
    
    def find(self, data):
        current_node = self.head
        while current_node.data != data:
            current_node = current_node.next
        return current_node
    
    def find_previous(self, data):
        current_node= self.head
        while current_node.next.data  != data:
            current_node = current_node.next
        return current_node
    
    def remove(self, data):
        previous_node= self.find_previous(data)
        previous_node.next = previous_node.next.next
        
