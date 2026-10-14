# Practical 12: Travelling Salesman using DP and bitmasking
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]
n = len(cost)
full = (1 << n) - 1
INF = float('inf')
dp = {(1, 0): 0}
predecessor = {}
print("TRAVELLING SALESMAN - BITMASK DP TRACE")
print("Start: mask=0001, city=0, cost=0")
for mask in range(1, full + 1):
    if not (mask & 1):
        continue
    for u in range(n):
        if (mask, u) not in dp:
            continue
        current = dp[(mask, u)]
        for v in range(1, n):
            if mask & (1 << v):
                continue
            new_mask = mask | (1 << v)
            candidate = current + cost[u][v]
            key = (new_mask, v)
            if candidate < dp.get(key, INF):
                dp[key] = candidate
                predecessor[key] = (mask, u)
                print(f"Update: {mask:04b} at {u} -> {new_mask:04b} at {v}; "
                      f"cost = {candidate}")
end = min(range(1, n), key=lambda v: dp[(full, v)] + cost[v][0])
best = dp[(full, end)] + cost[end][0]
route = []
state = (full, end)
while state != (1, 0):
    route.append(state[1])
    state = predecessor[state]
route = [0] + list(reversed(route)) + [0]
print(f"Return from city {end} to 0: +{cost[end][0]}")
print("Optimal tour:", " -> ".join(map(str, route)))
print("Minimum tour cost =", best)
