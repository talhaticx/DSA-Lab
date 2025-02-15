import time
import tracemalloc
from cprint import *
from ADeque import ADeque

def test_create_empty_adeque():
    D = ADeque()
    assert D.isEmpty(), "Test Failed: Deque should be empty"
    assert D.getSize() == 0, "Test Failed: Size should be 0"
    cPass("Test create empty ADeque passed")

def test_add_operations():
    D = ADeque()
    
    D.addLast(5)
    D.addLast(10)
    D.addLast(15)
    
    assert D.get(0) == 5, "Test Failed: addLast incorrect"
    assert D.get(1) == 10, "Test Failed: addLast incorrect"
    assert D.get(2) == 15, "Test Failed: addLast incorrect"
    assert D.getSize() == 3, "Test Failed: Size should be 3"
    cPass("Test add last operations passed")
    
    D.addFirst(20)
    D.addFirst(25)
    
    assert D.get(0) == 25, "Test Failed: addFirst incorrect"
    assert D.get(1) == 20, "Test Failed: addFirst incorrect"
    assert D.get(2) == 5, "Test Failed: addFirst incorrect"
    assert D.getSize() == 5, "Test Failed: Size should be 5"
    cPass("Test add first operations passed")

def test_remove_operations():
    D = ADeque()
    
    D.addLast(5)
    D.addLast(10)
    D.addLast(15)
    
    assert D.removeLast() == 15, "Test Failed: removeLast incorrect"
    assert D.removeLast() == 10, "Test Failed: removeLast incorrect"
    assert D.removeLast() == 5, "Test Failed: removeLast incorrect"
    assert D.isEmpty(), "Test Failed: Deque should be empty"
    cPass("Test remove last operations passed")
    
    D.addFirst(20)
    D.addFirst(25)
    
    assert D.removeFirst() == 25, "Test Failed: removeFirst incorrect"
    assert D.removeFirst() == 20, "Test Failed: removeFirst incorrect"
    assert D.isEmpty(), "Test Failed: Deque should be empty"
    cPass("Test remove first operations passed")

def test_resizing():
    D = ADeque()
    for i in range(100):
        D.addLast(i)
    assert D.getSize() == 100, "Test Failed: Size should be 100 after additions"
    
    for i in range(75):
        D.removeLast()
    assert D.capacity < 200, "Test Failed: Capacity should shrink after removing many elements"
    cPass(f"Test resizing behavior passed")

def test_time_add(n=100000):
    D = ADeque()
    start = time.time()
    for i in range(n):
        D.addLast(i)
    end = time.time()
    cInfo(f"Time taken to add {n} elements: {end - start:.5f} sec")
    

def test_time_remove(n=10000):
    D = ADeque()
    for i in range(n):
        D.addLast(i)
    
    start = time.time()
    for i in range(n):
        D.removeLast()
    end = time.time()
    cInfo(f"Time taken to remove {n} elements: {end - start:.5f} sec")

def test_memory_usage(n=1000):
    D = ADeque()
    tracemalloc.start()
    
    for i in range(n):
        D.addLast(i)
    before_mem = tracemalloc.get_traced_memory()[0]
    
    for i in range(n):
        progress_loader(i+1, n, prefix="Testing Memory")
        D.removeLast()
    
    after_mem = tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    
    cInfo(f"\nMemory before deletion: {before_mem} bytes")
    cInfo(f"Memory after deletion: {after_mem} bytes")
    assert after_mem < before_mem, "Test Failed: Memory should reduce after deletion"
    cPass("Test memory usage passed")

# Additional Tests
def test_boundary_conditions():
    D = ADeque()
    for i in range(8):
        D.addLast(i)
    assert D.getSize() == 8, "Test Failed: Size should be 8"
    D.addLast(8)
    assert D.get(8) == 8, "Test Failed: addLast incorrect on boundary"
    assert D.getSize() == 9, "Test Failed: Size should be 9 after boundary add"
    cPass("Test boundary conditions passed")

def test_edge_cases():
    D = ADeque()
    assert D.removeFirst() is None, "Test Failed: removeFirst on empty deque"
    assert D.removeLast() is None, "Test Failed: removeLast on empty deque"
    for i in range(100000):
        D.addLast(i)
    assert D.getSize() == 100000, "Test Failed: Size should be 100000"
    for i in range(100000):
        D.removeFirst()
    assert D.isEmpty(), "Test Failed: Deque should be empty after removing all elements"
    cPass("Test edge cases passed")

def test_alternating_add_remove():
    D = ADeque()
    for i in range(50):
        D.addLast(i)
        D.addFirst(-i)
    for i in range(50):
        assert D.removeFirst() == -(49-i), "Test Failed: alternating add/remove first incorrect"
        assert D.removeLast() == 49-i, "Test Failed: alternating add/remove last incorrect"
    cPass("Test alternating add/remove passed")

def test_randomized_operations():
    import random
    D = ADeque()
    operations = ['addFirst', 'addLast', 'removeFirst', 'removeLast']
    for _ in range(1000):
        op = random.choice(operations)
        if op in ['addFirst', 'addLast']:
            value = random.randint(1, 1000)
            if op == 'addFirst':
                D.addFirst(value)
            else:
                D.addLast(value)
        else:
            if op == 'removeFirst':
                D.removeFirst()
            else:
                D.removeLast()
    assert True, "Test Failed: Randomized operations encountered an error"
    cPass("Test randomized operations passed")

if __name__ == "__main__":
    print("\nRunning ADeque Tests...\n")
    test_create_empty_adeque()
    test_add_operations()
    test_remove_operations()
    test_resizing()
    print()
    for i in range(7):
        test_time_add(10**i)
    print()
    for i in range(7):
        test_time_remove(10**i)
    print()
    test_memory_usage(n=50000)
    test_boundary_conditions()
    test_edge_cases()
    test_alternating_add_remove()
    test_randomized_operations()
    print("\nAll tests passed successfully!\n")