import random
import time

def selectionSort(arr):
    n = len(arr)

    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if arr[minIdx] > arr[k]:
                minIdx = k
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr

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

countArray = [1000, 10000, 12000, 15000]

for count in countArray:
    tempArray = [random.randint(10000, 99999) for _ in range(count)]
    selectArray = tempArray[:]
    quickArray = tempArray[:]

    print("## 데이터 수 : ", count, "개")
    start = time.time()
    selectionSort(selectArray)
    end = time.time()
    print("  선택 정렬 --> %10.3f 초" % (end-start))
    start = time.time()
    quickSort(selectArray)
    end = time.time()
    print("   퀵 정렬 --> %10.3f 초" % (end-start))
    print()