import time
from lab1.SLL import SLList
from cprint import cPass, cFail, cInfo

def test_AddFirst():
    L = SLList()
    try:
        L.AddFirst(10)
        assert L.GetFirst() == 10, "Test AddFirst Failed"
        assert L.Size() == 1, "Test AddFirst Failed"
        
        L.AddFirst(20)
        assert L.GetFirst() == 20, "Test AddFirst Failed"
        assert L.Size() == 2, "Test AddFirst Failed"
        cPass("test_AddFirst passed")
    except AssertionError as e:
        cFail(str(e))

def test_AddLast():
    L = SLList()
    try:
        L.AddLast(10)
        assert L.GetFirst() == 10, "Test AddLast Failed"
        assert L.Size() == 1, "Test AddLast Failed"
        
        L.AddLast(20)
        assert L.sentinel.next.next.item == 20, "Test AddLast Failed"
        assert L.Size() == 2, "Test AddLast Failed"
        cPass("test_AddLast passed")
    except AssertionError as e:
        cFail(str(e))

def test_GetFirst():
    L = SLList()
    try:
        assert L.GetFirst() is None, "Test GetFirst Failed"
        
        L.AddFirst(10)
        assert L.GetFirst() == 10, "Test GetFirst Failed"
        
        L.AddLast(20)
        assert L.GetFirst() == 10, "Test GetFirst Failed"
        cPass("test_GetFirst passed")
    except AssertionError as e:
        cFail(str(e))

def test_Size():
    L = SLList()
    try:
        assert L.Size() == 0, "Test Size Failed"
        
        L.AddFirst(10)
        assert L.Size() == 1, "Test Size Failed"
        
        L.AddLast(20)
        assert L.Size() == 2, "Test Size Failed"
        
        L.AddLast(30)
        assert L.Size() == 3, "Test Size Failed"
        cPass("test_Size passed")
    except AssertionError as e:
        cFail(str(e))


if __name__ == '__main__':
    cInfo("Starting tests...")
    test_AddFirst()
    test_AddLast()
    test_GetFirst()
    test_Size()
    cInfo("All tests completed")
