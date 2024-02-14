with open("../../opgaves/2022/cat4/homeswap/wedstrijd.invoer") as f:
    cases = int(f.readline().strip())

    for case in range(cases):
        # parse
        n = int(f.readline().strip())
        likes = {}
        for i in range(n):
            x, *y = f.readline().strip().split(" ")
            likes[x] = [x] + y


        # compute
        def find_max(to_place: list, free: set) -> int:
            if not to_place:
                return 0

            # TODO pick one with least options instead
            curr = to_place[0]
            to_place = to_place[1:]

            best = None

            for cand in likes[curr]:
                if cand in free:
                    # print(f"  moving {curr} to {cand}")
                    free.remove(cand)
                    next = find_max(to_place, free)
                    if next is not None:
                        next += (curr != cand)
                        if best is None or next > best:
                            best = next
                    free.add(cand)

            return best


        print(case + 1, find_max(list(likes), set(likes)))
