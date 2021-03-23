def bubbleSort(arr):
    global cnt
    n = len(arr)

    for end in range(n-1, 0, -1):
        for cur in range(0, end):
            if arr[cur] > arr[cur+1]:
                arr[cur], arr[cur+1] = arr[cur+1], arr[cur]
            cnt += 1
    return arr

arr = [50, 105, 120, 188, 150, 162, 168, 177]
cnt = 0

if __name__ == "__main__":

    print("정렬 전 -->", arr)
    arr = bubbleSort(arr)
    print("정렬 후 -->", arr)
    print("횟수 -->", cnt)

def bubbleSort(arr):
    global cnt
    n = len(arr)

    for end in range(n-1, 0, -1):
        changeYN = False
        for cur in range(0, end):
            if arr[cur] > arr[cur+1]:
                arr[cur], arr[cur+1] = arr[cur+1], arr[cur]
                changeYN = True
            cnt += 1
        if not changeYN:
            break
    return arr

arr = [50, 105, 120, 188, 150, 162, 168, 177]
cnt = 0

if __name__ == "__main__":

    print("정렬 전 -->", arr)
    arr = bubbleSort(arr)
    print("정렬 후 -->", arr)
    print("횟수 -->", cnt)