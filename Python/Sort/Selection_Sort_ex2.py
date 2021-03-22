def selectionSort(arr):
    n = len(arr)

    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if arr[minIdx] > arr[k]:
                minIdx = k
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr

arr1 = [[55,33,250,44],[88,1,76,23],[199,222,38,47],[155,145,20,99]]
arr2 = []

if __name__ == "__main__":
    for i in range(len(arr1)):
        for k in range(len(arr1[i])):
            arr2.append(arr1[i][k])

    print("1차원 변경 후, 정렬 전 -->", arr2)
    arr2 = selectionSort(arr2)
    print("1차원 변경 후, 정렬 후 -->", arr2)
    print("중앙값 -->", arr2[len(arr2)//2])