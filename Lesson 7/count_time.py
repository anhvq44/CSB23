import random

arr1 = random.sample(range(100), 10)
arr2 = random.sample(range(100), 10)

# def bubble_sort(arr):
#     swapped_count = 0
#     print("Array chua sort:", arr)
#     for i in range(len(arr)):
#         swapped = False
#         for j in range(0, len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#                 swapped_count+=1
#                 print(f"Lan swap thu {swapped_count:02}: {arr}")
#         if not swapped:
#             break
# bubble_sort(arr1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert_index = i
        current_val = arr.pop(i)
        print(f"Cat phan tu {current_val}: {arr}")
        for j in range(i - 1, -1, -1):
            if arr[j]>current_val:
                insert_index = j
        arr.insert(insert_index, current_val)
        print(f"Lan chen {i:02}: {arr}")
    return arr

res = insertion_sort(arr2)
print(f"Result: {res}")