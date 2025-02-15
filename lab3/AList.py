import array as arr

class AList:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.items = arr.array('i', [0] * self.capacity)
        
    def resize(self):
        if self.size == self.capacity:  # Expand when full
            self.capacity *= 2
        elif self.size < self.capacity // 4 and self.capacity > 5:  # Shrink when size < 25% of capacity
            self.capacity //= 2
        
        new_items = arr.array('i', [0] * self.capacity)
        for i in range(self.size):
            new_items[i] = self.items[i]
        self.items = new_items

    def addLast(self, item):
        if self.size == self.capacity:
            self.resize()
        self.items[self.size] = item
        self.size += 1
    
    def getLast(self):
        return None if self.size == 0 else self.items[self.size - 1]
    
    def removeLast(self):
        if self.size == 0:
            return None
        ret = self.items[self.size - 1]
        self.items[self.size - 1] = 0
        self.size -= 1
        self.resize()  # Resize after removal to avoid wasted space
        return ret
    
    def Get(self, idx):
        return None if idx < 0 or idx >= self.size else self.items[idx]
    
    def isEmpty(self):
        return self.size == 0
    
    def getSize(self): 
        return self.size

    def __str__(self):  # For easy debugging
        return str(self.items[:self.size])

if __name__ == "__main__":
    a = AList()
    a.addLast(1)
    a.addLast(2)
    a.addLast(3)
    print(a)  # Output: array('i', [1, 2, 3])
