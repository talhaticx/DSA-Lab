class Node:
    def __init__(self, value, next=None):
        self.item = value
        self.next = next

class SLList:
    def __init__(self):
        self.sentinel = Node(63)
        self.size = 0
    
    def AddFirst(self, value):
        if self.size == 0:
            self.sentinel.next = Node(value)
            self.size+=1
        else:
            self.sentinel.next = Node(value, self.sentinel.next)
            self.size+=1
    
    def AddLast(self, value):
        if self.size == 0:
            self.sentinel.next = Node(value)
            self.size+=1
        else:
            current = self.sentinel.next
            while current.next:
                current = current.next
            current.next = Node(value)
            self.size+=1
    
    def GetFirst(self):
        if self.size == 0:
            return None
        else:
            return self.sentinel.next.item
        
    def Size(self):
        return self.size
    

L = SLList()
L.AddFirst(5)
L.AddFirst(10)
L.AddLast(15)

print(L.sentinel.next.item)
assert(L.sentinel.next.item == 10)