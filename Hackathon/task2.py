nums = [3, 2, 3]
seen_count = {}
result = []

for number in nums:
    if number in seen_count:
        seen_count[number] += 1
    else:
        seen_count[number] = 1
        
    if seen_count[number] > int((len(nums)/3)):
        result.append(number)
        
print(result)