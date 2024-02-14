def neighbors(grid, y, x):
    result = []
    for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if 0 <= ny < h and 0 <= nx < w:
            result.append(grid[y][x])
    return result


with open("../../opgaves/2023/cat4/flow/wedstrijd.invoer") as f:
    def readline():
        return f.readline().strip()


    cases = int(readline())

    for case in range(cases):
        h, w = readline().split(" ")
        h, w = int(h), int(w)

        grid = []
        for y in range(h):
            line = readline().split(" ")
            assert len(line) == w
            grid.append([int(x) for x in line])

        colors = list(set(x for line in grid for x in line))
        touching = {c: set() for c in colors}

        for y in range(h):
            for x in range(w):
                curr_color = grid[y][x]
                other_colors = []
                for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                    if 0 <= ny < h and 0 <= nx < w:
                        # print(f"{ny}, {nx} cell {grid[ny][nx]}, neighbors: {neighbors(grid, ny, nx)}")
                        # if neighbors(grid, ny, nx).count(grid[ny][nx]) > 1:
                        other_colors.append(grid[ny][nx])

                if other_colors.count(curr_color) == 1:
                    continue

                if len([d for d in other_colors if d == curr_color]) > 2:
                    touching[curr_color].add(curr_color)

                for c in other_colors:
                    if c != curr_color:
                        touching[curr_color].add(c)
                        touching[c].add(curr_color)

        max_count = 0

        removal_disallowed = []
        for color in colors:
            disallowed = 0
            for other in touching[color]:
                other_i = colors.index(other)
                disallowed |= 1 << other_i
            removal_disallowed.append(disallowed)


        # TODO cache!
        cache = {}
        def recurse(i: int, allowed_to_remove: int, removed: int):
            key = (i, allowed_to_remove >> i, removed)
            if key in cache:
                return cache[key]

            if allowed_to_remove >> i == 0:
                return removed

            max_removed = 0
            if (allowed_to_remove >> i) & 1:
                max_removed = max(max_removed,
                                  recurse(i + 1, allowed_to_remove & ~removal_disallowed[i], removed + 1))

            max_removed = max(max_removed, recurse(i + 1, allowed_to_remove, removed))
            cache[key] = max_removed
            return max_removed


        print(case + 1, recurse(0, (1 << len(colors)) - 1, 0))

        # for mask_remove in range(2 ** len(colors)):
        #     if mask_remove.bit_count() <= max_count:
        #         continue
        #
        #     for i, dis in enumerate(removal_disallowed):
        #         if ((mask_remove >> i) & 1) and (mask_remove & dis):
        #             break
        #     else:
        #         # print(f"  new max: {max_count}")
        #         max_count = max(max_count, mask_remove.bit_count())

        # print(h, w)
        # print(grid)
        # print(colors)
        # print(touching)
        # print(removal_disallowed)
        # print(max_count)
        # print(case + 1, max_count)

        # print()
        # print()
