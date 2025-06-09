num = int(input("Nhập 1 số: "))
total = 0
factors = []
for i in range(1, num+1):
    if(i%2==0):
        total+=i
    if((num%i == 0) and (num!=0)):
        factors.append(i)
        
print(f'Tổng các số lẻ từ 1 đến {num}: {total}')
if((len(factors) == 2) and (num>1)):
    print(f'{num} là số nguyên tố')
else:
    print(f'{num} không phải là số nguyên tố')

if(num!=0): 
    print(f'Các ước số của {num}: {factors}')
else:
    print('Mọi số nguyên đều là ước của số 0')