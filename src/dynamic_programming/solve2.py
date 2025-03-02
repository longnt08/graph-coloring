import networkx as nx
import matplotlib.pyplot as plt

def solve(adj_matrix, n):
    color = [0] * (n + 1)  # 1-based index
    flag = [0] * ((n + 1) * (n + 1))  # 1-based index
    
    # Gan dinh dau tien mau 1
    color[1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or flag[i * (n + 1) + j]:
                continue
            
            # Neu hai dinh ke nhau
            if adj_matrix[i * (n + 1) + j] and not flag[i * (n + 1) + j]:
                color[j] = color[i] + 1
                flag[i * (n + 1) + j] = flag[j * (n + 1) + i] = 1
            
            # Neu hai dinh khong ke nhau
            if not adj_matrix[i * (n + 1) + j] and not flag[i * (n + 1) + j]:
                color[j] = color[i]
                flag[i * (n + 1) + j] = flag[j * (n + 1) + i] = 1
    
    return color

def input_matrix(n):
    adj_matrix = [0] * ((n + 1) * (n + 1))  # 1-based index
    print("\nNhap ma tran lien ke:")
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            adj_matrix[i * (n + 1) + j] = row[j - 1]
    return adj_matrix

def draw_graph(adj_matrix, n, colors):
    G = nx.Graph()
    
    for i in range(1, n + 1):
        G.add_node(i, color=colors[i])
        for j in range(1, n + 1):
            if adj_matrix[i * (n + 1) + j]:
                G.add_edge(i, j)
    
    node_colors = [colors[node] for node in G.nodes()]
    pos = nx.spring_layout(G)  # Layout for visualization
    nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, edge_color='gray', node_size=500)
    plt.show()

def main():
    vertices = int(input("\nNhap so dinh: "))
    adj_matrix = input_matrix(vertices)
    
    res_color = solve(adj_matrix, vertices)
    
    print("\nMau cua cac dinh:")
    print(" ".join(map(str, res_color[1:])))  # Bo qua index 0 do chi su dung 1-based indexing
    
    draw_graph(adj_matrix, vertices, res_color)

if __name__ == "__main__":
    main()
