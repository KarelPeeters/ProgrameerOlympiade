from functools import cache
from oplossingen.lib import readint, readints


cases = readint()

for case in range(cases):
    ma, mb, n = readints()
    pairs = [tuple(readints()) for _ in range(n)]

    best = 0

    @cache
    def solve(left: int, taken: int, ca: int, cb: int):
        global best
        assert ca <= ma and cb <= mb
        if left + taken < best:
            return
        if left == 0:
            best = max(best, taken)
            return

        solve(left - 1, taken, ca, cb)

        a, b = pairs[left - 1]
        if ca + a <= ma and cb + b <= mb:
            solve(left - 1, taken + 1, ca + a, cb + b)

    solve(len(pairs), 0, 0, 0)
    print(case + 1, best)
