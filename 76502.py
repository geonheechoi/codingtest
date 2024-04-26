def is_correct(s): # "올바른 괄호 문자열"인지 체크하는 함수
    open0 = ["(", "{", "["]
    closed0 = [")", "}", "]"]
    
    stack = [] # 열린 괄호를 순차적으로 넣기 위한 스택
    for elem in s:
        if not stack: # 스택이 비었다면 무조건적으로 채우기
            stack.append(elem)
        else: # 스택에 뭔가가 들어있다면
            if stack[-1] in closed0: # 스택의 가장 위의 데이터가 닫는 괄호라면
                return False # 스택에는 여는 괄호만 있어야 되는데... 뭔가 이상하다! -> False
            else: # 스택의 가장 위의 데이터가 여는 괄호일 때
                if elem in open0: # s의 원소가 여는 괄호이면 스택에 넣기
                    stack.append(elem)
                else: # 스택의 가장 위 데이터가 닫는 괄호일 때 (중요!)
                    if open0.index(stack[-1]) == closed0.index(elem): # 괄호의 짝이 맞다면
                        stack.pop() # 스택의 가장 위를 꺼냄
                    else:
                        return False # 짝이 맞지 않다면 False를 출력
    if not stack: # 맨 마지막에 스택이 비었을 때 
        return True # 그 때만 True를 반환하고
    else: # 맨 마지막까지도 스택이 완전히 비어있지 않다면
        return False # 그 때는 뭔가 짝이 안 맞았다는 것이므로 False를 출력
            

def solution(s):
    count = 0 # 회전해가면서 "올바른 괄호 문자열"이 몇 개 나오는지 개수를 세는 변수
    for _ in range(len(s)): # 회전 -> s의 길이에 해당하는 양만큼 반복
        if is_correct(s): # 올바른 괄호 문자열이면
            count += 1 # 경우의 수에 포함
        else:
            pass # 그렇지 않으면 넘어감
        s = s[1:] + s[0] # 문자열 회전
    
    return count
