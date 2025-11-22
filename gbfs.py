import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def gbfs(maze, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start))
    came_from = {}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        visited.add(current)
        neighbors = [(current[0]+dx, current[1]+dy)
                     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        
        for n in neighbors:
            if 0 <= n[0] < len(maze) and 0 <= n[1] < len(maze[0]):
                if maze[n[0]][n[1]] == 0 and n not in visited:
                    heapq.heappush(open_list, (heuristic(n, goal), n))
                    if n not in came_from:
                        came_from[n] = current
    return None
# Example maze (0 = free, 1 = blocked)
maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

start = (0, 0)
goal = (3, 3)

path = gbfs(maze, start, goal)
print("Path found:", path)
