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

print("리스트로 구현", dfs_list(graph, 'A'))
print("deque로 구현", dfs_deque(graph,'A')) 
print("재귀함수로 구현", dfs_recursive(graph, 'A'))