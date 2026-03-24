from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)

    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트

    Returns:
        위상 정렬 순서
    """
    # 1. 그래프와 진입 차수 초기화
    graph = [[] for _ in range(vertices)]
    in_degree = [0] * vertices

    # 2. 그래프 구성 및 진입 차수 계산
    for a, b in edges:
        graph[a].append(b)
        in_degree[b] += 1

    # 3. 진입 차수가 0인 정점들을 큐에 추가
    queue = deque()
    for i in range(vertices):
        if in_degree[i] == 0:
            queue.append(i)

    result = []

    # 4. 큐가 빌 때까지 반복
    while queue:
        current = queue.popleft()
        result.append(current)

        # 현재 정점과 연결된 다음 정점들의 진입 차수 감소
        for next_node in graph[current]:
            in_degree[next_node] -= 1

            # 진입 차수가 0이 되면 큐에 추가
            if in_degree[next_node] == 0:
                queue.append(next_node)

    return result


# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]

    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()

    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")