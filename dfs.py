from collections import deque
# 리스트, 스택을 이용. 

def dfs_list(graph, start_node):
    need_visited , visited = list(), list() 
    # 방문한 노드 visited, 방문이 필요한 노드: need_visited
    need_visited.append(start_node)
    #시작노드 추가.
    while need_visited : 
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

# deque이용
def dfs_deque (graph, start_node):
    visited = []
    need_visited= deque()
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

#재귀함수 이용
def dfs_recursive(graph, start, visited= []):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited 

#재귀함수 및  방문정보 이용
def dfs_recursive2(graph, n, visited):
    visited[n] = True
    print(n, end = " ")
    for i in graph[n]:
        if not visited[i]:
            dfs_recursive2(graph, i, visited)
        
        

graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

graph2 =[
  [], # 노드번호가 1부터 시작하기 때문에 0은 비우기.
  [2,3,8], 
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
print("리스트로 구현", dfs_list(graph, 'A'))
print("deque로 구현", dfs_deque(graph,'A')) 
print("재귀함수로 구현", dfs_recursive(graph, 'A'))

visited = [False]*(8+1)
dfs_recursive2(graph2,1,visited)