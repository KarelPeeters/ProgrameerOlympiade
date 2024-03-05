from collections import defaultdict


def readline() -> str:
    return input().strip()


cases = int(readline())

for case in range(cases):
    indeg = defaultdict(int)
    edges = defaultdict(set)

    edge_count = int(readline())
    for _ in range(edge_count):
        src, dest = readline().split(" ")
        src, dest = int(src) - 1, int(dest) - 1  # Make 0 indexed
        edges[src].add(dest)
        indeg[dest] += 1
        edges[dest].add(src)
        indeg[src] += 1

    # Identify leaves
    leaves = []
    for i in range(len(indeg)):
        if indeg[i] == 1:
            leaves.append(i)

    # Remove leaves
    output = []
    dead_nodes = set()
    while leaves:
        dest = leaves.pop()
        dead_nodes.add(dest)  # Never visit again
        for src in edges[dest]:
            # Don't start from dead
            if src in dead_nodes:
                continue

            #print(f"Eliminating {src + 1} -> {dest + 1}")
            indeg[src] -= 1  # Source won't be visited by dead node anymore
            output.append((src + 1, dest + 1))
            if indeg[src] == 1:
                leaves.append(src)

    if len(dead_nodes) == len(edges):
        output_reverse = []
        for edge_src, edge_dest in output:
            output_reverse.append((edge_dest, edge_src))
        output = output + output_reverse
    output.sort()

    if output:
        print(case + 1, " ".join(str(x).replace(" ", "") for x in output))
    else:
        print(case + 1, "geen")
