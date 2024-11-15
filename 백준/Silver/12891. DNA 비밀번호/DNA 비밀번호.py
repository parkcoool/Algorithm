S, P = map(int, input().split())
word = input()
A, C, G, T = map(int, input().split())

ans = 0
start = 0
first_word = word[:P]
count = {
    "A": first_word.count("A"),
    "C": first_word.count("C"),
    "G": first_word.count("G"),
    "T": first_word.count("T")
}
while start + P <= S:
    if count["A"] >= A and count["C"] >= C and count["G"] >= G and count["T"] >= T:
        ans += 1

    count[word[start]] -= 1
    start += 1
    if start + P - 1 < S:
        count[word[start + P - 1]] += 1
    
print(ans)