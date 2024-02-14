from collections import Counter

from oplossing.lib import readline, ints_line, ortho_neighbors

with open("../../opgaves/2023/cat4/haven/wedstrijd.invoer") as f:
    cases = int(readline(f))
    for case in range(cases):
        # load input
        w, h = ints_line(f)

        grid_start = []
        boat = None
        for y in range(h):
            line = readline(f)
            grid_start.append(line)
            if "*" in line:
                boat = (y, line.index("*"))
        assert boat is not None
        grid_goal = []
        for y in range(h):
            line = readline(f)
            grid_goal.append(line)

        # find reachable sea and swaps
        reachable = set()
        todo = {boat}
        swaps = []
        while todo:
            cy, cx = todo.pop()
            if (cy, cx) in reachable:
                continue

            reachable.add((cy, cx))
            if 1 <= cy < h - 1:
                if grid_start[cy - 1][cx].isalpha() and grid_start[cy + 1][cx].isalpha():
                    swaps.append(((cy - 1, cx), (cy + 1, cx)))
            if 1 <= cx < w - 1:
                if grid_start[cy][cx - 1].isalpha() and grid_start[cy][cx + 1].isalpha():
                    swaps.append(((cy, cx - 1), (cy, cx + 1)))

            for ny, nx in ortho_neighbors(h, w, cy, cx):
                if grid_start[ny][nx] == ".":
                    # print(f"adding {(ny, nx)} from {(cy, cx)}")
                    todo.add((ny, nx))

        # connected swap groups
        # TODO make lib function from this
        swap_dict = {(y, x): set() for y in range(h) for x in range(w) if grid_start[y][x].isalpha()}
        for a, b in swaps:
            swap_dict[a].add(b)
            swap_dict[b].add(a)

        todo_ungrouped = set(swap_dict.keys())
        total_wrong = 0

        while todo_ungrouped:
            start = todo_ungrouped.pop()
            todo_group = {start}
            group_start_counts = Counter()
            group_goal_counts = Counter()

            while todo_group:
                curr = todo_group.pop()
                # print(f"visiting {curr}")

                group_start_counts[grid_start[curr[0]][curr[1]]] += 1
                group_goal_counts[grid_goal[curr[0]][curr[1]]] += 1

                for next in swap_dict[curr]:
                    if next in todo_ungrouped:
                        todo_ungrouped.remove(next)
                        todo_group.add(next)

            # print(f"Group start {start}, start counts {group_start_counts}, goal counts {group_goal_counts}")

            for key, count in group_goal_counts.items():
                total_wrong += max(0, count - group_start_counts[key])

        # print(grid_start)
        # print(grid_goal)
        # print(boat)
        # print(reachable)
        # print(swaps)
        print(case + 1, total_wrong)
        # print("\n\n")

        # collect swaps, put containers into groups
