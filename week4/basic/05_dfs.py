"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
    """

def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
# 재귀를 통한 풀이
def dfs(graph, start, visited=None):
    # 방문 리스트 없으면 생성
    if visited is None:
        visited = []
    # 이부분은 동일하게 방문리스트를 만드는것이다
    visited.append(start)
    # 출발지점을 더해라.
    # 현재 노드와 연결된 노드들 확인
    for next_node in graph[start]:
    #다음 노드에 넣어라 스타트값을 1,2가될것이다 
        if next_node not in visited:
        # 다음 노드가 방문자 리스트에 없다면 실행한다 
            dfs(graph, next_node, visited)
            # 재귀를 사용한다
    # 이러면 이함수는 0123 이라는 결과 값이 나온다 for문을통한 깊이탐색을 실행한다.
    # 이방식은 다음것을 알아서정해준다 예를 들자면 1이끝나면 다동적으로 2로간다
    return visited

#  스택버전 
def dfs_stack(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        # 내생각에는 사실상 넓이탐색의 큐 사용방식과 비슷하다고 생각하였다
        if node not in visited:
        # 만약에 노드가 방문자 리스트에 없다면 추가해라
            visited.append(node)
            # 사실상 visited=[0]이다 

            for next_node in reversed (graph[node]):
            # 다음노드에 넣어라 그래프의 노드의 값을 즉 처음에 2,1 이될것인데 왼쪽부터돌아야하기에 거꾸로를 사용하였다 
                if next_node not in visited:
                # 민약에 다음노드가 방문자리스트에 없다면 추가해라
                    stack.append(next_node)
        # 이방식은 갈곳을 스택을 통해 지정을 해준다 사실상 0213 이될수도있는데 안정성있게 0123가 된다
    return visited

    	# 재귀는 함수 호출로 깊게 들어감
	    # 스택은 리스트(stack)로 깊게 들어감
	    # 공부할 때, 트리 문제, 코테의 간단한 DFS → 재귀 많이 씀
	    # 입력이 크거나, 실무에서 안정성이 중요할 때 → 스택 많이 씀

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


