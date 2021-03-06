
def find_insert(name, count):
    pos = -1
    for i in range(len(arr)):
        pair = arr[i]
        if count >= pair[1]:
            pos = i
            break
    if pos == -1:
        pos = len(arr)

    insert_data(pos, (name, count))

def insert_data(pos, data):
    if pos < 0 or pos > len(arr):
        print("데이터를 삽입할 범위 초과")
        return

    arr.append(None)
    dLen = len(arr)

    for i in range(dLen - 1, pos, -1):
        arr[i] = arr[i-1]
        arr[i-1] = None

    arr[pos] = data

arr = [('A', 200), ('B', 100), ('C', 50), ('D', 25)]

if __name__ == "__main__":

    while True:
        data = input("추가 문자--> ")
        count = int(input("횟수--> "))
        find_insert(data, count)
        print(arr)