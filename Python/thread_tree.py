class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_thread_right = None

    def __str__(self):
        return str(self.data)

class ThreadTree:
    def __init__(self):
        self.root = None

    def inorderTraversal(self, node):   # 중위 순회
        while node.left is not None:    # 가장 처음 왼쪽으로 이동
            node = node.left
        print(node, end='')
        while True:
            node = self.findThread(node)
            print(node, end='')
            if node.right is None:      # 끝까지 돌았을 경우
                break

    def findThread(self, node):
        prev_node = node
        node = node.right
        if node is None:
            return node
        # 오른쪽 링크가 후행자인 경우 반환
        if prev_node.is_thread_right:
            return node
        # 오른쪽 링크가 서브 트리인 경우 왼쪽 서브 트리 끝으로 이동
        while node.left is not None:
            node = node.left
        return node

    def makeRoot(self, node, left_node, right_node, thread):
        if self.root is None:
            self.root = node
        node.left = left_node
        node.right = right_node
        node.is_thread_right = thread

if __name__ == "__main__":
    node = []
    node.append(Node('+'))
    node.append(Node('-'))
    node.append(Node('/'))
    node.append(Node('A'))
    node.append(Node('B'))
    node.append(Node('C'))
    node.append(Node('D'))

    m_tree = ThreadTree()
    for i in range(int(len(node)/2)):
        m_tree.makeRoot(node[i], node[i*2+1], node[i*2+2], False)

    m_tree.makeRoot(node[3], None, None, True)
    m_tree.makeRoot(node[4], None, None, True)
    m_tree.makeRoot(node[5], None, None, True)

    node[3].right = node[1]
    node[4].right = node[0]
    node[5].right = node[2]

    print('중위 순회 :', end='') ; m_tree.inorderTraversal(m_tree.root)