class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]

def printGraph(g):
    print('\t\t', end=' ')
    for v in range(g.SIZE):
        print("%8s" % storeArray[v][0], end=' ')
    print()
    for row in range(g.SIZE):
        print("%8s" % storeArray[row][0], end=' ')
        for col in range(g.SIZE):
            print("%8d" % g.graph[row][col], end=' ')
        print()
    print()

def findVertex(g):
    global cur, maxStore, maxCount
    while len(stack) != 0:
        next = None
        for ver in range(gSize):
            if g.graph[cur][ver] != 0:
                if ver in visited:
                    pass
                else:
                    next = ver
                    break

        if next != None:
            cur = next
            stack.append(cur)
            visited.append(cur)
            if storeArray[cur][1] > maxCount:   # 최대 개수 비교
                maxCount = storeArray[cur][1]
                maxStore = cur
        else:
            cur = stack.pop()

G1 = None
storeArray = [["G25", 30], ["CU", 60], ["Seven11", 10], ["MiniStop", 90], ["Emart24", 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4

if __name__ == "__main__":
    stack = []
    visited = []

    cur = 0  # 시작 편의점
    maxStore = cur  # 최대 개수 편의점 번호 (GS25)
    maxCount = storeArray[cur][1]  # 편의점에 있는 물품 개수
    stack.append(cur)
    visited.append(cur)

    gSize = 5
    G1 = Graph(gSize)
    G1.graph[GS25][CU] = 1; G1.graph[GS25][Seven11] = 1
    G1.graph[CU][GS25] = 1; G1.graph[CU][Seven11] = 1; G1.graph[CU][MiniStop] = 1
    G1.graph[Seven11][GS25] = 1; G1.graph[Seven11][CU] = 1; G1.graph[Seven11][MiniStop] = 1
    G1.graph[MiniStop][Seven11] = 1; G1.graph[MiniStop][CU] = 1; G1.graph[MiniStop][Emart24] = 1
    G1.graph[Emart24][MiniStop] = 1

    print("## 편의점 그래프 ##")
    printGraph(G1)
    findVertex(G1)
    print("물품 최대 보유 편의점(개수)-->", storeArray[maxStore][0], '(', storeArray[maxStore][1],')')