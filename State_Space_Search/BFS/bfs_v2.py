from collections import defaultdict

# Đọc dữ liệu từ file input.txt và lưu đồ thị vào một danh sách kề
def enterFromFile() :
    graph = defaultdict(list)
    file = open('../input.txt').read().strip().split('\n')
    print(file)
    for line in file:
        node, neighbors = line.strip().split(":")
        graph[node] = neighbors.split(",")
    return graph

# Định nghĩa hàm bfs để tìm kiếm đường đi từ một đỉnh s đến đỉnh t
def bfs(graph, s, t):
    visited = set()  # Danh sách các đỉnh đã duyệt
    queue = [[s]]  # Hàng đợi ban đầu chỉ chứa đỉnh gốc
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == t:  # Nếu tìm thấy đỉnh t, trả về đường đi
                    return new_path
            visited.add(node)  # Đánh dấu đỉnh đã duyệt
    return None  # Không tìm thấy đường đi từ s đến t

# Thực hiện chạy thuật toán
if __name__ == "__main__":
    start_node = "A"
    end_node = "N"

    graph = enterFromFile()
    path = bfs(graph, start_node, end_node)

    if path is not None:
        print(" -> ".join(path))
    else:
        print(f"Không có đường đi từ {start_node} đến {end_node}.")