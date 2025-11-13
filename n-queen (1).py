import tkinter as tk

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

def solve_n_queens(n):
    queens = [-1] * n
    solutions = []
    dfs(queens, 0, n, solutions)
    return solutions

def show_solutions(n):
    solutions = solve_n_queens(n)
    root = tk.Tk()
    root.title(f"{n}-Queens Problem ({len(solutions)} solutions)")

    for sol_index, sol in enumerate(solutions, start=1):
        frame = tk.LabelFrame(root, text=f"Solution {sol_index}", padx=5, pady=5)
        frame.pack(padx=10, pady=5)

        for r in range(n):
            for c in range(n):
                cell = "Q" if sol[r] == c else "."
                label = tk.Label(frame, text=cell, width=2, height=1, borderwidth=1, relief="solid",
                                 font=("Arial", 14))
                label.grid(row=r, column=c)

    root.mainloop()
    
n = int(input("Enter value of n: "))
show_solutions(n)
