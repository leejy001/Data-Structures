class Heap:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def insertElement(self, data):
        self.array.append(data)
        idx = len(self.array)
        if idx > 1:
            node_idx = idx - 1
            # 부모 노드와 새 노드간 크기 비교
            while True:
                next_node_idx = int(node_idx/2)
                # 새 노드가 더 크다면 서로 swap
                if self.array[next_node_idx] < self.array[node_idx]:
                    self.array[node_idx], self.array[next_node_idx] = self.array[next_node_idx], self.array[node_idx]
                else:
                    break
                # 부모 노드로 이동
                node_idx = int(node_idx/2)
                if node_idx == 0:
                    break

    def deleteRoot(self):
        root_value = self.array[0]
        del self.array[0]       # 최상위 노드 삭제

        # 최하단 노드를 최상위로 올리고 최하단 노드 삭제
        last_idx = len(self.array) - 1
        if last_idx < 0:
            return root_value
        tail_value = self.array[last_idx]
        del self.array[last_idx]
        self.array.insert(0, tail_value)
        next_idx = 0
        
        # 최하단 노드 자리 찾기
        while True:
            now_idx = next_idx
            next_idx *= 2
            if next_idx + 2 > last_idx:
                break
            # 자식 노드 중 가장 큰 값 비교
            if self.array[next_idx + 1] > self.array[next_idx + 2]:
                next_idx += 1
            else:
                next_idx += 2
            # 부모 노드와 자식 노드 크기 비교
            if self.array[now_idx] < self.array[next_idx]:
                self.array[now_idx], self.array[next_idx] = self.array[next_idx], self.array[now_idx]
        return root_value

if __name__ == '__main__':
    m_heap = Heap()
    m_heap.insertElement(2)
    m_heap.insertElement(4)
    m_heap.insertElement(5)
    m_heap.insertElement(8)
    m_heap.insertElement(2)
    m_heap.insertElement(3)
    print('Heap :', m_heap)
    print('Delete Root :', m_heap.deleteRoot())
    print('Delete Root :', m_heap.deleteRoot())
    print('Delete Root :', m_heap.deleteRoot())
    print('Heap :', m_heap)