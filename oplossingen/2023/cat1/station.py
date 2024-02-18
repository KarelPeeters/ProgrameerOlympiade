# no lib usage, functions calls are too slow!
cases = int(input().strip())

for case in range(cases):
    users = {}

    for _ in range(int(input().strip())):
        person, start, end = input().strip().split(" ")
        person = int(person)
        users.setdefault(int(start), set()).add(person)
        users.setdefault(int(end), set()).add(person)

    output = [(-len(persons), s) for s, persons in users.items()]
    output.sort()

    print(f"{case + 1}", " ".join(f"{s}({-c})" for c, s in output))
