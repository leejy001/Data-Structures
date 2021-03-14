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
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if isEmpty():
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def checkBar(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass

    if isEmpty():
        return True
    else:
        return False

SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    exprArray = ['(A+B)', '((A*A)+(B*B))', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C-D]>)']

    for expr in exprArray:
        top = -1
        print(expr, '==>', checkBar(expr))