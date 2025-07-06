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

try:
    # input
    n = int(input())
    if n <= 0:
        raise ValueError("n must be a positive integer")
    arr = input().split(" ")
    if len(arr) != n:
        raise ValueError("The number of elements does not match n")
    # yeu cau danh sach so int
    arr = [int(x) for x in arr]
    target = int(input())
    
    # thuc thi thuat toan
    arr.sort()
    result = binarySearch(arr, target)
    print(result)
except Exception as e:
    print("Error:", e)
finally:
    print("End.")