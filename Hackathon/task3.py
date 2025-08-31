path = "/home/"
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