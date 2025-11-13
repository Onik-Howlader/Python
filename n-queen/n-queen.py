# def is_safe(queens, row, col):
#     return all(c != col and abs(r - row) != abs(c - col) for r, c in enumerate(queens[:row]))

# def dfs(queens, row, n, sols):
#     if row == n:
#         sols.append(queens[:]); return
#     for col in range(n):
#         if is_safe(queens, row, col):
#             queens[row] = col
#             dfs(queens, row + 1, n, sols)

# def solve_n_queens(n=4):
#     sols, queens = [], [-1]*n
#     dfs(queens, 0, n, sols)
#     return sols

# # ---- Output ----
# for k, sol in enumerate(solve_n_queens(4), 1):
#     print(f"Solution {k}:")
#     for r in range(len(sol)):
#         print(" ".join("Q" if sol[r] == c else "." for c in range(len(sol))))
#     print("Queens at columns:", sol, "\n")

def is_safe(queens, row, col, n):
    for r in range(row):
        c = queens[r]
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def dfs(queens, row, n, solutions):
    if row == n:
        solutions.append(queens[:])
        return
    for col in range(n):
        if is_safe(queens, row, col, n):
            queens[row] = col
            dfs(queens, row + 1, n, solutions)
            queens[row] = -1

def solve_n_queens(n=4):
    queens = [-1] * n
    solutions = []
    dfs(queens, 0, n, solutions)
    return solutions

solutions = solve_n_queens(4)
for sol in solutions:
    for r in range(4):
        print(" ".join("Q" if sol[r] == c else "." for c in range(4)))
    print()