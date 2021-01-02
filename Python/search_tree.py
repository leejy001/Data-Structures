import random

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)

class SearchTree:
    def __init__(self):
        self.root = None

    def insertElement(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node

        node = self.root
        while True:
            prev_node = node
            # 새 노드의 데이터가 작을 시 왼쪽 이동
            if node.data > new_node.data:
                node = node.left
                # 이동한 노드가 빈 노드면 추가
                if node is None:
                    node = new_node
                    prev_node.left = node
            # 새 노드의 데이터가 크면 오른쪽 이동
            elif node.data < new_node.data:
                node = node.right
                if node is None:
                    node = new_node
                    prev_node.right = node
            # 똑같은 키가 있으면 취소
            else:
                return

    def searchElement(self, data):
        node = self.root
        while True:
            if node.data > data:    # 탐색 값이 작다면
                node = node.left
            elif node.data < data:  # 탐색 값이 크다면
                node = node.right
            elif node.data is data:
                break
            else:
                return Node('No search results')
        return node

    def preorderTraversal(self, node):  # 전위 순회
        print(node, end=' ')
        if not node.left is None:
            self.preorderTraversal(node.left)
        if not node.right is None:
            self.preorderTraversal(node.right)

    def inorderTraversal(self, node):   # 중위 순회
        if not node.left is None:
            self.inorderTraversal(node.left)
        print(node, end=' ')
        if not node.right is None:
            self.inorderTraversal(node.right)

    def postorderTraversal(self, node): # 후위 순회
        if not node.left is None:
            self.postorderTraversal(node.left)
        if not node.right is None:
            self.postorderTraversal(node.right)
        print(node, end=' ')

if __name__ == "__main__":
    m_tree = SearchTree()

    m_tree.insertElement(100)
    for i in range(20):
        m_tree.insertElement(random.randint(0,100))

    print(       '전위 순회 : ', end='') ; m_tree.preorderTraversal(m_tree.root)
    print('\n' + '중위 순회 : ', end='') ; m_tree.inorderTraversal(m_tree.root)
    print('\n' + '후위 순회 : ', end='') ; m_tree.postorderTraversal(m_tree.root)

    node = m_tree.searchElement(100)
    print('\n' + '탐색한 노드의 값 :', node)
    print(       '노드의 왼쪽 서브 트리 :', node.left)
    print(       '노드의 오른쪽 서브 트리 :', node.right)

    node = m_tree.searchElement(node.left.data)
    print('\n' + '탐색한 노드의 값 :', node)
    print(       '노드의 왼쪽 서브 트리 :', node.left)
    print(       '노드의 오른쪽 서브 트리 :', node.right)