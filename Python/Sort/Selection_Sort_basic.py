def findMin(data):
    min_idx = 0
    for i in range(1, len(data)):
        if data[min_idx] < data[i]:
            min_idx = i
    return min_idx

arr = [188, 162, 168, 120, 50, 150, 177, 105]
result = []

if __name__ == "__main__":
    print("정렬 전 -->", arr)
    for _ in range(len(arr)):
        minPos = findMin(arr)
        result.append(arr[minPos])
        del(arr[minPos])

    print("정렬 후 -->", result)


# 개선 코드
def selectionSort(arr):
    n = len(arr)

    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if arr[minIdx] > arr[k]:
                minIdx = k
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr

arr = [188, 162, 168, 120, 50, 150, 177, 105]

if __name__ == "__main__":
    print("정렬 전 -->", arr)
    arr = selectionSort(arr)
    print("정렬 후 -->", arr)