# find best
# best_dist = -1
# best_index = None
# for index, (node, dist) in enumerate(todo):
#     if best_index is None or dist < best_dist:
#         best_index = index
#         best_dist = dist
# assert best_index is not None
# del todo[best_index]

def readline():
    return input().strip()


cases = int(readline())
for case in range(cases):
    # load input
    values = readline().split(" ")
    assert len(values) % 2 == 0
    steps = list(zip(values[::2], values[1::2]))

    # print(steps)

    # walk forward
    dirs = {
        "O": (1, True),
        "W": (-1, True),
        "N": (1, False),
        "Z": (-1, False),
    }

    # collect lines
    line_to_nodes = []

    # (sx, sy, n, hor)
    lines = []
    cx, cy = 0, 0
    for n, r in steps:
        n = int(n)
        sign, hor = dirs[r]

        nx = cx + n * sign * hor
        ny = cy + n * sign * (1 - hor)

        # print(nx, ny)
        lines.append((min(cx, nx), min(cy, ny), n, hor))
        line_to_nodes.append({(cx, cy), (nx, ny)})

        cx = nx
        cy = ny

    # print(nodes_on_line)
    # collect crossings
    for ai, (ax, ay, an, a_hor) in enumerate(lines):
        for node in [(0, 0), (cx, cy)]:
            if ax <= node[0] <= ax + an * a_hor and ay <= node[1] <= ay + an * (1 - a_hor):
                line_to_nodes[ai].add(node)

    for ai, (ax, ay, an, a_hor) in enumerate(lines):
        for bi, (bx, by, bn, b_hor) in enumerate(lines):
            if a_hor and not b_hor:
                if ax <= bx <= ax + an and by <= ay <= by + bn:
                    # print("a", ai, (ax, ay, an, a_hor), "b", bi, (bx, by, bn, b_hor), "node", node)
                    line_to_nodes[ai].add((bx, ay))
                    line_to_nodes[bi].add((bx, ay))

            if a_hor and b_hor and ay == by and ax <= bx <= ax + an:
                line_to_nodes[ai].add((bx, ay))
                line_to_nodes[bi].add((bx, ay))

            if not a_hor and not b_hor and ax == bx and ay <= by <= ay + an:
                line_to_nodes[ai].add((ax, ay))
                line_to_nodes[bi].add((ax, ay))

    node_to_lines = {n: set() for line in line_to_nodes for n in line}
    for line, nodes in enumerate(line_to_nodes):
        for node in nodes:
            node_to_lines[node].add(line)

    best_dist_to = {(0, 0): 0}
    todo = [(0, 0)]

    while len(todo):
        # curr_node = todo.pop()
        # curr_dist = best_dist_to[curr_node]

        # find best
        curr_index = None
        curr_dist = -1
        for index, node in enumerate(todo):
            dist = best_dist_to[node]
            if curr_index is None or dist < curr_dist:
                curr_index = index
                curr_dist = dist
        assert curr_index is not None
        curr_node = todo[curr_index]
        del todo[curr_index]

        # find children
        for line in node_to_lines[curr_node]:
            for next_node in line_to_nodes[line]:
                ds = [abs(curr_node[i] - next_node[i]) for i in range(2)]
                assert max(ds) == sum(ds), ds
                next_dist = curr_dist + max(ds)

                if next_node not in best_dist_to or next_dist < best_dist_to[next_node]:
                    best_dist_to[next_node] = next_dist
                    todo.append(next_node)

    # print(lines)
    # print(nodes)
    # print(line_to_nodes)
    # print(node_to_lines)
    # print(best_dist_to)

    print(case + 1, best_dist_to[(cx, cy)])
