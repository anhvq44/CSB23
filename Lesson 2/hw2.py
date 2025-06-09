user_input = input("Nhập vào các số nguyên được ngăn cách bởi dấu cách: ")
numbers = list(map(int, user_input.split()))
total = 0
average = 0
length = 0
for i in numbers:
    if(i%2 == 0):
        total+=i
        length+=1
average = total/length
print("Trung bình cộng của dãy số là:", average)