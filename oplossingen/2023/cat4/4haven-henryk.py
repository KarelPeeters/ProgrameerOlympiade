from collections import Counter
from typing import List
from oplossingen.unionfind import UnionFind


def readline() -> str:
    return input().strip()

def readints() -> List[int]:
    line = readline()
    if not line:
        return []
    return [int(x) for x in line.split(" ")]


def ortho_neighbors(h, w, y, x):
    mid = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    return [(ny, nx) for ny, nx in mid if 0 <= ny < h and 0 <= nx < w]


cases = int(readline())
for case in range(cases):
    # load input
    w, h = readints()

    grid_start = []
    boat = None
    for y in range(h):
        line = readline()
        grid_start.append(line)
        if "*" in line:
            boat = (y, line.index("*"))
    assert boat is not None
    grid_goal = []
    for y in range(h):
        line = readline()
        grid_goal.append(line)

    # find reachable sea and swaps
    reachable = set()
    todo = {boat}
    swappable_unions = UnionFind()
    while todo:
        cy, cx = todo.pop()
        if (cy, cx) in reachable:
            continue

        reachable.add((cy, cx))
        if 1 <= cy < h - 1:
            if grid_start[cy - 1][cx].isalpha() and grid_start[cy + 1][cx].isalpha():
                swappable_unions.union((cy - 1, cx), (cy + 1, cx))
        if 1 <= cx < w - 1:
            if grid_start[cy][cx - 1].isalpha() and grid_start[cy][cx + 1].isalpha():
                swappable_unions.union((cy, cx - 1), (cy, cx + 1))

        for ny, nx in ortho_neighbors(h, w, cy, cx):
            if grid_start[ny][nx] == ".":
                # print(f"adding {(ny, nx)} from {(cy, cx)}")
                todo.add((ny, nx))

    total_wrong = 0

    # Count swappable wrongs
    groups = swappable_unions.get_all_unions()
    for group in groups:
        group_start_counts = Counter()
        group_goal_counts = Counter()

        for node in group:
            group_start_counts[grid_start[node[0]][node[1]]] += 1
            group_goal_counts[grid_goal[node[0]][node[1]]] += 1

        for key, count in group_goal_counts.items():
            total_wrong += max(0, count - group_start_counts[key])

    # Count not swappable wrongs
    for y in range(h):
        for x in range(w):
            # Swappable, already counted
            if swappable_unions.does_union_contain((y, x)):
                continue

            tile_real = grid_start[y][x]
            if not tile_real.isalpha():
                continue # Skip sea / boat

            # Not correct
            tile_goal = grid_goal[y][x]
            if tile_real != tile_goal:
                total_wrong += 1

    # Output
    print(case + 1, total_wrong)
