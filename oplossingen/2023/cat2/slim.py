from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    # parse
    prices = readints()

    tasks = []

    total_cost = 0

    for _ in range(int(readline())):
        usage, length = readints()
        tasks.append((usage, length))

        best_cost = None

        for start_h in range(24):
            starts = [start_h * 60]
            rem = length % 60
            if rem:
                starts.append(start_h * 60 + 60 - rem)

            for start in starts:
                if start + length - 1 >= 24 * 60:
                    continue

                # print(f"Starting {usage} {length} at {start}")

                curr_cost = 0
                curr_time = start
                curr_length = length

                while curr_length > 0:
                    curr_length -= 1
                    curr_cost += prices[curr_time//60] * usage
                    curr_time += 1

                # print(f"  => cost: {curr_cost}")

                if best_cost is None or curr_cost < best_cost:
                    best_cost = curr_cost

        # print(f"best_cost: {best_cost}")
        total_cost += best_cost

    # print(prices)
    # print(tasks)
    # print()

    print(f"{case + 1} {total_cost}")

    # calc
