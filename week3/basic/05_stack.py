"""
[스택 - 괄호 짝 맞추기]

문제 설명:
- 스택(Stack)을 사용하여 괄호가 올바르게 짝지어져 있는지 확인합니다.
- LIFO (Last In First Out) 구조를 활용합니다.

입력:
- s: 괄호 문자열 (예: "(())", "(()")

출력:
- True: 올바른 괄호
- False: 잘못된 괄호

예제:
입력: "(())"
출력: True

입력: "(()"
출력: False

힌트:
- 여는 괄호 '('는 스택에 push
- 닫는 괄호 ')'를 만나면 스택에서 pop
- 마지막에 스택이 비어있으면 True
"""

def is_valid_parentheses(s):
    """
    괄호 짝이 맞는지 확인
    
    Args:
        s: 괄호 문자열
    
    Returns:
        올바른 괄호면 True, 아니면 False
    """
    stack = []
    for ch in (s):
        # 입력깂의 1번쩨 값을 ch에 넣는다.
        if ch=="(":
            stack.append(ch)
        # ch가 "("일 경우에 스택이라는 리스트에 넣는다
        else:
        # 아닐경우에는
            if not stack:
                return False
        # 스탱이 비어있을 상태라면 거짓을 뱉는다 왜냐 )(의 경우는 무조건 성립이 될수없기에
            stack.pop()
        # 들어있는경우 스택에 마지막에 들어간 값을 삭제한다
    if len(stack) == 0:
    # 위 내용을 끝낸후 스택이 비어있을경우 사실이며
        return True
    else:
        return False
    # 남아있는경우에는 거짓이 나온다
    

    # TODO: 문자열의 각 문자를 순회
    ## : 여는 괄호 '('면 스택에 추가
    ## : 닫는 괄호 ')'면
    ## 스택이 비어있으면 False 반환
    ## 아니면 스택에서 pop
    

    
    # TODO: 반복이 끝나면 스택이 비어있는지 확인
    pass

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "(())"
    result1 = is_valid_parentheses(test1)
    print(f"입력: {test1}")
    print(f"결과: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "(()"
    result2 = is_valid_parentheses(test2)
    print(f"입력: {test2}")
    print(f"결과: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "()(())"
    result3 = is_valid_parentheses(test3)
    print(f"입력: {test3}")
    print(f"결과: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "())("
    result4 = is_valid_parentheses(test4)
    print(f"입력: {test4}")
    print(f"결과: {result4}")


