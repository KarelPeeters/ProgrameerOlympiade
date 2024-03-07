import itertools
import math
from oplossingen.lib import readint, readline


def inc_seq(x, key=lambda i: i, kp=None, len=0) -> int:
    if not x:
        return len
    c, *x = x

    kc = key(c)
    if kp is None:
        return inc_seq(x, key, kc, 1)
    assert isinstance(kp, tuple)

    if kc < kp:
        # either start new or skip
        return max(inc_seq(x, key, kc, 1), inc_seq(x, key, kp, len))
    else:
        # either continue or skip
        return max(inc_seq(x, key, kc, len + 1), inc_seq(x, key, kp, len))


cases = readint()
for case in range(cases):
    n, *cards = readline().split(" ")
    # print(cards)
    suits = {c[0] for c in cards}

    single = [{"S", "K"}, {"H", "R"}]
    order = [str(i) for i in range(10 + 1)] + ["B", "V", "H", "A"]

    best = math.inf

    for perm in itertools.permutations(list(suits)):
        if suits not in single and any(
            set(p) in single for p in zip(perm[1:], perm[:-1])
        ):
            continue

        target = sorted(cards, key=lambda c: (perm.index(c[0]), order.index(c[1])))
        curr = list(cards)

        # print(perm)
        # print(target)
        # print(curr)
        # print()

        inc = inc_seq(cards, key=lambda c: (perm.index(c[0]), order.index(c[1])))
        # print(inc)
        t = len(cards) - inc
        # print(t)
        best = min(best, t)

    # print()
    print(case + 1, best)
