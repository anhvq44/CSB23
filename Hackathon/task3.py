path = input("Input path: ")
if len(path) > 3000 or len(path) < 1:
    print("Invalid input.")
path_items = path.split('/')
result = []

for item in path_items:
    if item == '' or item == '.':
        continue
    elif item == '..':
        if result:
            result.pop()
    else:
        result.append(item)

print('/' + '/'.join(result))