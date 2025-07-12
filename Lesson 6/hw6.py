import random
import time

def linearSearch(num_list, target):
    if not num_list:
        return -1
    for index, value in enumerate(num_list):
        if value == target: return index
    return -1

def binarySearch(arr, target):
    if not arr:
        return -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (high-low)//2 + low
        if arr[middle] == target:
            return middle
        if arr[middle]<target:
            low = middle+1
        elif arr[middle]>target:
            high = middle-1
            
    return -1
    
def testSearch(arr, target, arr_length):
    sorted_arr = arr.sort()
    print(f"The array has {arr_length} values.")
    print("-----------")
    
    start = time.time()
    res_linear = linearSearch(sorted_arr, target)
    end = time.time()
    print("Linear Search")
    print(f"Output: {res_linear}")
    print(f"Time: {(end - start):.6f}s")
    
    print("-----------")
    
    start = time.time()
    res_binary = binarySearch(sorted_arr, target)
    end = time.time()
    print("Binary Search")
    print(f"Output: {res_binary}")
    print(f"Time: {(end - start):.6f}s")
    
    print("\n")
    
for i in [10, 100, 1000, 10000]:
    arr = random.sample(range(i * 5), i)
    random_target = random.randint(0, i)
    testSearch(arr, random_target, i)