import os

class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def searchFile():
    global root, fnameArray, dupNameArray
    node = TreeNode()
    node.data = fnameArray[0]
    root = node
    memory.append(node)

    for name in fnameArray[1:]:
        node = TreeNode()
        node.data = name

        cur = root
        while True:
            if name == cur.data:
                dupNameArray.append(name)
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

memory = []
root = None
fnameArray = []
dupNameArray = []

if __name__ == "__main__":
    folderName = 'C:/Program Files/Common Files/'
    for dirName, subDirList, fnames in os.walk(folderName):
        for fname in fnames:
            fnameArray.append(fname)

    searchFile()

    dupNameArray = list(set(dupNameArray))
    print(folderName, "및 그 하위 디렉터리의 중복된 파일 목록 -->")
    print(dupNameArray)