class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]

G1 = None
stack = []
visitedArray = []

G1 = Graph(4)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("## G1 무방향 그래프 ##")
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end=' ')
    print()

cur = 0
stack.append(cur)
visitedArray.append(cur)

while len(stack) != 0:
    next = None
    for ver in range(4):
        if G1.graph[cur][ver] == 1:
            if ver in visitedArray: # 방문한 적이 있다면
                pass
            else:                   # 방문한 적이 없다면
                next = ver          # 다음 정점으로 지정
                break

    if next != None:    # 다음에 방문할 정점이 있는 경우
        cur = next
        stack.append(cur)
        visitedArray.append(cur)
    else:               # 다음에 방문할 정점이 없는 경우
        cur = stack.pop()

print('방문 순서 -->', end=' ')
for i in visitedArray:
    print(chr(ord('A')+i), end=' ')