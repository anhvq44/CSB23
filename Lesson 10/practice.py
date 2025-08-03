import string
#Đếm số lần xuất hiện của 1 từ trong văn bản
def CountWords(paragraph):
    paragraph = paragraph.lower()
    
    for char in string.punctuation:
        paragraph = paragraph.replace(char, ' ')
        
    words = paragraph.split()
    
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
            
    return words_count

text = "It was a weird concept. Why would I really need to generate a random paragraph? Could I actually learn something from doing so? All these questions were running through her head as she pressed the generate button. To her surprise, she found what she least expected to see."
res = CountWords(text)
max = 0
word_count_max = ""
for word, counter in sorted(res.items()):
    if counter > max:
        max = counter
        word_count_max = word
    print(f"{word}: {counter}")

print(f"Từ với số lần lặp nhiều nhất: {word_count_max}, lặp {max} lần")