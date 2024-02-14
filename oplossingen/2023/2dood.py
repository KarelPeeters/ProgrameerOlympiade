with open("../../opgaves/2023/cat4/doodlopend/wedstrijd.invoer") as f:
    def readline():
        return f.readline().strip()

    cases = int(readline())

    for case in range(cases):
        edge_count = int(readline())
        # node -> (node, live)
        live_from_to = {}

        for _ in range(edge_count):
            a, b = readline().split(" ")
            a, b = int(a), int(b)
            live_from_to.setdefault(a, {})[b] = True
            live_from_to.setdefault(b, {})[a] = True

        # init
        todo = set()
        for node in live_from_to:
            if len(live_from_to[node]) == 1:
                other, _ = next(iter(live_from_to[node].items()))
                live_from_to[other][node] = False
                todo.add(other)
                # print(f"init marking {other}->{node} as dead")

        # prove dead
        while len(todo):
            curr = todo.pop()
#             print(f"checking {curr}")

            for other in live_from_to[curr]:
                if not any(live for derp, live in live_from_to[curr].items() if other != derp):
                    if live_from_to[other][curr]:
                        live_from_to[other][curr] = False
                        todo.add(other)
#                         print(f"prove marking {other}->{curr} as dead")

        # collect output
        output = []
        for a in live_from_to:
            for b in live_from_to[a]:
                alive = live_from_to[a][b]
                if not alive:
                    output.append((a, b))
        output.sort()

        if output:
            print(case, " ".join(str(x) for x in output))
        else:
            print(case, "geen")


