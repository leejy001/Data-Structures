import webbrowser
import time

def isFull():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
        return False

def isEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isFull():
        print("Stack is Full!")
        return
    else:
        top += 1
        stack[top] = data

def pop():
    global SIZE, stack, top
    if isEmpty():
        print("Stack is Empty!")
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data

def peek():
    global SIZE, stack, top
    if isEmpty():
        print("Stack is Empty!")
        return None
    return stack[top]

SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    urls = ['naver.com', 'daum.net', 'nate.com']

    for url in urls:
        push(url)
        webbrowser.open('http://'+url)
        print(url, end='-->')
        time.sleep(1)

    print("방문 종료")
    time.sleep(1)

    while True:
        url = pop()
        if url == None:
            break

        webbrowser.open('http://'+url)
        print(url, end='-->')
        time.sleep(1)
    print("방문 종료")