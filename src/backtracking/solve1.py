import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import time

def tao_do_thi(n, edge_prob=0.0):
    graph = {i: [] for i in range(1, n + 1)}
    if edge_prob == 0.0:
        return graph
    if edge_prob == 1.0:
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                graph[i].append(j)
                graph[j].append(i)
        return graph
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if random.random() < edge_prob:
                graph[i].append(j)
                graph[j].append(i)
    return graph
def co_an_toan(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True
def giai_bai_toan_to_mau(node, graph, colors, m):
    if node not in graph:
        return True
    for color in range(1, m + 1):
        if co_an_toan(node, color, graph, colors):
            colors[node] = color
            next_node = next((n for n in graph if colors[n] == -1), None)
            if next_node is None or giai_bai_toan_to_mau(next_node, graph, colors, m):
                return True
            colors[node] = -1
    return False
def to_mau_do_thi_backtracking(graph):
    start_time = time.time()
    colors = {node: -1 for node in graph}
    m = 1  #
    while True:
        if giai_bai_toan_to_mau(next(iter(graph)), graph, colors, m):
            end_time = time.time()
            execution_time = end_time - start_time
            return colors, m, execution_time
        m += 1

n = 30
edge_prob = 0.4  # Thử với 0.0, 0.5, hoặc 1.0
graph = tao_do_thi(n, edge_prob)

graph_coloring, num_colors, exec_time = to_mau_do_thi_backtracking(graph)

print(f"Số màu được sử dụng: {num_colors}")
print(f"Thời gian thực thi thuật toán: {exec_time:.6f} giây")

print("\nDanh sách kề của đồ thị:")
for node, neighbors in graph.items():
    print(f"Đỉnh {node}: {sorted(neighbors)}")
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)
colors_list = list(mcolors.TABLEAU_COLORS.values()) + list(mcolors.CSS4_COLORS.values())
node_colors = [colors_list[(graph_coloring[node] - 1) % len(colors_list)] for node in G.nodes()]
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray',
        node_size=800, font_size=12, font_weight='bold', alpha=0.9, linewidths=1.5)
plt.title(f"Tô màu đồ thị với edge_prob = {edge_prob}", fontsize=14, fontweight="bold")
plt.show()
