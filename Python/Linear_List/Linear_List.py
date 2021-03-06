def add_data(data):
    arr.append(None)
    dLen = len(arr)
    arr[dLen-1] = data

def insert_data(pos, data):
    if pos < 0 or pos > len(arr):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    arr.append(None)
    dLen = len(arr)

    for i in range(dLen-1, pos, -1):
        arr[i] = arr[i-1]
        arr[i-1] = None

    arr[pos] = data

def delete_data(pos):
    if pos < 0 or pos > len(arr):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    dLen = len(arr)
    arr[pos] = None

    for i in range(pos+1, dLen):
        arr[i-1] = arr[i]
        arr[i] = None

    del(arr[dLen-1])

arr = []
select = -1

if __name__ == "__main__":

    while (select != 4):
        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)-->"))

        if select == 1:
            data = int(input("추가할 데이터-->"))
            add_data(data)
            print(arr)
        elif select == 2:
            pos, data = map(int, input("삽입할 위치 및 데이터-->").split())
            insert_data(pos, data)
            print(arr)
        elif select == 3:
            pos = int(input("삭제할 위치-->"))
            delete_data(pos)
            print(arr)
        elif select == 4:
            print(arr)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue