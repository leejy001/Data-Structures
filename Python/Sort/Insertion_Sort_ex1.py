import os

def makeFileList(folderName):
    fnameArray = []
    for dirName, subDirList, fnames in os.walk(folderName):
        for fname in fnames:
            fnameArray.append(fname)
    return fnameArray

def insertionSort(arr):
    n = len(arr)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if arr[cur-1] < arr[cur]:
                arr[cur-1], arr[cur] = arr[cur], arr[cur-1]
    return arr

fileArray = []

if __name__ == "__main__":
    fileArray = makeFileList('C:/Program Files/Common Files')
    fileArray = insertionSort(fileArray)
    print("파일명 역순 정렬 -->", fileArray)