from oplossingen.dijkstra import dijkstra
from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    # input
    count_lines = int(readline())
    lines = []

    for _ in range(count_lines):
        _, *stations = readints()
        lines.append(stations)

    count_trips = int(readline())
    trips = []
    for _ in range(count_trips):
        start, end = readints()
        trips.append((start, end))

    # convert
    station_to_lines = {}
    for line, st in enumerate(lines):
        for station in st:
            station_to_lines.setdefault(station, set()).add(line)

    # solve
    for start, end in trips:
        def call_next(st):
            if st == end:
                return True, []

            result = []
            for line in station_to_lines[st]:
                for other in lines[line]:
                    result.append((other, 1))
            return False, result


        result = dijkstra([start], call_next)
        if result.found:
            print(case+1, f"{result.dist}")
        else:
            print(case+1, "ONMOGELIJK")
