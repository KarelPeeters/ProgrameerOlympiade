from typing import Tuple, Dict

from oplossingen.lib import readline, readints, readint

cases = int(readline())

for case in range(cases):
    # parse
    _ = readint()
    w = set(readints())
    k0, a1, a2, b1, b2 = readints()

    cache: Dict[Tuple[int, int], Tuple[int, set]] = {}
    max_w = max(w)


    def solve(k: int, a: bool, depth: int) -> Tuple[int, set]:
        global cache
        if k in w:
            return -1, {k}
        if k > max_w:
            return 0, set()

        key = (k, a)
        if key in cache:
            return cache[key]

        d1, d2 = (a1, a2) if a else (b1, b2)

        s1, f1 = solve(k + d1, not a, depth + 1)
        s2, f2 = solve(k + d2, not a, depth + 1)

        s1 = -s1
        s2 = -s2

        result = max(s1, s2)
        final = f1 if s1 > s2 else f2 if s2 > s1 else f1 | f2

        cache[key] = result, final
        # print(f"k={k}, a={a} -> {result}")
        return result, final


    solution, final = solve(k0, a=True, depth=0)
    same = sorted(set(final))
    same_str = " ".join(str(s) for s in same)

    # print(best_cache)

    if solution == 0:
        print(f"{case + 1} gelijk")
    elif solution == 1:
        print(f"{case + 1} win {same_str}")
    else:
        print(f"{case + 1} verlies {same_str}")

    # print(solution)
