from operator import itemgetter

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]

def printGraph(g):
    print('\t', end=' ')
    for v in range(g.SIZE):
        print(storeArray[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(storeArray[row], end=' ')
        for col in range(g.SIZE):
            print("%2d" % g.graph[row][col], end=' ')
        print()
    print()

def findVertex(g, findVtx):
    stack = []
    visited = []

    cur = 0     # 시작 도시
    stack.append(cur)
    visited.append(cur)

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
        else:
            cur = stack.pop()

    if findVtx in visited:
        return True
    else:
        return False

G1 = None
storeArray = ["서울", "뉴욕", "런던", "북경", "방콕", "파리"]
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5

if __name__ == "__main__":

    gSize = 6
    G1 = Graph(gSize)
    G1.graph[서울][뉴욕] = 80; G1.graph[서울][북경] = 10
    G1.graph[뉴욕][서울] = 80; G1.graph[뉴욕][북경] = 40; G1.graph[뉴욕][방콕] = 70
    G1.graph[런던][방콕] = 30; G1.graph[런던][파리] = 60
    G1.graph[북경][서울] = 10; G1.graph[북경][뉴욕] = 40; G1.graph[북경][방콕] = 50
    G1.graph[방콕][뉴욕] = 70; G1.graph[방콕][북경] = 50; G1.graph[방콕][런던] = 30; G1.graph[방콕][파리] = 20
    G1.graph[파리][방콕] = 20; G1.graph[파리][런던] = 60

    print("## 해저 케이블 전체 연결도 ##")
    printGraph(G1)

    # 가중치 간선 목록
    edgeArray = []
    for i in range(gSize):
        for k in range(gSize):
            if G1.graph[i][k] != 0:
                edgeArray.append([G1.graph[i][k], i, k])

    edgeArray = sorted(edgeArray, key=itemgetter(0), reverse=False)
    newArray = []
    for i in range(0, len(edgeArray), 2):
        newArray.append(edgeArray[i])

    index = 0
    while len(newArray) > gSize-1:
        start = newArray[index][1]
        end = newArray[index][2]
        saveCost = newArray[index][0]

        G1.graph[start][end] = 0
        G1.graph[end][start] = 0

        startYN = findVertex(G1, start)
        endYN = findVertex(G1, end)

        if startYN and endYN:
            del(newArray[index])
        else:
            G1.graph[start][end] = saveCost
            G1.graph[end][start] = saveCost
            index += 1

    print("## 가장 효율적인 해저 케이블 연결도 ##")
    printGraph(G1)