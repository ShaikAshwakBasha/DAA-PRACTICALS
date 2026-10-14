# Practical 11: Floyd-Warshall all-pairs shortest paths
INF = float('inf')
d = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0],
]
n = len(d)
def show(matrix):
    for row in matrix:
        print("  " + " ".join(f"{x:>3}" if x != INF else "INF"
                            for x in row))
print("FLOYD-WARSHALL - STEP-BY-STEP DISTANCE UPDATES")
print("Initial distance matrix:")
show(d)
for k in range(n):
    print(f"Intermediate vertex k = {k}:")
    changes = []
    for i in range(n):
        for j in range(n):
            if d[i][k] != INF and d[k][j] != INF:
                alt = d[i][k] + d[k][j]
                if alt < d[i][j]:
                    old = "INF" if d[i][j] == INF else str(d[i][j])
                    changes.append(f"  d[{i}][{j}]: {old} -> {alt} via {k}")
                    d[i][j] = alt
    if changes:
        print("\n".join(changes))
    else:
        print("  No distances improved")
    show(d)
if any(d[i][i] < 0 for i in range(n)):
    raise ValueError("Negative cycle detected")
print("Final shortest-path distance matrix:")
show(d)
