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
    n = readint()
    h = readints()
    # index (bottom, top)
    m = [readints() for _ in range(n)]

    # print("h", h)
    # print("m", m)

    min_h = math.inf

    cache = {}


    def recurse(left: List, curr_h, curr_top, other_h, sl, sr):
        # print(left)
        global min_h

        used_h = max(curr_h, other_h if other_h is not None else 0)
        cache_key = (other_h is not None, tuple(left))
        if cache_key in cache:
            if cache[cache_key] < used_h:
                return

        if not left:
            # print(f"done {curr_h} {other_h}, {used_h} {sl} {sr}")
            min_h = min(min_h, used_h)
            assert set(sl + sr) == set(range(1, n+1))
        # if used_h > min_h:
        #     return

        for i, next in enumerate(left):
            # print(f"put {next} on {curr_top}")
            sl.append(next)
            del left[i]
            # left.remove(next)
            if curr_top is None:
                next_h = curr_h + h[next - 1]
            else:
                next_h =  curr_h + m[curr_top - 1][next - 1]

            recurse(left, next_h, next, other_h, sl, sr)

            # print("back")
            # left.add(next)
            left.insert(i, next)
            sl.pop()

        if other_h is None:
            # print(f"start second {left}")
            recurse(left, 0, None, curr_h, [], sl)

        cache[cache_key] = min_h

    recurse(list(range(1, n+1)), 0, None, None, [], [])
    print(case + 1, min_h)
