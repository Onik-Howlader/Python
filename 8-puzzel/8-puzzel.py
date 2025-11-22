import copy


def find_zero(p_state):
    x = 0
    while True:
        if 0 in p_state[x]:
            y = p_state[x].index(0)
            return x, y
        else:
            x = x+1


def position_check():
    while queue[0] != t_state:
        print(queue[0])
        print('Solution Found: ')
        index = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        x, y = find_zero(queue[0])
        for a in index:
            i = a[0]+x
            j = a[1]+y
            if i >= 0 and j >= 0 and i < n and j < n:
                temp_state = copy.deepcopy(queue[0])
                temp_state[x][y] = temp_state[i][j]
                temp_state[i][j] = 0
                print(temp_state)

                if temp_state in pop_list:
                    a = 1
                elif temp_state == t_state:
                    print(temp_state)
                    print("result Found")
                    return 0
                else:
                    queue.append(temp_state)
                    pop_list.append(temp_state)
        queue.pop(0)
        print('New State:')
    print(queue[0])


p_state = [[2, 5, 1], [7, 0, 8], [3, 4, 6]]
t_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
print(t_state)
print('BFS START:')
n = len(p_state)
queue = []
pop_list = []
queue.append(p_state)
pop_list.append(p_state)
position_check()

# import copy
# import heapq

# # find position of 0 (blank tile)


# def find_zero(p_state):
#     for i in range(len(p_state)):
#         if 0 in p_state[i]:
#             return i, p_state[i].index(0)

# # heuristic function: misplaced tiles


# def heuristic(state, goal):
#     h = 0
#     for i in range(len(state)):
#         for j in range(len(state[i])):
#             if state[i][j] != 0 and state[i][j] != goal[i][j]:
#                 h += 1
#     return h


# def position_check():
#     # priority queue: (heuristic, state)
#     while queue:
#         h, current = heapq.heappop(queue)
#         print("Current State (h =", h, "):")
#         for row in current:
#             print(row)
#         print()

#         if current == t_state:
#             print("✅ Goal Found!")
#             return

#         x, y = find_zero(current)
#         moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

#         for dx, dy in moves:
#             i, j = x + dx, y + dy
#             if 0 <= i < n and 0 <= j < n:
#                 temp_state = copy.deepcopy(current)
#                 temp_state[x][y], temp_state[i][j] = temp_state[i][j], temp_state[x][y]

#                 if temp_state not in visited:
#                     h_new = heuristic(temp_state, t_state)
#                     heapq.heappush(queue, (h_new, temp_state))
#                     visited.append(temp_state)


# # initial & goal states
# p_state = [[2, 5, 1],
#            [7, 0, 8],
#            [3, 4, 6]]

# t_state = [[1, 2, 3],
#            [4, 0, 5],
#            [6, 7, 8]]

# print("Target State:")
# for row in t_state:
#     print(row)

# print("\nBest First Search START:\n")
# n = len(p_state)
# queue = []
# visited = []

# # push initial state with heuristic
# heapq.heappush(queue, (heuristic(p_state, t_state), p_state))
# visited.append(p_state)

# position_check()
