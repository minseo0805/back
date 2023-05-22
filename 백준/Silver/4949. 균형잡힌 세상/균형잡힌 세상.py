while True :
    a = input()
    stack = []

    if a == "." : #종료 조건 
        break

    for i in a : 
        if i == '[' or i == '(' :
            stack.append(i) 
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 짝이 맞으면 지워서 stack을 비우기
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')