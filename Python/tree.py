class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def preorderTraversal(self, node):  # 전위 순회
        print(node, end='')
        if not node.left is None:
            self.preorderTraversal(node.left)
        if not node.right is None:
            self.preorderTraversal(node.right)

    def inorderTraversal(self, node):   # 중위 순회
        if not node.left is None:
            self.inorderTraversal(node.left)
        print(node, end='')
        if not node.right is None:
            self.inorderTraversal(node.right)

    def postorderTraversal(self, node): # 후위 순회
        if not node.left is None:
            self.postorderTraversal(node.left)
        if not node.right is None:
            self.postorderTraversal(node.right)
        print(node, end='')

    def makeRoot(self, node, left_node, right_node):
        if self.root is None:
            self.root = node
        node.left = left_node
        node.right = right_node

if __name__ == "__main__":
    node = []
    node.append(Node('+'))
    node.append(Node('-'))
    node.append(Node('/'))
    node.append(Node('A'))
    node.append(Node('B'))
    node.append(Node('C'))
    node.append(Node('D'))

    m_tree = Tree()
    for i in range(int(len(node)/2)):
        m_tree.makeRoot(node[i], node[i*2+1], node[i*2+2])

    print('전위 순회 : ', end='') ; m_tree.preorderTraversal(m_tree.root)
    print('\n중위 순회 : ', end='') ; m_tree.inorderTraversal(m_tree.root)
    print('\n후위 순회 : ', end='') ; m_tree.postorderTraversal(m_tree.root)