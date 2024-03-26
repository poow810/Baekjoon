import sys


def check(string):

    stack = []
    for i in string:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) == 0:
        return True
    else:
        return False 


while True:
    string = input()
    
    if string == ".":
        exit()

    if check(string):
        print("yes")
    else:
        print("no")

