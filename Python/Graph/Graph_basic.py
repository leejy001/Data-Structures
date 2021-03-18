class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]

def printGraph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(nameArray[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(nameArray[row], end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end=' ')
        print()
    print()

G1 = None
nameArray = ['A', 'B', 'C', 'D', 'E', 'F']
A, B, C, D, E, F = 0, 1, 2, 3, 4, 5

gSize = 6
G1 = Graph(gSize)
G1.graph[A][B] = 1; G1.graph[A][C] = 1
G1.graph[B][A] = 1; G1.graph[B][D] = 1
G1.graph[C][A] = 1; G1.graph[C][D] = 1
G1.graph[D][B] = 1; G1.graph[D][C] = 1; G1.graph[D][E] = 1; G1.graph[D][F] = 1
G1.graph[E][D] = 1; G1.graph[E][F] = 1
G1.graph[F][D] = 1; G1.graph[F][E] = 1

print("## G1 무방향 그래프 ##")
printGraph(G1)