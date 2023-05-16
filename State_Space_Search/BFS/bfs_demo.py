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
visited = set()
root = 'A'
q = []
q.append(root)
visited.add(root)
father[root] = None

def bfs(end) :
    while q :
        t = q.pop(0)
        for i in graph.get(t,[]) :
            if i not in visited :
                father[i] = t
                visited.add(i)
                if i == end :
                    return
                q.append(i)


def trace(a) :
    if a == root:
        print(root,end='')
        return
    trace(father[a])
    print(' -> {}'.format(a),end='')


bfs('N')
trace('N')