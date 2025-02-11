from main import SLList
from cprint import cprint


def test_AddFirst():
    L = SLList()
    L.AddFirst(10)
    assert L.GetFirst() == 10, "Test AddFirst Failed"
    assert L.Size() == 1, "Test AddFirst Failed"
    
    L.AddFirst(20)
    assert L.GetFirst() == 20, "Test AddFirst Failed"
    assert L.Size() == 2, "Test AddFirst Failed"
    cprint("test_AddFirst passed", "green")

def test_AddLast():
    L = SLList()
    L.AddLast(10)
    assert L.GetFirst() == 10, "Test AddLast Failed"
    assert L.Size() == 1, "Test AddLast Failed"
    
    L.AddLast(20)
    assert L.sentinel.next.next.item == 20, "Test AddLast Failed"
    assert L.Size() == 2, "Test AddLast Failed"
    cprint("test_AddLast passed", "green")

def test_GetFirst():
    L = SLList()
    assert L.GetFirst() is None, "Test GetFirst Failed"
    
    L.AddFirst(10)
    assert L.GetFirst() == 10, "Test GetFirst Failed"
    
    L.AddLast(20)
    assert L.GetFirst() == 10, "Test GetFirst Failed"
    cprint("test_GetFirst passed", "green")

def test_Size():
    L = SLList()
    assert L.Size() == 0, "Test Size Failed"
    
    L.AddFirst(10)
    assert L.Size() == 1, "Test Size Failed"
    
    L.AddLast(20)
    assert L.Size() == 2, "Test Size Failed"
    
    L.AddLast(30)
    assert L.Size() == 3, "Test Size Failed"
    cprint("test_Size passed", "green")

if __name__ == '__main__':
    test_AddFirst()
    test_AddLast()
    test_GetFirst()
    test_Size()
    cprint("All tests passed", "green")