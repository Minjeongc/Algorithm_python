class Node : 
    
    def __init__ (self, key ,data ) :
        self.key = key 
        self.data = data
        self.left = None
        self.right = None

    def lookup (self, key , parent = None) : 
        if key < self.key : 
            if self.left : return self.left.lookup(key, self)
            else: return None, None
        
        elif key > self.key :
            if self.right : return self.right.lookup (key, self)
            else: return None, None
        else: return self, parent 

    def countChildern (self):
        count = 0
        if self.left : count += 1
        if self.right : count += 1
        return count

class BinSearchTree:
    def __init__(self):
        self.root = None
    
    def lookup (self, key):
        if self.root : return self.root.lookup(key)
        else: return None, None
    
    def remove (self, key):
        node, parent = self.lookup(key)
        if node:
            nChildern = node.count.Children()
            if nChildern == 0 : #자식노드가 없는 경우
                #만약 부모가 존재한다면, node가 왼쪽자식인지 오른쪽 자식인지 판단하여
                #parent.left or parent.right 를 None으로 하여 
                #leaf node였던 자식을 트리에서 끊어내어 없앰.
                if parent:
                    if parent.left == node : 
                        parent.left = None
                    else: parent.right = None
                else:
                    self.root = None
            elif nChildern == 1:
                if parent :
                    if node.left:
                        if parent.left == node:
                            parent.left = node.left
                        else:
                            parent.right = node.left
                    else: 
                        if parent.right == node :
                            parent.right = node.right
                        else: 
                            parent.left - node.right

                else: 
                    if node.left: self.root = node.left
                    else: self.root = node.right 
            
            else:
                parent = node
                successor = node.right 
                while successor.left:
                    parent = successor
                    successor = successor.left
                
                node.key = successor.key
                node.data = successor.data

                if parent == successor:
                    if successor.left : 
                        parent.left = successor.left
                    elif successor.right:
                        parent.left = successor.right 
                    else: 
                        parent.left = None
                else:
                    if successor.left: 
                        parent.right = successor.left
                    elif successor.right :
                        parent.right = successor.right 
                    else:
                        parent.right = None
        else:
            return False 



                


    