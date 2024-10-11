def solution(phone_book):
    dic = {}

    for number in phone_book:
        dic[number] = 1
        
    for number in phone_book:
        temp = ""
        for n in number:
            temp += n
            if temp in dic and temp != number:
                return False
    
    return True