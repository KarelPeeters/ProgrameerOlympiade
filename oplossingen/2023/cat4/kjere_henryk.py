from collections import defaultdict
import time
from oplossingen.dijkstra import dijkstra

def readline():
    return input().strip()


start = time.perf_counter()

cases = int(readline())
for case in range(cases):
    # load input
    values = readline().split(" ")
    assert len(values) % 2 == 0
    steps = list(zip(values[::2], values[1::2]))

    path = []
    loop_count = 0

    cdist = 0
    cx, cy = 0, 0
    connections = defaultdict(list)
    for n, dir in steps:
        for _ in range(int(n)):
            nx, ny = cx, cy
            if dir == "O":
                nx += 1
            elif dir == "W":
                nx -= 1
            elif dir == "N":
                ny += 1
            elif dir == "Z":
                ny -= 1

            connections[(min(cx, nx), min(cy, ny))].append((max(cx, nx), max(cy, ny)))
            connections[(max(cx, nx), max(cy, ny))].append((min(cx, nx), min(cy, ny)))
            cx, cy = nx, ny


    def call_next(node):
        if node == (0, 0):
            return True, []

        result = []
        for neighbor in connections[node]:
            result.append((neighbor, 1))
        return False, result


    result = dijkstra([(cx, cy)], call_next)
    assert result.found
    print(case + 1, result.dist)
