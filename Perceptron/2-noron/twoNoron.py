import numpy as np

x = np.array([
    [1,1],
    [2,2],
    [8,1],
    [9,3],
    [2,7],
    [3,8],
    [8,8],
    [9,9]
])

y1 = np.array([-1,-1,1,1,-1,-1,1,1])
y2 = np.array([-1,-1,-1,-1,1,1,1,1])
w1 = np.array([1,1,1])
w2 = np.array([1,1,1])

def predict(x,w) :
    x.shape = (1,len(x))
    x = np.concatenate((x,np.ones((len(x),1))), axis=1)
    return np.sign(x@w.T)

def train(x,y,w) :
    x = np.concatenate((x,np.ones((len(x),1))), axis=1)
    ypre = np.sign( x @ w.T)
    E = y - ypre
    w = w + E@x
    return w

def toString(o1,o2) :
    return ('[Nhỏ]' if o1 == -1 else '[To]'), ('[Xanh]' if o2 == -1 else '[Chín]')

for i in range(1000) :
    w1 = train(x, y1, w1)
    w2 = train(x, y2, w2)

def pre(x) :
    outN1 = predict(np.array(x), w1)
    outN2 = predict(np.array(x), w2)
    print(toString(outN1,outN2))

with open("input.txt", "r") as f:
  lines = f.readlines()
  input = []
  for line in lines:
    data = line.strip().split(" ")
    input.append([int(data[0]), int(data[1])])

input = np.array(input)
print("--> INPUT:\n", input)
print("--> OUTPUT:")

for i in range(input.shape[0]):
    pre([input[i][0], input[i][1]])