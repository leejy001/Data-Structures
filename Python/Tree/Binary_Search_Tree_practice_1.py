import random

class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 책 이름 트리
def bookName():
    global rootBook, rootAuth, bookArray
    node = TreeNode()
    node.data = bookArray[0][0]
    rootBook = node
    memory.append(node)

    for book in bookArray[1:]:
        name = book[0]
        node = TreeNode()
        node.data = name

        cur = rootBook
        while True:
            if name < cur.data:
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

    print("책 이름 트리 구성 완료!")

# 작가 이름 트리
def authName():
    global rootBook, rootAuth, bookArray
    node = TreeNode()
    node.data = bookArray[0][1]
    rootAuth = node
    memory.append(node)

    for book in bookArray[1:]:
        name = book[1]
        node = TreeNode()
        node.data = name

        cur = rootAuth
        while True:
            if name <cur.data:
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

    print("작가 이름 트리 구성 완료!")

memory = []
rootBook, rootAuth = None, None
bookArray = [["어린왕자", "생떽쥐베리"], ["이방인", "까뮈"], ["부활", "톨스토이"], ["신곡", "단테"], ["대지", "펄벅"],
             ["돈키호테", "세르반테스"], ["동물농장", "조지오웰"], ["데미안", "헤르만헤세"], ["파우스트", "괴테"]]
random.shuffle(bookArray)

if __name__ == "__main__":
    bookName()
    authName()
    # 책 이름 및 작가 이름 검색
    bookOrAuth = int(input("책검색(1), 작가검색(2)-->"))
    findName = input("검색할 책 또는 작가-->")

    if bookOrAuth == 1:
        root = rootBook
    else:
        root = rootAuth

    cur = root
    while True:
        if findName == cur.data:
            print(findName, "을(를) 찾음.")
            break
        elif findName < cur.data:
            if cur.left == None:
                print(findName, "이(가) 목록에 없음")
                break
            cur = cur.left
        else:
            if cur.right == None:
                print(findName, "이(가) 목록에 없음")
                break
            cur = cur.right