import random

class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def solution():
    global root, sellArray
    node = TreeNode()
    node.data = sellArray[0]
    root = node
    memory.append(node)

    for name in sellArray[1:]:
        node = TreeNode()
        node.data = name

        cur = root
        while True:
            if name == cur.data:
                break
            if name < cur.data:
                if cur.left == None:
                    cur.left = node
                    memory.append(node)
                    break
                cur = cur.left
            else:
                if cur.right == None:
                    cur.right = node
                    memory.append(node)
                    break
                cur = cur.right

def preOrder(node):
    if node == None:
        return
    print(node.data, end=' ')
    preOrder(node.left)
    preOrder(node.right)

memory = []
root = None
dataArray = ["바나나맛우유", "레쓰비캔커피", "츄파춥스", "도시락", "삼다수", "코카콜라", "삼각김밥"]
sellArray = [random.choice(dataArray) for _ in range(20)]

if __name__ == "__main__":
    print("오늘 판매된 물건-->", sellArray)
    solution()
    print("오늘 판매된 물건 종류-->", end=' ')
    preOrder(root)