from collections import defaultdict

# Khởi tạo dictionary, nếu truy cập vào key chưa tồn tại trong
# dictionary graph, giá trị của nó sẽ là một danh sách rỗng
graph = defaultdict(list)

# Đọc dữ liệu từ file input.txt và lưu vào danh sách kề
with open('../input.txt') as f:
    for line in f:
        u, v_list = line.strip().split(':')
        v_list = v_list.split(',')
        graph[u] = [v for v in v_list]

# Tìm đường đi từ giữa hai đỉnh sử dụng thuật toán DFS
def dfs(u, visited, target):
    if u == target:
        return [u]
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            res = dfs(v, visited, target)
            if res:
                return [u] + res
    return None

# Thực hiện chạy thuật toán
if __name__ == "__main__":
    start, end = 'A', 'N'
    visited = set()
    path = dfs(start, visited, end)
    if path:
        print("Đường đi từ", start, " đến ", end, ":", " -> ".join(path))
    else:
        print("Không tìm được đường đi từ", start, " đến ", end)