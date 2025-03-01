import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def welsh_powell_coloring(graph):
    # Bước 1: Sắp xếp đỉnh theo bậc giảm dần
    sorted_nodes = sorted(graph, key=lambda x: len(graph[x]), reverse=True)

    # Bước 2: Khởi tạo màu cho các đỉnh (-1 nghĩa là chưa tô màu)
    colors = {node: -1 for node in graph}
    color_count = 0

    # Bước 3: Duyệt từng đỉnh theo thứ tự đã sắp xếp
    for node in sorted_nodes:
        if colors[node] == -1:  # Nếu đỉnh chưa tô màu
            color_count += 1  # Tăng số màu
            colors[node] = color_count  # Gán màu mới

            # Tô màu cho các đỉnh chưa tô màu mà không kề với đỉnh đã tô màu hiện tại
            for other_node in sorted_nodes:
                if colors[other_node] == -1:  # Đỉnh chưa tô màu
                    if all(colors[neighbor] != color_count for neighbor in graph[other_node]):
                        colors[other_node] = color_count  # Gán màu hiện tại

    return colors

# Định nghĩa đồ thị
graph = {
    1: [2,3,4],  2: [1,5,9],  3: [1,7,8],  4: [1,6,10],
    5: [2,6,8],  6: [4,5,7],  7: [3,6,9],  8: [3,5,10],
    9: [2,7,10], 10: [4,8,9]
}

graph_coloring = welsh_powell_coloring(graph)

# Tạo đồ thị với NetworkX
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Danh sách màu sắc từ Matplotlib
colors_list = list(mcolors.TABLEAU_COLORS.values()) + list(mcolors.CSS4_COLORS.values())
node_colors = [colors_list[(graph_coloring[node] - 1) % len(colors_list)] for node in G.nodes()]

# Vẽ đồ thị với layout đẹp
plt.figure(figsize=(8, 8))
pos = nx.kamada_kawai_layout(G)  # Bố cục tối ưu khoảng cách
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray',
        node_size=1200, font_size=14, font_weight='bold', alpha=0.9, linewidths=2)

plt.title("Tô màu đồ thị theo thuật toán Welsh-Powell", fontsize=16, fontweight="bold")
plt.show()
