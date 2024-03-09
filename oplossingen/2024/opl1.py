from typing import List


def readline(f=None) -> str:
    if f is None:
        return input().strip()
    else:
        return f.readline().strip()


def readint(f=None) -> int:
    return int(readline(f))


def readints(f=None) -> List[int]:
    line = readline(f)
    if not line:
        return []
    return [int(x) for x in line.split(" ")]


def ortho_neighbors(h, w, y, x):
    mid = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    return [(ny, nx) for ny, nx in mid if 0 <= ny < h and 0 <= nx < w]


cases = readint()

for case in range(cases):
    total_a, total_b, n_orders = readints()

    orders_input = []
    for _ in range(n_orders):
        a, b = readints()
        orders_input.append((a, b))

    orders = []
    remaining = orders_input

    while remaining:
        new_remaining = []

        for test_a, test_b in remaining:
            # Test if this value is dominated
            dominated = False
            for rem_a, rem_b in remaining:
                if rem_a < test_a and rem_b <= test_b:
                    dominated = True
                    break
                if rem_a <= test_a and rem_b < test_b:
                    dominated = True
                    break

            # Add to correct list
            if dominated:
                new_remaining.append((test_a, test_b))
            else:
                orders.append((test_a, test_b))

        remaining = new_remaining


    #best_cache = [[] for _ in range(n_orders + 1)]

    cache_a = {}
    cache_b = {}
    best = 0

    def dfs(c_idx, c_a, c_b, c_cnt):
        global cache_a, cache_b

        if c_a > total_a:
            return 0
        if c_b > total_b:
            return 0

        if c_idx == n_orders:
            return c_cnt

        # cache a
        cache_has_better = False
        for cache_val_a in range(0, c_a + 1):
            cache_key_a = (c_cnt, cache_val_a)
            if cache_key_a in cache_a:
                cache_val_b = cache_a[cache_key_a]
                if cache_key_a == c_a:
                    if cache_val_b < c_b:
                        cache_has_better = True
                        #print(f"current value {c_a}, {c_b}")
                        #print(f"Found value {cache_key_a}  in cache {cache_val_a} , {cache_val_b}")
                else:
                    if cache_val_b <= c_b:
                        cache_has_better = True
                        #print(f"current value {c_a}, {c_b}")
                        #print(f"Found value {cache_key_a}  in cache {cache_val_a} , {cache_val_b}")
        for cache_val_b in range(0, c_b + 1):
            cache_key_b = (c_cnt, cache_val_b)
            if cache_key_b in cache_b:
                cache_val_a = cache_b[cache_key_b]
                if cache_key_b == c_b:
                    if cache_val_a < c_a:
                        cache_has_better = True
                        #print(f"current value {c_a}, {c_b}")
                        #print(f"Found value {cache_key_b} in cache {cache_val_a} , {cache_val_b}")
                else:
                    if cache_val_a <= c_a:
                        cache_has_better = True
                        #print(f"current value {c_a}, {c_b}")
                        #print(f"Found value {cache_key_b} in cache {cache_val_a} , {cache_val_b}")

        cache_a[(c_cnt, c_a)] = c_b
        cache_a[(c_cnt, c_b)] = c_a
        #print(f"{c_cnt}, {c_a}, {c_b}")

        new_idx = c_idx + 1
        best_left = dfs(new_idx, c_a, c_b, c_cnt) # dont take

        order_a, order_b = orders[c_idx]
        new_a = c_a + order_a
        new_b = c_b + order_b
        best_right = 0
        #print(f"bestleft = {best_left}")
        if not cache_has_better:
            best_right = dfs(new_idx, new_a, new_b, c_cnt + 1) # take

        #print(f"bestleft22 = {best_left}")
        result = max(best_right, best_left)
        #best[c_idx+1] = result
        #best[min(c_idx+2, len(best)-1)] = result
        return result

    best = dfs(0, 0,0, 0)
    print(case + 1, best)
