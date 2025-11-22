import heapq
def heuristic(a, b):
    # Manhattan distance
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star(maze, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_list:
        f, g, current = heapq.heappop(open_list)
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
                    tentative_g = g + 1
                    if n not in g_score or tentative_g < g_score[n]:
                        g_score[n] = tentative_g
                        f_score = tentative_g + heuristic(n, goal)
                        heapq.heappush(open_list, (f_score, tentative_g, n))
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
goal = (3, 2)

path = a_star(maze, start, goal)
print("a_star Path found:", path)
