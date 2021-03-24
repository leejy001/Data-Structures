def quickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[n//2]
    leftArr, rightArr = [], []

    for num in arr:
        if num < pivot:
            leftArr.append(num)
        elif num > pivot:
            rightArr.append(num)

    return quickSort(leftArr) + [pivot] + quickSort(rightArr)

arr = [188, 150, 168, 162, 105, 120, 177, 50]

if __name__ == "__main__":

    print("정렬 전 -->", arr)
    arr = quickSort(arr)
    print("정렬 후 -->", arr)


# 중복값 고려
def quickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[n//2]
    leftArr, midArr, rightArr = [], [], []

    for num in arr:
        if num < pivot:
            leftArr.append(num)
        elif num > pivot:
            rightArr.append(num)
        else:
            midArr.append(num)

    return quickSort(leftArr) + midArr + quickSort(rightArr)

arr = [120, 120, 188, 150, 168, 50, 50, 162, 105, 120, 177, 50]

if __name__ == "__main__":

    print("정렬 전 -->", arr)
    arr = quickSort(arr)
    print("정렬 후 -->", arr)


# 배열 하나로 구현
def qSort(arr, start, end):
    if end <= start:
        return

    low = start
    high = end

    pivot = arr[(low+high)//2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low+1, high-1
    mid = low
    qSort(arr, start, mid-1)
    qSort(arr, mid, end)

def quickSort(arr):
    qSort(arr, 0, len(arr)-1)

arr = [188, 150, 168, 162, 105, 120, 177, 50]

if __name__ == "__main__":
    print("정렬 전 -->", arr)
    quickSort(arr)
    print("정렬 후 -->", arr)