def printPoly(t_x, p_x):
    polyStr = "P(x) = "

    for i in range(len(p_x)):
        term = t_x[i]
        coef = p_x[i]

        if coef >= 0:
            polyStr += "+"

        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr

def calcPoly(xVal, t_x, p_x):
    retValue = 0

    for i in range(len(px)):
        term = t_x[i]
        coef = p_x[i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue

tx = [300, 20, 0]
px = [7, -4, 5]

if __name__ == "__main__":
    pStr = printPoly(tx, px)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, tx, px)
    print(pxValue)


# -------- 2차원 배열 -----------
def printPoly(p_x):
    polyStr = "P(x) = "

    for i in range(len(p_x[0])):
        term = p_x[0][i]
        coef = p_x[1][i]

        if coef >= 0 and i != 0:
            polyStr += "+"

        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr

def calcPoly(xVal, p_x):
    retValue = 0

    for i in range(len(px[0])):
        term = p_x[0][i]
        coef = p_x[1][i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue

px = [[300, 20, 0],[7, -4, 5]]

if __name__ == "__main__":
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, px)
    print(pxValue)