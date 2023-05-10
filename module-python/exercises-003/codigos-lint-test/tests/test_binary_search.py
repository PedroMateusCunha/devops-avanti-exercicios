import sys, os
up_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(up_directory)
from binary_search import *

def test__element_present():
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    x = 23
    assert binary_search(arr, 0, len(arr)-1, x) == 5

def test__element_not_present():
    arr = [3, 9, 15, 22, 33, 40, 57, 63, 79]
    x = 12
    assert binary_search(arr, 0, len(arr)-1, x) == -1

def test__single_element():
    arr = [8]
    x = 8
    assert binary_search(arr, 0, len(arr)-1, x) == 0

def test__empty_array():
    arr = []
    x = 10
    assert binary_search(arr, 0, len(arr)-1, x) == -1

def test__multiple_elements_not_present():
    arr = [2, 4, 4, 4, 7, 8, 8, 9, 10]
    x = 5
    assert binary_search(arr, 0, len(arr)-1, x) == -1

def test__large_array():
    arr = [i for i in range(1, 1000001)]
    x = 500000
    assert binary_search(arr, 0, len(arr)-1, x) == 499999

def test__negative_numbers():
    arr = [-8, -4, 0, 3, 6, 9, 12]
    x = -8
    assert binary_search(arr, 0, len(arr)-1, x) == 0