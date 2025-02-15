import time
import tracemalloc
from cprint import *
from AList import AList  

def test_create_empty_alist():
    L = AList()
    assert L.isEmpty(), "Test Failed: List should be empty"
    assert L.size == 0, "Test Failed: Size should be 0"
    cPass("Test create empty AList passed")

def test_add_operations():
    L = AList()
    
    L.addLast(5)
    L.addLast(10)
    L.addLast(15)
    
    assert L.Get(0) == 5, "Test Failed: addLast incorrect"
    assert L.Get(1) == 10, "Test Failed: addLast incorrect"
    assert L.Get(2) == 15, "Test Failed: addLast incorrect"
    assert L.size == 3, "Test Failed: Size should be 3"
    cPass("Test add operations passed")

def test_remove_operations():
    L = AList()
    L.addLast(5)
    L.addLast(10)
    L.addLast(15)
    
    assert L.removeLast() == 15, "Test Failed: removeLast incorrect"
    assert L.removeLast() == 10, "Test Failed: removeLast incorrect"
    assert L.removeLast() == 5, "Test Failed: removeLast incorrect"
    assert L.isEmpty(), "Test Failed: List should be empty"
    cPass("Test remove operations passed")

def test_resizing():
    L = AList()
    for i in range(100):
        L.addLast(i)
    assert L.size == 100, "Test Failed: Size should be 100 after additions"
    
    for i in range(75):
        L.removeLast()
    assert L.capacity < 200, "Test Failed: Capacity should shrink after removing many elements"
    cPass(f"Test resizing behavior passed")

def test_time_add(n=100000):
    L = AList()
    start = time.time()
    for i in range(n):
        L.addLast(i)
    end = time.time()
    cInfo(f"Time taken to add {n} elements: {end - start:.5f} sec")
    

def test_time_remove(n=10000):
    L = AList()
    for i in range(n):
        L.addLast(i)
    
    start = time.time()
    for i in range(n):
        L.removeLast()
    end = time.time()
    cInfo(f"Time taken to remove {n} elements: {end - start:.5f} sec")

def test_memory_usage(n=1000):
    L = AList()
    tracemalloc.start()
    
    for i in range(n):
        L.addLast(i)
    before_mem = tracemalloc.get_traced_memory()[0]
    
    for i in range(n):
        progress_loader(i+1, n, prefix="Testing")
        L.removeLast()
    
    after_mem = tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    
    cInfo(f"\nMemory before deletion: {before_mem} bytes")
    cInfo(f"Memory after deletion: {after_mem} bytes")
    assert after_mem < before_mem, "Test Failed: Memory should reduce after deletion"
    cPass("Test memory usage passed")

if __name__ == "__main__":
    print("\nRunning AList Tests...\n")
    test_create_empty_alist()
    test_add_operations()
    test_remove_operations()
    test_resizing()
    print()
    for i in range(7):
        test_time_add(10**i)
    print()
    for i in range(4):
        test_time_remove(10**i)
    print()
    test_memory_usage(n=2000)
    print("\nAll tests passed successfully!\n")
