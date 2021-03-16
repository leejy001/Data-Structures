class TreeNode():
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


def insertNode(num):
    cur = root
    while True:
        if num < cur.data:
            if cur.left != None:
                cur = cur.left
            else:
                cur.left = TreeNode(data)
                break
        else:
            if cur.right != None:
                cur = cur.right
            else:
                cur.right = TreeNode(data)
                break

def seatchNode(f_num):
    cur = root

    while True:
        if f_num == cur.data:
            print(f_num, "을(를) 찾음...")
            break
        elif f_num > cur.data:
            if cur.right == None:
                print(f_num, "이(가) 트리에 없음...")
                break
            cur = cur.right
        else:
            if cur.left == None:
                print(f_num, "이(가) 트리에 없음...")
                break
            cur = cur.left

def delNode(d_num):

    is_search = False
    cur = root
    parent = root
    while cur:
        if cur.data == d_num:
            is_search = True
            break
        elif d_num < cur.data:
            parent = cur
            cur = cur.left
        else:
            parent = cur
            cur = cur.right

    if is_search == False:
        return print("해당 값 없음...")

    # 삭제할 노드가 리프 노드일 때
    if cur.left == None and cur.right == None:
        if d_num < parent.d_num:
            parent.left = None
        else:
            parent.right = None

    # 삭제할 노드가 왼쪽 자식 노드를 가질 때
    if cur.left != None and cur.right == None:
        if d_num < parent.data:
            parent.left = cur.left
        else:
            parent.right = cur.left

    # 삭제할 노드가 오른쪽 자식 노드를 가질 때
    if cur.left == None and cur.right != None:
        if d_num < parent.data:
            parent.left = cur.right
        else:
            parent.right = cur.right

    # 삭제할 노드가 자식 노드를 두 개 가지고 있을 때
    if cur.left != None and cur.right != None:
        temp = temp_parent = cur.right
        while temp.left != None:
            temp_parent = temp
            temp = temp.left
        if temp.right != None:
            temp_parent.left = temp.right
        else:
            temp_parent.left = None

        if d_num < parent.data:
            parent.left = temp
            temp.right = cur.right
            temp.left = cur.left
        else:
            parent.right = temp
            temp.left = cur.left
            temp.right = cur.right

    return print(d_num, "삭제 완료")

memory = []
root = None
dataArray = [10, 15, 8, 3, 9, 6, 1, 20, 30]

if __name__ == "__main__":
    node = TreeNode(dataArray[0])
    root = node
    memory.append(node)

    for data in dataArray[1:]:
        node = TreeNode(data)

        cur = root
        while True:
            if data < cur.data:
                if cur.left == None:
                    cur.left = node
                    break
                cur = cur.left
            else:
                if cur.right == None:
                    cur.right = node
                    break
                cur = cur.right

        memory.append(node)

    insertNode(7)

    seatchNode(9)

    delNode(15)