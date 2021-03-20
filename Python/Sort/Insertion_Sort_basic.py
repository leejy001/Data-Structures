def findInsertIdx(arr, data):
    findIdx = -1
    for i in range(0, len(arr)):
        if arr[i] > data:
            findIdx = i
            break
    if findIdx == -1:
        return len(arr)
    else:
        return findIdx

arr = [188, 162, 168, 120, 50, 150, 177, 105]
result = []

if __name__ == "__main__":
    print("정렬 전 -->", arr)

    for i in range(len(arr)):
        data = arr[i]
        inPos = findInsertIdx(result, data)
        result.insert(inPos, data)

    print("정렬 후 -->", result)


# 개선된 코드
def insertionSort(arr):
    n = len(arr)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if arr[cur-1] > arr[cur]:
                arr[cur-1], arr[cur] = arr[cur], arr[cur-1]
    return arr

arr = [188, 162, 168, 120, 50, 150, 177, 105]

if __name__ == "__main__":
    print("정렬 전 -->", arr)
    arr = insertionSort(arr)
    print("정렬 후 -->", arr)