import random
import time

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert_index = i
        current_val = arr.pop(i)
        for j in range(i - 1, -1, -1):
            if arr[j]>current_val:
                insert_index = j
        arr.insert(insert_index, current_val)
    return arr

def testSort(arr1, arr2, arr_length):
    print(f"The array has {arr_length} values.")
    print("-----------")
    
    print("Bubble Sort")
    print(f"A part of the input: {arr1[0:5]}")
    start = time.time()
    res_bubble = bubble_sort(arr1)
    end = time.time()
    print(f"Output: {res_bubble}")
    print(f"Time: {(end - start):.6f}s")
    
    print("-----------")
    
    print("Insertion Sort")
    print(f"A part of the input: {arr2[0:5]}")
    start = time.time()
    res_insertion = insertion_sort(arr2)
    end = time.time()
    print(f"Output: {res_insertion}")
    print(f"Time: {(end - start):.6f}s")
    
    print("\n")
    
for i in [10, 50, 100]:
    arr1 = random.sample(range(i * 5), i)
    arr2 = random.sample(range(i * 5), i)
    testSort(arr1, arr2, i)