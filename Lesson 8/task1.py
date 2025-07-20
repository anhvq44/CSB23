# Method 1 O(n) where n is the length of arr_2
def med_1(arr_1, arr_2):
    arr_1_set = set(arr_1)
    res = []
    for i in arr_2:
        if i in arr_1_set:
            res.append(i)
    return res

# Method 2
def med_2(arr_1, arr_2):
    res=[]
    for i in arr_1:
        if (i in arr_2) and (i not in res):
            res.append(i)
    return res

arr_1 = []
len_arr1 = int(input("First array's length: "))
for i in range(len_arr1):
    item = input(f'Input the {i+1} value: ')
    if item: arr_1.append(item)

arr_2 = []
len_arr2 = int(input("Second array's length: "))
for n in range(len_arr2):
    item2 = input(f'Input the {n+1} value: ')
    if item2: arr_2.append(item2)

if arr_1 and arr_2:
    fin_res = med_1(arr_1, arr_2)
    print(fin_res)