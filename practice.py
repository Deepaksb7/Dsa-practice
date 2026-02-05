
# def binary_search(arr , tar):
#     start= 0
#     end=len(arr) -1
#     while start <= end:
#         mid = (start+end)//2
#         if arr[mid] == tar:
#             return mid
#         elif arr[mid] < tar:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return -1


# tar=12

# arr = [2,4,6,8,10,12,14,16]
# print(binary_search(arr,tar))


# def dfs(graph, node, visited):
#     if node not in visited:
#         print(node,end="")
#         visited.add(node)

#         for neg in graph[node]:
#             if neg not in visited:
#                 dfs(graph,neg,visited)

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': [],
#     'F': []
# }
# visited = set()
# dfs(graph, 'A', visited)


# def dfs_itrative(graph,start):
#     visited= set()
#     stack = [start]

#     while stack:
#         node = stack.pop()
#         print(node,end='')
#         visited.add(node)

#         for neg in reversed(graph[node]):
#             if neg not in visited:
#                 stack.append(neg)


# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': [],
#     'F': []
# }

# dfs_itrative(graph,"A")


# from collections import deque
# def bfs(graph,start):
#     visited = set()
#     queue = deque([start])

#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node , end='')
#             visited.add(node)
#             for neg in graph[node]:
#                 queue.append(neg)


# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': [],
#     'F': []
# }
# bfs(graph,'A')



# def backtracking(start,path):
#     print(path)

#     for i in range(start,len(num)):
#         path.append(num[i])
#         backtracking(i+1,path)
#         path.pop()

# num=[1,2,3]
# backtracking(0,[])



# def is_safe(maze,x,y,n):
#     return (0 <= x < n and 0 <= y < n and maze[x][y] == 1)

# def solve_maze(maze, x, y , path ,n):

#     if (x == n - 1 and y == n - 1):
#         print(path)
#         return

#     direction = [(0,1,"R"),(1,0,'D'),(0,-1,'L'),(-1,0,'U')]

#     for dx,dy,move in direction:
#         nx,ny = dx + x , dy + y

#         if is_safe(maze, nx,ny, n):
#             maze[nx][ny] = 0
#             solve_maze(maze, nx,ny,path+move,n)
#             maze[nx][ny] = 1 

# maze = [
#     [1, 0, 0, 0],
#     [1, 1, 0, 1],
#     [1, 1, 0, 0],
#     [0, 1, 1, 1]
# ]

# n= len(maze)
# maze[0][0] = 0 
# solve_maze(maze,0,0,'',n)



 