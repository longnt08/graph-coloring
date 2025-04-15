import networkx as nx
import matplotlib.pyplot as plt
from generate_graph import generate_adjacency_matrix

# giai thuat quy hoach dong
def solve(adj_matrix, n):
    colors = [1] * (n + 1)  
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            
            # Neu hai dinh ke nhau
            if(adj_matrix[i][j]):
                colors[j] = colors[i] + 1 if colors[j] == colors[i] else colors[j]
    
    return colors

# tao ma tran ke
def input_matrix(n):
    adj_matrix = [0] * ((n + 1) * (n + 1))  # 1-based index
    print("\nNhap ma tran lien ke:")
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            adj_matrix[i][j] = row[j - 1]
    return adj_matrix

# tao danh sach ke
def create_adjacency_list(adj_matrix, n):
    adjacency_list = []
    for i in range(1, n+1):
        neighbors = []
        for j in range(1, n+1):
            if(adj_matrix[i][j]):
                neighbors.append(str(j))
        neighbors_str = ", ".join(neighbors) if neighbors else "None"
        adjacency_list.append(f"'{i}': [{neighbors_str}]")

    return adjacency_list

def draw_graph(adj_matrix, n, colors):
    G = nx.Graph()
    
    for i in range(1, n + 1):
        G.add_node(i, colors=colors[i])
        for j in range(1, n + 1):
            if adj_matrix[i][j]:
                G.add_edge(i, j)
    
    node_colors = [colors[node] for node in G.nodes()]
    pos = nx.spring_layout(G)  # Layout for visualization
    nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, edge_color='gray', node_size=500)
    plt.show()

def main():
    vertices = int(input("\nNhập số đỉnh: "))
    # adj_matrix = input_matrix(vertices)

    adj_matrix = generate_adjacency_matrix(vertices)

    adj_list = create_adjacency_list(adj_matrix, vertices)
    print("Danh sách đỉnh kề: \n")
    for line in adj_list:
        print(f" {line},")
    
    res_colors = solve(adj_matrix, vertices)

    min_color = max(res_colors)
    print(f"\nsố màu ít nhất: {min_color}")
    
    print("\nMàu của các đỉnh:")
    print(" ".join(map(str, res_colors[1:]))) 
    
    draw_graph(adj_matrix, vertices, res_colors)

if __name__ == "__main__":
    main()