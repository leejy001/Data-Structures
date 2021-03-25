import random
import time

def bubbleSort(arr):
    n = len(arr)

    for end in range(n-1, 0, -1):
        changeYN = False
        for cur in range(0, end):
            if arr[cur] > arr[cur+1]:
                arr[cur], arr[cur+1] = arr[cur+1], arr[cur]
                changeYN = True
        if not changeYN:
            break
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

tempArray = [random.randint(10000, 99999) for _ in range(1000000)]
tempArray.sort()

rndPos = random.randint(0, len(tempArray)-1)
print("# 데이터 개수 --> ", len(tempArray))
print("# 끼어든 위치 --> ", rndPos)
tempArray.insert(rndPos, tempArray[-1])

bubbleArray = tempArray[:]
quickArray = tempArray[:]

start = time.time()
bubbleSort(bubbleArray)
end = time.time()
print("재정렬 시간(버블 정렬) --> %10.3f 초" % (end - start))

start = time.time()
quickSort(bubbleArray)
end = time.time()
print("재정렬 시간(퀵 정렬) --> %10.3f 초" % (end - start))