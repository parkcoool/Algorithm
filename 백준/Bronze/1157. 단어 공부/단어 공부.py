word = input().upper()
word_list = list(set(word))
lst = []

for i in word_list:
    count = word.count(i)
    lst.append(count)

if lst.count(max(lst))>= 2:
    print("?")
else:
    print(word_list[lst.index(max(lst))])