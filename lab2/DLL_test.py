from DLL import DLList
from cprint import *
import tracemalloc
import gc

def test_create_empty_list():
    L = DLList()
    assert L.isEmpty(), "Test Failed: List should be empty"
    assert L.size() == 0, "Test Failed: Size should be 0"
    assert L.toList() == [], "Test Failed: List should be empty"
    cPass("Test create empty list passed")

def test_add_operations():
    L = DLList()
    
    L.addLast(5)
    L.addLast(10)
    L.addFirst(3)
    L.addFirst(1)

    assert L.toList() == [1, 3, 5, 10], "Test Failed: addFirst/addLast incorrect"
    assert L.size() == 4, "Test Failed: Size should be 4"
    cPass("Test add operations passed")

def test_remove_operations():
    L = DLList()
    L.addLast(5)
    L.addLast(10)
    L.addFirst(3)
    L.addFirst(1)

    assert L.removeFirst() == 1, "Test Failed: removeFirst incorrect"
    assert L.removeLast() == 10, "Test Failed: removeLast incorrect"
    assert L.toList() == [3, 5], "Test Failed: Incorrect list after removals"
    assert L.size() == 2, "Test Failed: Size should be 2"
    
    L.removeFirst()
    L.removeLast()
    
    assert L.isEmpty(), "Test Failed: List should be empty after removing all elements"
    cPass("Test remove operations passed")

def test_get():
    L = DLList()
    L.addLast(5)
    L.addLast(10)
    L.addLast(15)

    assert L.get(0) == 5, "Test Failed: get(0) should be 5"
    assert L.get(1) == 10, "Test Failed: get(1) should be 10"
    assert L.get(2) == 15, "Test Failed: get(2) should be 15"
    assert L.get(-1) is None, "Test Failed: get(-1) should return None"
    assert L.get(3) is None, "Test Failed: get(3) should return None"
    
    cPass("Test get function passed")

def test_remove_empty():
    L = DLList()
    
    assert L.removeFirst() is None, "Test Failed: removeFirst() on empty list should return None"
    assert L.removeLast() is None, "Test Failed: removeLast() on empty list should return None"

    L.addLast(10)
    L.removeFirst()

    assert L.isEmpty(), "Test Failed: List should be empty after removing only element"
    
    cPass("Test remove from empty list passed")

def test_size():
    L = DLList()
    assert L.size() == 0, "Test Failed: Initial size should be 0"
    
    L.addFirst(5)
    assert L.size() == 1, "Test Failed: Size should be 1"
    
    L.addLast(10)
    assert L.size() == 2, "Test Failed: Size should be 2"

    L.removeFirst()
    assert L.size() == 1, "Test Failed: Size should be 1 after removing one element"

    L.removeLast()
    assert L.size() == 0, "Test Failed: Size should be 0 after removing all elements"
    
    cPass("Test size function passed")

def test_isEmpty():
    L = DLList()
    assert L.isEmpty(), "Test Failed: isEmpty() should return True for new list"
    
    L.addFirst(5)
    assert not L.isEmpty(), "Test Failed: isEmpty() should return False after adding an element"

    L.removeFirst()
    assert L.isEmpty(), "Test Failed: isEmpty() should return True after removing all elements"
    
    cPass("Test isEmpty function passed")

def test_memory_usage(info=False):
    L = DLList()

    # Start tracking memory
    tracemalloc.start()

    # Add 10,000 items
    for i in range(10000):
        L.addLast(i)

    assert L.size() == 10000, "Test Failed: Size should be 10000"

    # Check memory usage before deletion
    before_mem = tracemalloc.get_traced_memory()[0]
    if info:
        cInfo(f"Memory used before deleting: {before_mem} bytes")

    # Remove 9,999 items
    for i in range(9999):
        L.removeFirst()

    assert L.size() == 1, "Test Failed: Size should be 1 after removing 9999 items"

    # Force garbage collection
    gc.collect()

    # Check memory usage after deletion
    after_mem = tracemalloc.get_traced_memory()[0]
    if info:
        cInfo(f"Memory used after deleting: {after_mem} bytes")

    # Stop tracing memory
    tracemalloc.stop()

    assert after_mem < before_mem, "Test Failed: Memory should decrease after removal"
    cPass("Test memory usage passed")

if __name__ == "__main__":
    print("\nRunning DLList Tests...\n")
    test_create_empty_list()
    test_add_operations()
    test_remove_operations()
    test_get()
    test_remove_empty()
    test_size()
    test_isEmpty()
    test_memory_usage(info=True)
    print("\nAll tests passed successfully!\n")
