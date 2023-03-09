from collections import deque

def bfs(graph, start_node):
    need_visited, visited = [] , []
    need_visited.append(start_node)
    while need_visited:
        node = need_visited[0]
        del need_visited[0]

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    
    return visited 

def bfs_recursive(graph, start, visited):
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


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
#graph['A'].append('L')
print(bfs(graph,'A'))
print(graph)