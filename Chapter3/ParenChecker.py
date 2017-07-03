from pythonds.basic.stack import Stack

def parChecker(string):
    pStack = Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced:
        cChar = string[index]
        if cChar == "(":
            pStack.push("(")
        elif cChar == ")":
            if pStack.isEmpty():
                return False
            else:
                p = pStack.pop()
        index += 1
    if pStack.isEmpty():
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        s = input()
        print(parChecker(s))






