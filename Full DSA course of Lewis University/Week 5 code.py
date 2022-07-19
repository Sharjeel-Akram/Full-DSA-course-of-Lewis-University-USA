import queue

class BinaryTree:
    class _Node:
        def __init__(self, element, left = None, right = None):
            self._left = left
            self._right = right
            self._element = element

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._root

    def add_root(self, e):
        if self._root:
            raise Exception()

        node = self._Node(e)
        self._root = node
        return node

    def add_left(self, e, p):
        node = self._Node(element=e)
        p._left = node
        return node


    def add_right(self, e, p):
        node = self._Node(element=e)
        p._right = node
        return node

    def in_order(self):
        self._in_order(self._root)


    def _in_order(self, p):
        if p is not None:
            self._in_order(p._left)
            print(p._element, end = " ")
            self._in_order(p._right)


    def pre_order(self):
        self._pre_order(self._root)

    def _pre_order(self, p):
        if p is not None:
            print(p._element, end = " ")
            self._pre_order(p._left)
            self._pre_order(p._right)


    def post_order(self):
        self._post_order(self._root)

    def _post_order(self, p):
        if p is not None:
            self._post_order(p._left)
            self._post_order(p._right)
            print(p._element)

    def breadth_first(self):
        q = queue.Queue()
        q.put(self._root)

        while not q.empty():
            p = q.get()
            if p._left:
                q.put(p._left)
            if p._right:
                q.put(p._right)

            yield p._element


    def height(self):
        return self._height(self._root)

    def _height(self, p):
        if p is None:
            return 0

        height_left = self._height(p._left)
        height_right = self._height(p._right)

        return 1 + max(height_left, height_right)

    def copy(self):
        tree = BinaryTree()
        tree._root = self.copying(self._root)
        return tree
    
    def copying(self, root) :
        if (root != None):
            Root = self._Node(root._element)
            Root._left = self.copying(root._left)
            Root._right = self.copying(root._right)
            return Root._element
        return None
    
    def equal(self, a, b):
        if a is None and b is None:
            return True
        if a is not None and b is not None:
            return ((a._element == b._element) and self.equal(a._left, b._left)and self.equal(a._right, b._right))
        return False

btree = BinaryTree()
root = btree.add_root(4)
node = btree.add_left(2, root)
btree.add_left(1, node)
btree.add_right(3, node)

node = btree.add_right(6, root)

btree.add_left(5, node)
btree.add_right(7, node)

btree._pre_order(root)

print('\nheight of b_tree: {}'.format(btree.height()))
tree2 = btree.copy()
tree2._pre_order(root)

if btree.equal(root, tree2):
    print("\nBoth trees are not same")
else:
    print ("\nBoth Trees are same")
