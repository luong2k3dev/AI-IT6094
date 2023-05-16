from queue import Queue
from collections import defaultdict

# Khởi tạo dictionary, nếu truy cập vào key chưa tồn tại trong dictionary graph, giá trị của nó sẽ là một danh sách rỗng
graph = defaultdict(list)

# Đọc file input.txt và biểu diễn đồ thị dưới dạng danh sách kề
with open('../input.txt', 'r') as f:
    for line in f:
        node, children = line.strip().split(':')
        children = children.split(',')
        graph[node] = [child for child in children]

# Hàm tìm đường đi từ đỉnh start đến đỉnh end bằng BFS
def bfs(start, end):
    parent = {}
    visited = set()
    queue = Queue()

    # Khởi tạo hàng đợi và đỉnh ban đầu
    queue.put(start)
    visited.add(start)

    # Bắt đầu vòng lặp BFS
    while not queue.empty():
        current = queue.get()

        # Nếu tìm được đỉnh kết thúc thì quay lại với đường đi từ start đến end
        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return list(reversed(path))

        # Duyệt qua tất cả các đỉnh con của đỉnh hiện tại
        for neighbor in graph[current]:
            # Nếu chưa được duyệt thì thêm vào hàng đợi và lưu trữ thông tin cha
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put(neighbor)
                parent[neighbor] = current

    # Trường hợp không tìm được đường đi từ start đến end
    return None

# Gọi hàm bfs để tìm đường đi từ A đến N
start = 'A'
end = 'N'
path = bfs(start, end)

if path is None:
    print(f'Không tìm được đường đi từ {start} đến {end}.')
else:
    print(f'Đường đi từ {start} đến {end}: {" -> ".join(path)}')