from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    users = {}

    for _ in range(int(readline())):
        person, start, end = readints()
        users.setdefault(start, set()).add(person)
        users.setdefault(end, set()).add(person)

    output = [(-len(persons), s) for s, persons in users.items()]
    output.sort()

    print(f"{case+1}", " ".join(f"{s}({-c})" for c, s in output))
