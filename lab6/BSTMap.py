# Represents a single node (vertex) in the Binary Search Tree
class Vertex:
    def __init__(self, k=0, l=None, r=None, v=None):
        self.key = k           # Key for sorting
        self.left = l          # Left child (smaller keys)
        self.right = r         # Right child (larger keys)
        self.value = v         # Associated value


# Binary Search Tree based Map implementation
class BSTMap:
    def __init__(self):
        self.root = None  # Start with an empty tree

    # Public insert method (takes a tuple of key, value)
    def insert(self, params):
        k, v = params
        self.root = self._insertRecursive(self.root, k, v)

    # Helper recursive insert method
    def _insertRecursive(self, ver: Vertex, k, v):
        if ver is None:
            # Found correct spot, insert new node
            return Vertex(k=k, v=v)
        if k < ver.key:
            # Go left for smaller key
            ver.left = self._insertRecursive(ver.left, k, v)
        elif k > ver.key:
            # Go right for larger key
            ver.right = self._insertRecursive(ver.right, k, v)
        else:
            # Key already exists, update value
            ver.value = v
        return ver

    # Public method to check if a key exists in the BST
    def find(self, k):
        return self._findRecursive(self.root, k)

    # Recursive search method
    def _findRecursive(self, ver: Vertex, k):
        if ver is None:
            return False  # Reached leaf, key not found
        if k == ver.key:
            return True   # Key found
        elif k < ver.key:
            return self._findRecursive(ver.left, k)  # Go left
        else:
            return self._findRecursive(ver.right, k) # Go right

# Test block
if __name__ == "__main__":
    t = BSTMap()
    
    # Sample data as (key, value) pairs
    DATA = [(4, 'uet'), (2, 'uet'), (1, 'uet'), (3, 'uet'), (7, 'uet'), (5, 'uet'), (8, 'uet')]

    # Insert all data into BSTMap
    for d in DATA:
        t.insert(d)

    # Check if keys exist
    print(t.find(5))    # True
    print(t.find(9))    # False
