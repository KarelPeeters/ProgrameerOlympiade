import itertools
import math

from typing import List


def readline(f=None) -> str:
    if f is None:
        return input().strip()
    else:
        return f.readline().strip()


def readint(f=None) -> int:
    return int(readline(f))


def readints(f=None) -> List[int]:
    line = readline(f)
    if not line:
        return []
    return [int(x) for x in line.split(" ")]


def ortho_neighbors(h, w, y, x):
    mid = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    return [(ny, nx) for ny, nx in mid if 0 <= ny < h and 0 <= nx < w]


cases = readint()

for case in range(cases):
    try:
        n, *cards = readline().split()
        n  = int(n)

        cards = [(c[0], c[1]) for c in cards]
        suits =list( {c[0] for c in cards})
        # print(cards)

        illegal = [{"S", "K"}, {"H", "R"}]
        sort = [str(s) for s in range(1, 11)] + ["B", "D", "H", "A"]

        min_steps = math.inf

        for so in itertools.permutations(suits):
            if set(so) not in illegal:
                if any({a, b} in illegal for a, b in zip(so[1:], so[:-1])):
                    continue

            target = []
            for s in so:
                filtered = [c for c in cards if c[0] == s]
                filtered.sort(key=lambda c: sort.index(c[1]))
                target.extend(filtered)

            # print(cards)
            # print(target)

            current = list(cards)
            count = 0

            while True:
                worst_pair = None
                worst_dis = 0
                for i in range(len(current)):
                    j = target.index(current[i])
                    if abs(j-i) > worst_dis:
                        worst_dis = abs(j-i)
                        worst_pair = (i, j)
                if worst_dis == 0:
                    break

                (i, j) = worst_pair
                v = current[i]
                del current[i]
                if i < j:
                    j -= 1
                current.insert(j, v)
                count += 1
            # assert current == target

            if count < min_steps:
                min_steps = count
        print(case + 1, min_steps)
    except Exception as e:
        print(case + 1, 0)

