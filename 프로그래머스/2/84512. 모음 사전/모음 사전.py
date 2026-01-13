def solution(word):
    word = list(word)
    ans = 1
    
    while word != ["A"]:
        if word[-1] == "A": word.pop()
        else:
            if word[-1] == "U": word[-1] = "O"
            elif word[-1] == "O": word[-1] = "I"
            elif word[-1] == "I": word[-1] = "E"
            elif word[-1] == "E": word[-1] = "A"
            word += ["U"] * (5 - len(word))
        ans += 1
        
    return ans