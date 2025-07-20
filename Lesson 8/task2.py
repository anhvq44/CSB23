color_code = {'r': 1, 'w': 2, 'b': 3}

def SortColorMe(arr):
    res=[]
    # Method 1: O(2n)?
    red = 0
    white = 0
    blue = 0
    for i in arr:
        if i == "r":
            red+=1
        elif i == "w":
            white+=1
        elif i == "b":
            blue+=1
    for r in range(red): res.append('r')
    for w in range(white): res.append('w')
    for b in range(blue): res.append('b')
    return res

    
# Method 2: Insertion sort O(n^2)
def insertion_sort_color(arr):
    for i in range(1, len(arr)):
        insert_index = i
        current_val = arr.pop(i)
        for j in range(i - 1, -1, -1):
            if arr[j]>current_val:
                insert_index = j
        arr.insert(insert_index, current_val)
    return arr
    
def ColorToNum(color_arr):
    global color_code
    result = []
    for c in color_arr:
        result.append(color_code[c])
        
    if len(result) != len(color_arr):
        raise ValueError("The color array is invalid")
    return result

def NumToColor(num_arr):
    global color_code
    result = []
    for n in num_arr:
        for key, value in color_code.items():
            if value == n:
                result.append(key)
    if len(num_arr) != len(result):
        raise ValueError("Invalid color code")
    return result

def TestDrive():
    print("Start----------------")
    color_arr = input("Input:")
    try:
        color_arr = color_arr.split(" ")
        color_code_lst = ColorToNum(color_arr)
        sorted_color_lst = insertion_sort_color(color_code_lst)
        fin_lst = NumToColor(sorted_color_lst)
        print(fin_lst)
    except Exception as e:
        print("Error:", e)
    finally:
        print("End----------------")
        
TestDrive()