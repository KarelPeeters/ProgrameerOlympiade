# find best
# best_dist = -1
# best_index = None
# for index, (node, dist) in enumerate(todo):
#     if best_index is None or dist < best_dist:
#         best_index = index
#         best_dist = dist
# assert best_index is not None
# del todo[best_index]


def dijkstra(graph, starts, ends):
    """
    graph: dict of node -> (neighbor, distance)
    starts: set of start nodes, all assumed with cost 0
    ends: set of end nodes

    returns: (distance, path including start and end)
    """

    import heapq

    # priority queue of (dist, node, parent)
    todo = [(0, start, None) for start in starts]
    heapq.heapify(todo)

    # node -> best parent
    visited = {}

    while todo:
        dist, node, parent = heapq.heappop(todo)
        # print(f"popped {dist, node, parent}")
        if node in visited:
            continue
        visited[node] = parent

        if node in ends:
            # print(f"end node {node}")
            path = []
            curr = node
            while curr is not None:
                path.append(curr)
                curr = visited[curr]
            path.reverse()
            return dist, path

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(todo, (dist + weight, neighbor, node))

    # TODO return all distances instead?
    return None


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
    lines_set = set()
    cx, cy = 0, 0
    for n, r in steps:
        n = int(n)
        sign, hor = dirs[r]

        nx = cx + n * sign * hor
        ny = cy + n * sign * (1 - hor)

        # print(nx, ny)
        line = (min(cx, nx), min(cy, ny), n, hor)

        if line not in lines_set:
            lines.append(line)
            lines_set.add(line)
            line_to_nodes.append({(cx, cy), (nx, ny)})

        cx = nx
        cy = ny

    # print(nodes_on_line)
    # collect crossings
    # print("start simple")
    for ai, (ax, ay, an, a_hor) in enumerate(lines):
        for node in [(0, 0), (cx, cy)]:
            if ax <= node[0] <= ax + an * a_hor and ay <= node[1] <= ay + an * (1 - a_hor):
                line_to_nodes[ai].add(node)

    #     print("start pair crossings")
    #     print(len(lines))
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

    # print("start node to lines")
    node_to_lines = {n: set() for line in line_to_nodes for n in line}
    for line, nodes in enumerate(line_to_nodes):
        for node in nodes:
            node_to_lines[node].add(line)

    #     print("start dijkstra")

    # covert to cleaner graph
    node_to_nodes = {}
    for node in node_to_lines:
        for line in node_to_lines[node]:
            for next_node in line_to_nodes[line]:
                ds = [abs(node[i] - next_node[i]) for i in range(2)]
                assert max(ds) == sum(ds), ds
                node_to_nodes.setdefault(node, []).append((next_node, max(ds)))

    # call out to dijkstra
    dist, _ = dijkstra(node_to_nodes, {(0, 0)}, {(cx, cy)})
    #
    # best_dist_to = {(0, 0): 0}
    # todo = queue.PriorityQueue()
    # todo.put((0, (0, 0)))
    #
    # while todo.qsize():
    #     curr_dist, curr_node = todo.get()
    #     if best_dist_to[curr_node] < curr_dist:
    #         continue
    #
    #     # find children
    #     for line in node_to_lines[curr_node]:
    #         for next_node in line_to_nodes[line]:
    #             ds = [abs(curr_node[i] - next_node[i]) for i in range(2)]
    #             assert max(ds) == sum(ds), ds
    #             next_dist = curr_dist + max(ds)
    #
    #             if next_node not in best_dist_to or next_dist < best_dist_to[next_node]:
    #                 best_dist_to[next_node] = next_dist
    #                 todo.put((next_dist, next_node))

    # print(lines)
    # print(nodes)
    # print(line_to_nodes)
    # print(node_to_lines)
    # print(best_dist_to)

    print(case + 1, dist)
