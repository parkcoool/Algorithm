def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    for i in range(len(phone_book) - 1):
        if sorted_phone_book[i + 1].startswith(sorted_phone_book[i]):
            return False
    
    return True