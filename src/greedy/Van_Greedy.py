import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import time


def generate_connected_graph(n, edge_prob=0.2):
    graph = {i: [] for i in range(1, n + 1)}
    nodes = list(graph.keys())

    available_nodes = set(nodes)
    connected_nodes = {random.choice(nodes)}
    available_nodes.remove(next(iter(connected_nodes)))

    while available_nodes:
        new_node = available_nodes.pop()
        connect_to = random.choice(list(connected_nodes))
        graph[new_node].append(connect_to)
        graph[connect_to].append(new_node)
        connected_nodes.add(new_node)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if random.random() < edge_prob and j not in graph[i]:
                graph[i].append(j)
                graph[j].append(i)

    return graph


def welsh_powell_coloring(graph):
    start_time = time.time()
    sorted_nodes = sorted(graph, key=lambda x: len(graph[x]), reverse=True)
    colors = {node: -1 for node in graph}
    color_count = 0

    for node in sorted_nodes:
        if colors[node] == -1:
            color_count += 1
            colors[node] = color_count

            for other_node in sorted_nodes:
                if colors[other_node] == -1 and all(colors[neighbor] != color_count for neighbor in graph[other_node]):
                    colors[other_node] = color_count

    end_time = time.time()
    execution_time = end_time - start_time
    return colors, color_count, execution_time


# Tạo đồ thị liên thông với 50 đỉnh
graph = generate_connected_graph(20, edge_prob=0.1)
graph_coloring, num_colors, exec_time = welsh_powell_coloring(graph)

# In số màu và thời gian thực thi
print(f"Số màu được sử dụng: {num_colors}")
print(f"Thời gian thực thi thuật toán: {exec_time:.6f} giây")

# In danh sách kề của đồ thị
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

plt.title("Tô màu đồ thị với thuật toán Welsh-Powell", fontsize=14, fontweight="bold")
plt.show()
