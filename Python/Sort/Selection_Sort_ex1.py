def selectionSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if arr[minIdx] > arr[k]:
                minIdx = k

        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr

arr = [7, 5, 11, 6, 9, 80000, 10, 6, 15, 12]

if __name__ == "__main__":
    print("정렬 전 -->", arr)
    arr = selectionSort(arr)
    print("정렬 후 -->", arr)
    print("중앙 값 -->", arr[len(arr)//2])