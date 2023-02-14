class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
    
    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0

        return l + r + 1
    
    def depth(self):
        leftDepth = self.left.depth() if self.left else 0
        rightDepth = self.right.depth() if self.right else 0
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth+1

    def inorder(self): #중위순회
        traversal = []
        if self.left : traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right : traversal += self.right.inorder()
        return traversal
    
    def preorder(self): #전위순회
        traverse = []
        traverse.append(self.data)
        if self.left: traverse += self.left.preorder()
        if self.right : traverse += self.right.preorder()
        return traverse

    def postorder (self) :
        traverse = []
        if self.left : traverse += self.left.postorder()
        if self.right : traverse += self.right.postorder()
        traverse.append(self.data)
        return traverse

class BinaryTree:

    def __init__ (self, r):
        self.root = r
    
    def size (self):
        if self.root: return self.root.size()
    
    def depth(self) :
        if self.root : return self.root.depth()
        else: return 0

    def inorder(self):
        if self.root: return self.root.inorder()
        else: return []
    
    def preorder(self):
        if self.root: return self.root.preorder()
        else: return []

    def postorder(self):
        if self.root: return self.root.postorder()
        else: return []

    def insert(self, key, data) : 
        if key < self.key : 
            if self.left : self.left.insert(key, data)
            else: self.left = Node(key, data) 
        elif key > self.key :
            if self.right : self.right.insert(key, data)
            else: self.right = Node(key, data) 
        else: raise KeyError ("이미 존재합니다")
