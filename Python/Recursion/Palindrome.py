def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:len(s)-1])

strArray = ["reaver", "kayak", "Borrow or rob", "주유소의 소유주", "야 너 이번 주 주번이 너야", "살금 살금"]

if __name__ == "__main__":
    for s in strArray:
        print(s, end='-->')
        s = s.lower().replace(' ', '')
        if palindrome(s):
            print('O')
        else:
            print('X')