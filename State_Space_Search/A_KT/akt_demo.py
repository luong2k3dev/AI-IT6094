import queue

def enterFromFile() :
    graph = dict()
    file = open('../input.txt').read().strip().split('\n')
    print(file)
    for line in file :
        father,sons = tuple(line.split(':'))
        for son in sons.split(',') :
            a  = list(graph.get(father,[]))
            a.append(son)
            graph[father] = a
    return graph


graph = enterFromFile()
father = dict()
distance = dict()
visited = set()
root = 'A'
distance[root] = 0
visited.add(root)
q = queue.PriorityQueue()
q.put((distance[root],root))


def heuristic(i) :
    return 1


def akt() :
    while not  q.empty() :
        t = q.get()
        for i in graph.get(t[1],[]) :
            if (i not in visited)  :
                father[i] = t[1]
                distance[i] = distance[t[1]] + 1
                q.put((distance[i] + heuristic(i) ,i))


def trace(a) :
    if a == root:
        print(root,end='')
        return
    trace(father[a])
    print(' -> {}'.format(a),end='')
akt()
trace('N')