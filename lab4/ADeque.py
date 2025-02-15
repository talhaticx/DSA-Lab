import array as arr 

class ADeque:
    def __init__(self):
        self.capacity = 8
        self.items = arr.array('i', [0]*self.capacity)
        self.nextFirst = 0
        self.nextLast = 1
        self.size = 0
        
    def resize(self):
        capacity = self.capacity
        if self.size == self.capacity:
            capacity = self.capacity * 2
        elif self.size < self.capacity // 4 and self.capacity > 8:
            capacity = self.capacity // 2
        
        newDeque = arr.array('i', [0] * capacity)
        
        # Copy elements in order from front to back
        old_index = (self.nextFirst + 1) % self.capacity
        for i in range(self.size):
            newDeque[i] = self.items[old_index]
            old_index = (old_index + 1) % self.capacity
        
        # Update attributes
        self.items = newDeque
        self.capacity = capacity
        self.nextFirst = capacity - 1  # Points to the last empty slot
        self.nextLast = self.size     # Points to the next available slot
    
    def addFirst(self, item):
        if self.size == self.capacity:
            self.resize()

        self.items[self.nextFirst] = item
        self.nextFirst = (self.nextFirst - 1) % self.capacity
        
        self.size += 1
    
    def addLast(self, item):
        if self.size == self.capacity:
            self.resize()

        self.items[self.nextLast] = item
        self.nextLast = (self.nextLast + 1) % self.capacity
        
        self.size += 1
        
    def get(self, index):
        if index >= self.size:
            return None
        
        index = (self.nextFirst + 1 + index) % self.capacity
        return self.items[index]
    
    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    
    def removeFirst(self):
        if self.isEmpty():
            return None
        
        self.nextFirst = (self.nextFirst + 1) % self.capacity
        item = self.items[self.nextFirst]
        self.items[self.nextFirst] = 0
        self.size -= 1
        
        if self.size < self.capacity // 4:
            self.resize()
        
        return item

    def removeLast(self):
        if self.isEmpty():
            return None
        
        self.nextLast = (self.nextLast - 1) % self.capacity
        item = self.items[self.nextLast]
        self.items[self.nextLast] = 0
        self.size -= 1
        
        if self.size < self.capacity // 4:
            self.resize()
        
        return item

    def toList(self):
        result = []
        index = (self.nextFirst + 1) % self.capacity
        for i in range(self.size):
            result.append(self.items[index])
            index = (index + 1) % self.capacity
        return result

# a = ADeque()
# a.addFirst(25)
# a.addLast(30)
# a.addFirst(20)
# a.addLast(35)
# a.addFirst(15)
# a.addLast(40)
# a.addFirst(10)
# a.addFirst(5)
# a.addFirst(9)

# print(a.toList())