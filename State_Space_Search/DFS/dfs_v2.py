# Định nghĩa class Graph để lưu trữ đồ thị
class Graph:
    def __init__(self):
        self.vertices = set()  # tập hợp các đỉnh của đồ thị
        self.edges = {}  # tập hợp các cạnh của đồ thị

    def add_edge(self, from_vert, to_vert):
        # Thêm một cạnh mới vào đồ thị
        if from_vert not in self.vertices:
            self.vertices.add(from_vert)
            self.edges[from_vert] = set()
        if to_vert not in self.vertices:
            self.vertices.add(to_vert)
            self.edges[to_vert] = set()
        self.edges[from_vert].add(to_vert)

    def dfs(self, start, end, path=[]):
        # Tìm kiếm đường đi từ đỉnh start đến đỉnh end bằng DFS
        path = path + [start]
        if start == end:
            return path
        if start not in self.vertices:
            return None
        for v in self.edges[start]:
            if v not in path:
                newpath = self.dfs(v, end, path)
                if newpath: return newpath
        return None

# Hàm đọc đồ thị từ file input.txt và tạo graph object
def read_graph(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        print(lines)
    graph = Graph()
    for line in lines:
        from_vert, to_verts = line.strip().split(":")
        for to_vert in to_verts.split(","):
            graph.add_edge(from_vert, to_vert)
    return graph

# Thực hiện chạy thuật toán
if __name__ == "__main__":
    graph = read_graph("../input.txt")
    path = graph.dfs('A', 'N')

    if path:
        print(" -> ".join(path))
    else:
        print("Không tìm thấy đường đi từ A đến N")