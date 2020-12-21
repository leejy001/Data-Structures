test = [1,2,3,4,5]
test.append(6) # 맨뒤에 삽입
print(test)
test.insert(0, 0) # index의 위치에 삽입
print(test)
del test[0] # index의 원소 삭제
print(test)
test.remove(3) # 원소를 찾아 삭제 (원소가 없으면 valueError 발생)
print(test)
print(test.index(2)) # index() 함수를 이용한 탐색

def find(arr, num):
    idx = -1
    for i in arr:
        idx += 1
        if num == i:
            return idx
    else:
        return -1
    
print(find(test, 4)) # 2