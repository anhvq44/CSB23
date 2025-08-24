from collections import deque

def count_hungry_students(sandwiches, students):
    students = deque(students)
    sandwiches = deque(sandwiches)

    count = 0
    while students and sandwiches:
        # lay phan tu o dau 2 danh sach
        if students[0] == sandwiches[0]:
            students.popleft()
            sandwiches.popleft()
            count = 0
        else:
            # neu khong trung khop -> day student xuong cuoi
            std = students.popleft()
            students.append(std)
            count += 1
            # neu xoay het 1 lan -> dung
            if count == len(students):
                break

    return len(students)

print(count_hungry_students([1,1,0,0], [0,1,0,1]))  # KQ: 0
print(count_hungry_students([1,1,1,0,0,1], [1,0,0,0,1,1]))  # KQ: 3