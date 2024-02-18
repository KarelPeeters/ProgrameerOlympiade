from oplossingen.dijkstra import dijkstra
from oplossingen.lib import readline, readints, ortho_neighbors

cases = int(readline())

for case in range(cases):
    # parse
    h, w = readints()
    grid = []
    for _ in range(h):
        grid.append(list(readline()))

    # print(h, w)
    # print(grid)
    # for row in grid:
    #     print("".join(row))
    # print()

    for _ in range(int(readline())):
        r, c, dir = readline().split(" ")
        r = int(r) - 1
        c = int(c) - 1

        delta = 1 if dir == "+" else -1

        symbol = grid[r][c]
        # print(symbol, int(symbol, 16), f"{int(symbol, 16):x}")
        new_symbol = f"{min(15, max(0, int(symbol, 16) + delta)):x}".upper()


        def call_next(node):
            nr, nc = node
            others = [(n, 0) for n in ortho_neighbors(h, w, nr, nc) if grid[n[0]][n[1]] == symbol]
            return False, others


        result = dijkstra([(r, c)], call_next)
        assert not result.found

        for nr, nc in result.visited.keys():
            grid[nr][nc] = new_symbol

        # for row in grid:
        #     print("".join(row))
        # print()

    for row in grid:
        print(f"{case + 1}", "".join(row))

    # print()
