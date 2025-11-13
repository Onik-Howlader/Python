# BFS
# from collections import deque

# with open("maze.txt") as f:
#     maze = [line.split() for line in f.read().splitlines()]

# r_max, c_max = len(maze), len(maze[0])
# start = goal = None
# for r in range(r_max):
#     for c in range(c_max):
#         if maze[r][c] == 'A': start = (r,c)
#         if maze[r][c] == 'B': goal = (r,c)

# q = deque([start])
# visited = {start}
# parent = {}
# while q:
#     r,c = q.popleft()
#     if (r,c) == goal: break
#     for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
#         nr,nc = r+dr,c+dc
#         if 0<=nr<r_max and 0<=nc<c_max and maze[nr][nc]!='#' and (nr,nc) not in visited:
#             visited.add((nr,nc))
#             parent[(nr,nc)] = (r,c)
#             q.append((nr,nc))

# path = []
# cur = goal
# while cur != start:
#     path.append(cur)
#     cur = parent[cur]
# path.append(start)
# path.reverse()

# for row in maze:
#     print(" ".join(row))
# print("\nPath coordinates:")
# print(", ".join(map(str, path)))
# print(f"Start: {start}")
# print(f"Final: {goal}")


#DFS
from collections import deque 

with open("maze.txt") as f:
    maze = [line.split() for line in f.read().splitlines()]

r_max, c_max = len(maze), len(maze[0])
start = goal = None
for r in range(r_max):
    for c in range(c_max):
        if maze[r][c] == 'A': 
            start = (r, c)
        if maze[r][c] == 'B': 
            goal = (r, c)

# DFS stack
stack = [start]
visited = {start}
parent = {}
found = False

while stack:
    r, c = stack.pop()   # DFS uses LIFO (stack)
    if (r, c) == goal:
        found = True
        break
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < r_max and 0 <= nc < c_max and maze[nr][nc] != '#' and (nr, nc) not in visited:
            visited.add((nr, nc))
            parent[(nr, nc)] = (r, c)
            stack.append((nr, nc))

# Path reconstruct
path = []
if found:
    cur = goal
    while cur != start:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    path.reverse()

    for row in maze:
        print(" ".join(row))
    print("\nPath coordinates:")
    print(", ".join(map(str, path)))
    print(f"Start: {start}")
    print(f"Final: {goal}")
else:
    print("No path found.")
