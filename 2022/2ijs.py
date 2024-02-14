import sys
from functools import cache

from oplossing.lib import ints_line, readline

with open("../../opgaves/2022/cat4/ijsjes/wedstrijd.invoer") as f:
    cases = int(f.readline().strip())

    for case in range(cases):
        # parse
        s, k = ints_line(f)

        streets = []

        adj = {}
        total_to_cover = 0

        for si in range(s):
            start, end, dist, cover = ints_line(f)
            streets.append((start, end, dist, cover == 1))

            total_to_cover += cover == 1

            adj.setdefault(start, {})[end] = (si, dist)
            adj.setdefault(end, {})[start] = (si, dist)

        depot = int(readline(f))

        # print(streets, depot, total_to_cover)

        own_cover_count = 0
        visit_counts = [0] * len(streets)

        cache = {}

        def bruteforce(curr):
            global own_cover_count
            # print(f"curr={case}, visit_counts={visit_counts}, cover_count={own_cover_count}")

            key = (own_cover_count, curr, tuple(visit_counts))
            if key in cache:
                return cache[key]

            if own_cover_count == total_to_cover and curr == depot:
                # print("Finished")
                return 0

            best = None

            for next, (si, dist) in adj[curr].items():
                # print(f"Trying {si} to {next}, cost {dist}")
                if visit_counts[si] > 1:
                    continue

                if streets[si][3] and visit_counts[si] == 0:
                    own_cover_count += 1
                visit_counts[si] += 1

                next_cost = bruteforce(next)
                if next_cost is not None:
                    next_cost += dist
                    if best is None or next_cost < best:
                        best = next_cost

                visit_counts[si] -= 1
                if streets[si][3] and visit_counts[si] == 0:
                    own_cover_count -= 1

            cache[key] = best
            return best


        # TODO output
        print(case + 1, bruteforce(depot))
        # sys.exit(0)
