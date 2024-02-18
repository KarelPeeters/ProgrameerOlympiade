import math

from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    h, b = readints()
    _ = int(readline())
    points = [p for p in readints()]

    dirs = set()
    visited = set()

    pr = None
    pc = None

    fail = False
    # print(f"points={points}")

    # check start and ends unique
    fail = fail or len(set(points[:-1])) != len(points) - 1
    fail = fail or len(set(points[1:])) != len(points) - 1

    for ci in points:
        if fail:
            break

        cr = (ci - 1) // b
        cc = (ci - 1) % b

        if pr is not None and pc is not None:
            # simplify
            t = cc - pc
            n = cr - pr
            g = math.gcd(t, n)
            # print(t, n, g)
            t = t // g
            n = n // g

            # check intermediate
            nr = pr
            nc = pc
            # print(f"moving from {pr, pc} to {cr, cc} with dir {n, t}")
            while True:
                nr += n
                nc += t
                if nr == cr and nc == cc:
                    break

                # print(f"  checking {nr, nc}")
                if (nr, nc) not in visited:
                    # print("    fail")
                    fail = True
                    break
            if fail:
                break

            # flip
            s = 1
            if n < 0:
                s = -1
            if n == 0 and t < 0:
                s = -1
            if t == 0 and n < 0:
                s = -1

            # count
            dir = (t * s, n * s)
            dirs.add(dir)

        # update
        visited.add((cr, cc))
        pr = cr
        pc = cc

        # print(cr, cc)

    # print(dirs)

    if fail:
        print(f"{case + 1} ongeldig patroon")
    else:
        complexity = len(points) - 1 + len(dirs)
        print(f"{case + 1} {complexity}")
