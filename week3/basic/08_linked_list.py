"""
[연결 리스트 - Linked List 기본 구현]

문제 설명:
- 단순 연결 리스트를 구현합니다.
- 노드는 값과 다음 노드를 가리키는 포인터를 가집니다.

입력:
- 연결 리스트에 추가할 값들

출력:
- 연결 리스트의 모든 값 출력

예제:
입력: 1 -> 2 -> 3
출력: [1, 2, 3]

힌트:
- Node 클래스: data와 next 포인터
- LinkedList 클래스: head 포인터
- append(): 끝에 추가
- print_list(): 모든 노드 출력
"""

class Node:
    """연결 리스트의 노드"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """단순 연결 리스트"""
    def __init__(self):
    # ll = LinkedList()리스트를 만들시에 이포멧을 적용한다
        self.head = None
        # 리스트의 내용은 비워져있다

        
    def append(self, data):
    # 노드를 더해준다 11이란 리스트의 1이란는 데이터에게 즉 데이터값은 있지만 현제 노드는 존재하지 않는다
        new_node = Node(data)
        # self.data = 1
        #self.next = None 이게 현재의 상태이다.

        if self.head == None:
        # 만약 해드가 없을경우
            self.head = new_node
        #   이값은 헤더이다
        current = self.head
             #current 는 헤더의 별명이다
        while current.next != None:
            # 헤더 다음값이 없을경우 브레이크 있으경우에 성립
            current = current.next
            # 헤는 같다 헤더다음?
        current.next = new_node
        # current의 주소 즉노드는 새로운
        
        return self.head
    
    def print_list(self):
        """리스트의 모든 값 출력"""
        values = []
        
        current = self.head
        while current != None:
            values.append(current.data)
            current = current.next
        
        return values

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 연결 리스트 테스트 ===")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    result = ll.print_list()
    print(f"리스트: {result}")
    print()
    
    # 테스트 케이스 2
    print("=== 연결 리스트 테스트 2 ===")
    ll2 = LinkedList()
    ll2.append(10)
    ll2.append(20)
    ll2.append(30)
    ll2.append(40)
    result2 = ll2.print_list()
    print(f"리스트: {result2}")


