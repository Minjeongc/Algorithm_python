# 가중치 그래프, 인접 행렬

INF = 2147000000

graph1 = [
    [0, 7, 3],
    [7, 0, INF],
    [3, INF, 0]
]

# 가중치 그래프, 인접 리스트

graph2 = [[] for _ in range(3)]

graph2[0].append((1,7))
graph2[0].append((2,3))
graph2[1].append((0,7))
graph2[2].append((0,3))

print(graph2)