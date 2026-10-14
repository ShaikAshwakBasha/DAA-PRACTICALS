# Practical 10: Kruskal's Minimum Spanning Tree (DSU)
n = 5
edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3),
         (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
parent = list(range(n))
rank = [0] * n
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def unite(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1
    return True
print("KRUSKAL'S ALGORITHM - STEP-BY-STEP MST")
ordered = sorted(edges, key=lambda e: (e[2], e[0], e[1]))
print("Sorted edges (u, v, weight):", ordered)
tree = []
total = 0
for step, (u, v, w) in enumerate(ordered, 1):
    if unite(u, v):
        tree.append((u, v, w))
        total += w
        print(f"Step {step}: {u}-{v} weight {w}: ACCEPT (different components)")
        print(f"        MST edges = {len(tree)}; running cost = {total}")
    else:
        print(f"Step {step}: {u}-{v} weight {w}: REJECT (forms a cycle)")
    # Check all edges to demonstrate accept and reject decisions.
if len(tree) != n - 1:
    raise ValueError("Graph is disconnected")
print("Selected MST edges:")
for u, v, w in tree:
    print(f"  {u} - {v} : {w}")
print(f"MST cost = {total}")
