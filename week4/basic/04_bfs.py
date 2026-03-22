from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited = [] #방문한 거 저장할 리스트
    queue = deque() # 큐 생성
    # TODO: 큐 생성 및 시작 정점 추가
    ## 방문한 정점 집합
    queue.append(start) #큐에 start를 넣는다
    # queue=(0)
    visited.append(start) #visited에 start를 넣는다
    # visited=(0)

    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들 확인
    ## 방문하지 않은 정점이면 큐에 추가
    while len(queue) > 0 : #큐가 비지 않았다면
        cur = queue.popleft() 
        #front를 pop

        for nx in graph[cur]: 
        #for nx in graph[0]:
        # nx 1,2
            if(nx < 0 or nx > 3): #nx가 칸 넘어가면 continue
                continue
            if(nx not in visited): #nx가 visited에 없으면
                visited.append(nx)
                queue.append(nx)
    
    
    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")