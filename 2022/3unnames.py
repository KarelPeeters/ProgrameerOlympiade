from functools import cache

from oplossing.lib import *

with open("../../opgaves/2022/cat4/untitled4/wedstrijd.invoer") as f:
    cases = int(f.readline().strip())

    for case in range(cases):
        # parse
        n = int(readline(f))
        a = ints_line(f)
        assert len(a) == n

        # print(n, a)

        cache = {}


        # def eval(v, i):
        #     if i >= len(a):
        #         return 0
        #
        #     key = (v, i)
        #     if key in cache:
        #         return cache[key]
        #
        #     for j in reversed(range(i + 1, len(a))):
        #         eval(v, j)
        #
        #     result = (v < a[i]) + eval(v, i + 1)
        #     cache[key] = result
        #     return result

        result = []
        hist = []
        for i in reversed(range(len(a))):

            result.append(max((v for k, v in hist.items() if k < a[i]), default=0))

            hist.setdefault(a[i], 0)
            hist[a[i]] += 1


        # result = []
        # for i in range(len(a)):
        #     result.append(eval(a[i], i + 1))
        result.reverse()

        # TODO output
        print(" ".join(str(x) for x in [case + 1] + result))
        # sys.exit(0)
