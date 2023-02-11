class Node:
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.no = 0
        self.head = None
        self.current = None #이터레이터에서 사용될 변수
    
    def __len__(self):
        return self.no

    def search(self, data):
        count = 0
        pointer = self.head

        while pointer is not None:
            if pointer.data == data:
                return count
            count += 1
            pointer = pointer.next

        return -1

    def __contains__(self, data):
        return self.search(data) >= 0

    def add_first(self, data):
        pointer = self.head
        self.head = Node(data, pointer)
        self.no += 1
    
    def add_last(self, data):
        pointer = self.head
        if pointer is None:
            self.add_first(data)
        else:
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = Node(data, None)
            self.no += 1
        
    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next
            self.no -= 1
        
    def remove_last(self):
        if self.head.next is not None:
            self.remove_first()
        else:
            cur_pointer = self.head
            pre_pointer = self.head
            while cur_pointer.next is not None:
                pre_pointer = cur_pointer
                cur_pointer - cur_pointer.next

            pre_pointer.next = None
            self.no -= 1

    def remove(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.remove_first()
                return True
            
            pointer = self.head
            while pointer.next is not None:
                if pointer.next.data == data:
                    pointer.next = pointer.next.next
                    return True
                pointer = pointer.next
        return False 

    def __iter__(self):
        self.current = self.head
        return self 
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
