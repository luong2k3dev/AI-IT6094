import numpy as np

# Đọc dữ liệu train vào ma trận x, y từ file dataTrain.txt
data = []
labels = []

with open('dataTrain.txt', 'r') as f:
    for line in f:
        row = line.strip().split()
        data.append([float(x) for x in row[:-1]])
        labels.append(int(row[-1]))

x = np.array(data)
y = np.array(labels)
print("--> Data Train:")
print("Data Train x:\n", x)
print("Data Train y:\n", y)
w1 = np.array([1, 1, 1])

# Dự đoán
def predict(x, w):
    x = np.array(x)
    if x.ndim == 1:
        x.shape = (1, len(x))
    x = np.concatenate((x, np.ones((len(x), 1))), axis=1)
    return np.sign(x @ w)


# Huấn luyện mô hình
def train(x, y, w, timeTrain):
    x = np.concatenate((x, np.ones((len(x), 1))), axis=1)  # thêm cột 1 để nhân chồng bias
    for i in range(timeTrain):
        ypre = np.sign(x @ w.T)
        E = y - ypre
        w = w + E @ x
    return w

# Chuyển kết quả về string
def toString(ans):
    return ('[Xanh]' if ans == -1 else '[Chín]')

w1 = train(x, y, w1, 100)

# Đọc dữ liệu đầu vào vào mảng input từ file input.txt
with open("input.txt", "r") as f:
  lines = f.readlines()
  input = []
  for line in lines:
    data = line.strip().split(" ")
    input.append([int(data[0]), int(data[1])])

input = np.array(input)
print("--> INPUT:\n", input)
print("--> OUTPUT:")

# Output
for i in range(input.shape[0]):
    res = predict([input[i][0],input[i][1]], w1)
    print("Khoi luong =", input[i][0], ", Do Chin =", input[i][1], "=> Du Doan", toString(res))