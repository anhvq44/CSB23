brackets = {
    '(': ')',
    '[': ']',
    '{': '}'
}

def check_valid_brackets(input=None):
    if (input is None) or (len(input)%2 !=0) or (len(input)==0):
        return "False"
    
    left = 0
    right = len(input) - 1
    
    while right>left:
        if input[left] in brackets:
            if input[right] == brackets[input[left]]:
                left+=1
                right-=1
                continue
            else:
                return "False"
            
    return "True"

input = input("Input a string: ")
print(check_valid_brackets(input.strip()))