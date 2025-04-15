import numpy as np
import random

def generate_adjacency_matrix(num_nodes, edge_probability=0.5):
    matrix = np.zeros((num_nodes + 1, num_nodes + 1), dtype=int)
    
    for i in range(1, num_nodes+1):
        for j in range(i + 1, num_nodes+1):  # Chỉ xét nửa trên
            if random.random() < edge_probability:
                matrix[i][j] = 1
                matrix[j][i] = 1  # Đảm bảo đối xứng cho đồ thị vô hướng

    return matrix

# Tạo ma trận kề cho đồ thị 100 đỉnh
# adj_matrix = generate_adjacency_matrix(5)

# In thử vài dòng đầu
# print(adj_matrix[:5, :5])
