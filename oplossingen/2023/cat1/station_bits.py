from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    users = [0] * 1000

    # print("collecting")
    for _ in range(int(readline())):
        person, start, end = readints()

        limit = max(start, end)
        if limit >= len(users):
            users += [0] * (limit - len(users) + 1)

        mask = 1 << person
        users[start] |= mask
        users[end] |= mask

    # print(uses)
    # print("sorting")
    output = [(-persons.bit_count(), s) for s, persons in enumerate(users) if persons != 0]
    output.sort()

    # print("output")
    print(f"{case+1}", " ".join(f"{s}({-c})" for c, s in output))
