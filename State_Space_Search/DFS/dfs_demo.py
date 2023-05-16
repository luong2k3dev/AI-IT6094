def enterFromFile() :
    graph = dict()
    file = open('../input.txt').read().strip().split('\n')
    print(file)
    for line in file :
        father,sons = tuple(line.split(':'))
        for son in sons.split(',') :
            a = list(graph.get(father,[]))
            a.append(son)
            graph[father] = a
    return graph


graph = enterFromFile()
father = dict()
visited = set()
root = 'A'


def dfs(a, fa = None) :
    visited.add('A')
    global father
    father[a] = fa
    for i in graph.get(a,[]) :
        if i not in visited :
            dfs(i, a)


def trace(a) :
    if a == root:
        print(root,end='')
        return
    trace(father[a])
    print(' -> {}'.format(a),end='')


dfs(root)
trace('N')