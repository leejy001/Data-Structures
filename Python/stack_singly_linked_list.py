class Node:
    def __init__(self, data):
        self.data = data
        self.node = None

class Stack:
    def __init__(self):
        self.head = None

    # 노드 생성 (head가 새로운 노드를 가리킴)
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 노드 삭제 노드가 비어있다면 -1 리턴
    def pop(self):
        if self.is_empty():
            return -1
        data = self.head.data
        self.head = self.head.next
        return data

    # 노드의 변형 없이 가장 앞의 값 출력
    def peek(self):
        if self.is_empty():
            return -1
        return self.head.data

    # 노드가 없는지 확인
    def is_empty(self):
        if self.head:
            return False
        return True

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek()) # 3
    print(s.pop())  # 3
    print(s.pop())  # 2
    print(s.pop())  # 1
    print(s.pop())  # -1 (더 이상 존재하지 않음)