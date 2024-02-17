from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    points = readints()

    name_a, *places_a = readline().split(" ")
    name_b, *places_b = readline().split(" ")

    places_a = [int(p) - 1 for p in places_a]
    places_b = [int(p) - 1 for p in places_b]


    # print(f"places: {places_a}, {places_b}")

    def score(places, delta):
        score = 0
        for p in places:
            if p < len(points):
                add = points[p] + delta
                if add <= 0:
                    return None
                # print(f"adding {add} from index {p}")
                score += add
        return score


    def outcome(delta):
        score_a = score(places_a, delta)
        score_b = score(places_b, delta)

        if score_a is None or score_b is None:
            return None

        # print(f"scores: {score_a}, {score_b}")

        if score_a > score_b:
            return f"{name_a} wint"
        if score_a < score_b:
            return f"{name_b} wint"
        return "ex aequo"


    base = outcome(0)
    print(f"{case + 1} {base}")

    best = {base: 0}
    for delta in range(-max(points) * 2 - 1, max(points) * 2 + 2):
        new = outcome(delta)
        if new is not None:
            if new not in best or abs(delta) < abs(best[new]):
                best[new] = delta

    # print(f"{new} ")

    del best[base]

    best = [(v, k) for k, v in best.items()]
    best.sort()
    best.reverse()

    for k, v in best:
        print(f"{case + 1} {v} door verschuiving met {k}")
