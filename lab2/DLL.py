class Node:
    """A node in the doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLList:
    """A circular doubly linked list with a sentinel node."""
    def __init__(self):
        self.sentinel = Node(None)  # Sentinel node (dummy)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self._size = 0

    def addFirst(self, data):
        """Adds a node with the given data to the front of the list."""
        new_node = Node(data)
        new_node.next = self.sentinel.next
        new_node.prev = self.sentinel
        self.sentinel.next.prev = new_node
        self.sentinel.next = new_node
        self._size += 1

    def addLast(self, data):
        """Adds a node with the given data to the end of the list."""
        new_node = Node(data)
        new_node.prev = self.sentinel.prev
        new_node.next = self.sentinel
        self.sentinel.prev.next = new_node
        self.sentinel.prev = new_node
        self._size += 1

    def toList(self):
        """Returns a list representation of the linked list."""
        lst = []
        current = self.sentinel.next
        while current != self.sentinel:
            lst.append(current.data)
            current = current.next
        return lst

    def size(self):
        """Returns the number of elements in the list."""
        return self._size

    def isEmpty(self):
        """Checks if the list is empty."""
        return self._size == 0

    def get(self, index):
        """Returns the data at the given index or None if out of bounds."""
        if index < 0 or index >= self._size:
            return None
        
        # Optimize traversal by starting from head or tail
        if index < self._size // 2:
            current = self.sentinel.next
            for _ in range(index):
                current = current.next
        else:
            current = self.sentinel.prev
            for _ in range(self._size - index - 1):
                current = current.prev

        return current.data

    def removeFirst(self):
        """Removes and returns the first element. Returns None if empty."""
        if self._size == 0:
            return None
        first_node = self.sentinel.next
        self.sentinel.next = first_node.next
        first_node.next.prev = self.sentinel
        self._size -= 1
        
        first_node.next = None
        first_node.prev = None
        
        return first_node.data

    def removeLast(self):
        """Removes and returns the last element. Returns None if empty."""
        if self._size == 0:
            return None
        last_node = self.sentinel.prev
        self.sentinel.prev = last_node.prev
        last_node.prev.next = self.sentinel
        self._size -= 1
        
        last_node.next = None
        last_node.prev = None
        
        return last_node.data
