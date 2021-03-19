from operator import itemgetter

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]

def printGraph(g):
    print('  ', end=' ')
    for v in range(g.SIZE):
        print(nameArray[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(nameArray[row], end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end='\t')
        print()
    print()

def findVertex(g, findVtx):
    stack = []
    visited = []

    cur = 0
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
nameArray = ["춘천", "서울", "속초", "대전", "광주", "부산"]
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

gSize = 6
G1 = Graph(gSize)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25;
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print("## 자전거 도로 건설을 위한 전체 연결도 ##")
printGraph(G1)

edgeArray = []      # 가중치 간선 목록 [가중치, 도시1, 도시2]
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k] != 0:
            edgeArray.append([G1.graph[i][k], i, k])

edgeArray = sorted(edgeArray, key=itemgetter(0), reverse=True)

newArray = []       # 중복되는 간선 목록 삭제
for i in range(0, len(edgeArray), 2):
    newArray.append(edgeArray[i])

index = 0
# 가중치가 높은 간선부터 제거
while len(newArray) > gSize-1:
    start = newArray[index][1]
    end = newArray[index][2]
    saveCost = newArray[index][0]   # 복구를 대비하여 가중치 임시 저장

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = findVertex(G1, start)
    endYN = findVertex(G1, end)

    if startYN and endYN:   # 간선을 제거해도 된다면 제거
        del(newArray[index])
    else:                   # 간선을 제거하면 안되는 경우 복구
        G1.graph[start][end] = saveCost
        G1.graph[end][start] = saveCost
        index += 1

print("## 최소 비용의 자전거 도로 연결도 ##")
printGraph(G1)