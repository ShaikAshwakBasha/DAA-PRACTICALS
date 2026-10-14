# Practical 9: Prim's Minimum Spanning Tree (adjacency matrix)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]
n = len(graph)
visited = {0}
tree = []
total = 0
print("PRIM'S ALGORITHM - STEP-BY-STEP MST")
print("Start at vertex 0; visited = [0]")
for step in range(1, n):
    candidates = sorted((graph[u][v], u, v)
                        for u in visited for v in range(n)
                        if v not in visited and graph[u][v] > 0)
    if not candidates:
        raise ValueError("Graph is disconnected; no spanning tree exists")
    w, u, v = candidates[0]
    visited.add(v)
    tree.append((u, v, w))
    total += w
    print(f"Step {step}: choose {u}-{v} (weight {w}), minimum crossing edge")
    print(f"        Visited vertices: {sorted(visited)}; running cost: {total}")
print("Selected MST edges:")
for u, v, w in tree:
    print(f"  {u} - {v} : {w}")
print(f"MST cost = {total}")
