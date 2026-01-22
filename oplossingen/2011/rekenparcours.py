import re

n = int(input())

for _ in range(n):
    h, w = map(int, input().split(" "))
    grid = []
    for y in range(h):
        grid.append(list(input()))

    seen = {}

    def f(cx, cy, visited, s):
        key = (cx, cy, visited, s)
        if key in seen:
            return False
        seen[key] = None

        if visited == 2 ** (w * h) - 1:
            if s[-1].isnumeric():
                if eval(re.sub(r"0*(\d+)", r"\1", s).replace("=", "==").replace("x", "*")):
                    print(s)
                    return True
            return False

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = cx + dx
            ny = cy + dy
            if not (0 <= nx < w and 0 <= ny < h):
                continue

            nm = 1 << (nx + ny * w)
            if visited & nm:
                continue

            ds = grid[ny][nx]
            if s == "" and not ds.isnumeric():
                continue
            if s and not s[-1].isnumeric() and not ds.isnumeric():
                continue

            if f(nx, ny, visited | nm, s + ds):
                return True

        return False


    for sx in range(w):
        stop = False
        for sy in range(h):
            stop = f(sx, sy, 0, "")
            if stop:
                break
        if stop:
            break
