import time
import tracemalloc
import random

from cprint import *
from BSTMap import BSTMap
from DisplayBST import display

def test_insert_and_find():
    bst = BSTMap()
    data = [(4, 'uet'), (2, 'uet'), (1, 'uet'), (3, 'uet'), (7, 'uet'), (5, 'uet'), (8, 'uet')]
    
    for d in data:
        bst.insert(d)
    
    display(bst.root)
    
    for key, _ in data:
        assert bst.find(key), f"Test Failed: Key {key} should exist"
    assert not bst.find(100), "Test Failed: Key 100 should not exist"
    cPass("Test insert and find passed")

def test_duplicate_key():
    bst = BSTMap()
    bst.insert((10, 'initial'))
    bst.insert((10, 'updated'))
    
    assert bst.find(10), "Test Failed: Key 10 should exist"
    cPass("Test duplicate key handling passed (value update assumed)")

if __name__ == "__main__":
    print("\nRunning BSTMap Tests...\n")
    test_insert_and_find()
    test_duplicate_key()
    print("\nAll BSTMap tests passed successfully!\n")
