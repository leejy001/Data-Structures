class Stack():
    def __init__(self):
        self.stack = []

    # 맨 위에 값 추가
    def push(self, data):
        self.stack.append(data)

    # 맨 위의 값 삭제 (비어있다면 -1 출력)
    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    # 스택 변형 없이 맨 위의 값 출력
    def peek(self):
        return self.stack[-1]

    # 스택에 값이 비어있는지 아닌지 확인
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

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