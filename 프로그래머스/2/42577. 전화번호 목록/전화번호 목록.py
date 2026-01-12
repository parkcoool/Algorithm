def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    for i in range(len(phone_book) - 1):
        phone = sorted_phone_book[i]
        if sorted_phone_book[i + 1][:len(phone)] == phone: return False
    
    return True