with open("../../opgaves/2023/cat4/aandelen/wedstrijd.invoer") as f:
    def readline():
        return f.readline().strip()


    cases = int(readline())

    for case in range(cases):
        start = int(readline())
        times = int(readline())
        values_str = readline()
        if not values_str:
            values = []
        else:
            values = [int(x) for x in values_str.split(" ")]

        curr = start
        for c, n in zip(values[:-1], values[1:]):
            if n > c:
                curr += (n - c) * (curr // c)
        print(curr)


