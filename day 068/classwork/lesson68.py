def stone_scoring(board):
    rows = len(board)
    cols = len(board[0])
    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols
    def dfs(x, y, color):
        stack = [(x, y)]
        group = set()
        liberties = set()
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in group:
                continue
            group.add((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if in_bounds(nx, ny):
                    if board[nx][ny] == color:
                        if (nx, ny) not in group:
                            stack.append((nx, ny))
                    elif board[nx][ny] == "W" or board[nx][ny] == "B":
                        liberties.add((nx, ny))
        return group, liberties
    visited = set()
    scores = {"B": 0, "W": 0}
    for r in range(rows):
        for c in range(cols):
            if board[r][c] in "BW" and (r, c) not in visited:
                color = board[r][c]
                group, liberties = dfs(r, c, color)
                visited.update(group)
                scores[color] += len(group) + len(liberties)
    
    if scores["B"] > scores["W"]:
        return "B"
    elif scores["W"] > scores["B"]:
        return "W"
    else:
        return "Draw"
board = [
    ["W", "W", "W", "B", "B", "B"],
    ["W", "W", "W", "W", "B", "B"],
    ["W", "W", "W", "B", "B", "B"],
    ["W", "X", "W", "B", "B", "B"],
    ["X", "W", "B", "B", "B", "B"],
    ["W", "W", "B", "X", "B", "X"]
]

print(stone_scoring(board)) 
