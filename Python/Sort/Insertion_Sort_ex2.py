def insertionSort(arr):
    n = len(arr)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if arr[cur-1] < arr[cur]:
                arr[cur-1], arr[cur] = arr[cur], arr[cur-1]
    return arr

scoreArray = [['A', 88], ['B', 99], ['C', 71], ['D', 78], ['E', 67], ['F', 92]]

if __name__ == "__main__":
    print("정렬 전 -->", scoreArray)
    scoreArray = insertionSort(scoreArray)
    print("정렬 후 -->", scoreArray)

    print("## 점수별 조 편성표 ##")
    for i in range(len(scoreArray)//2):
        print(scoreArray[i][0], ':', scoreArray[len(scoreArray)-1-i][0])