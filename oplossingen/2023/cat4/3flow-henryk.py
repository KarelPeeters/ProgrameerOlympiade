from functools import cache


def readline() -> str:
    return input().strip()


def neighbors(grid, y, x):
    result = []
    for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if 0 <= ny < HEIGHT and 0 <= nx < WIDTH:
            result.append(grid[y][x])
    return result


cases = int(readline())

for case in range(cases):
    HEIGHT, WIDTH = readline().split(" ")
    HEIGHT, WIDTH = int(HEIGHT), int(WIDTH)

    grid = []
    for y in range(HEIGHT):
        line = readline().split(" ")
        assert len(line) == WIDTH
        grid.append([int(x) for x in line])

    colors = list(set(x for line in grid for x in line))

    # Collect touching
    touching = {c: set() for c in colors}
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = grid[y][x]
            same_neighbors = 0
            neighbors = []

            # Create neighbor list
            for n_y, n_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if 0 <= n_y < HEIGHT and 0 <= n_x < WIDTH:
                    n_color = grid[n_y][n_x]
                    if n_color == color:
                        same_neighbors += 1
                    else:
                        neighbors.append(n_color)

            # Add touching if not edge
            if same_neighbors > 1:
                touching[color].update(neighbors)
                for n_color in neighbors:
                    touching[n_color].add(color)

    #print(touching)
    max_set = 0

    def dfs(curr_list, i):
        global max_set
        # Exit condition
        if i == len(colors):
            max_set = max(max_set, len(curr_list))
            return

        # We will choose if colors[i] will be added
        n_color = colors[i]
        n_touching = touching[n_color]

        # 1. Check if colors[i] can be added
        can_be_added = True
        for exist_color in curr_list:
            illegal = exist_color in n_touching
            can_be_added = can_be_added and not illegal

        # 2. WE MUST GO DEEPER
        if can_be_added:
            # Could choose whether to add or not
            dfs(curr_list, i + 1)  # don't add
            curr_list.append(n_color)
            dfs(curr_list, i + 1)  # add
            curr_list.pop()
        else:
            # Not compatible, adding not allowed
            dfs(curr_list, i + 1)  # don't add

    dfs([], 0)
    print(case + 1, max_set)


