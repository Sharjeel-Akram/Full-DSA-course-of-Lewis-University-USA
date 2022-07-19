import queue

class BinaryTree:
    class _Node:
        def __init__(self, element, left = None, right = None):
            self._left = left
            self._right = right
            self._element = element

    def __init__(self):
        self._head = None
        self._size = 0

    def Insert(self, key):
        if self._head == None:
            newNode = self._Node(key)
            self._head = newNode
        else:
            node = self._head
            while node is not None:
                n = node
                if key < node._element:
                    node = node._left
                else:
                    node = node._right
            newNode = self._Node(key)
            if key < n._element:
                n._left = newNode
            else:
                n._right = newNode

    def in_order(self):
        self._in_order(self._head)

    def _in_order(self, p):
        if p is not None:
            self._in_order(p._left)
            print(p._element, end = " ")
            self._in_order(p._right)

    def search(self,key):
        if self._head:
            Found = self.search_key(key,self._head)
            if Found:
                print("The element is present in the Binary Search Tree")
            else:
                print("The element is not present in the Binary Search Tree")
            
    def search_key(self,key,current_Node):
        if key > current_Node._element and current_Node._right:
            return self.search_key(key,current_Node._right)      
        elif key < current_Node._element and current_Node._left:
            return self.search_key(key,current_Node._left)
        if key == current_Node._element:
            return True
        
    def delete(self,key):
        if self._head:
            return self.deleteNode(self._head,key)

    def minValueNode( node): 
        current = node
        while(current.left is not None): 
            current = current.left
        return current  

    def deleteNode(self,root, key):
        if root is None: 
            return root
        if key < root._element: 
            root._left = self.deleteNode(root._left, key) 
        elif(key > root._element): 
            root._right = self.deleteNode(root._right, key)
        else: 
            if root._left is None : 
                temp = root._right  
                root = None 
                return temp  
            elif root._right is None : 
                temp = root._left  
                root = None
                return temp  
            temp = self.minValueNode(root._right)
            root._element = temp._element 
            root._right = self.deleteNode(root._right , temp._element) 
        return root

btree = BinaryTree()
btree.Insert(2)
btree.Insert(3)
btree.Insert(4)
btree.Insert(5)
btree.Insert(6)
btree.Insert(7)

btree.in_order()
print()
btree.search(7)
btree.delete(2)




