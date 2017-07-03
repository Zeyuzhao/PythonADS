from pythonds.basic.stack import Stack

class BracketChecker:
    bracketOpen = ["[", "{", "("]
    bracketClose = ["]", "}", ")"]
    def __init__(self, s = ""):
        self.bStack = Stack()
        self.str = s

    def store(self, s):
        i = BracketChecker.bracketOpen.index(s)
        if s != -1:
            self.bStack.push(i)

    def retrieve(self, s):
        i = BracketChecker.bracketClose.index(s)
        if s != -1:
            currentB = self.bStack.pop()
            if currentB == i:
                return True
        return False
    def bracketCheck(self):
        index = 0
        balanced = True
        while index < len(self.str) and balanced:
            currentChar = self.str[index]
            if currentChar in BracketChecker.bracketOpen:
                self.store(currentChar)
            elif currentChar in BracketChecker.bracketClose:
                if not self.bStack.isEmpty():
                    retVal = self.retrieve(currentChar)
                    if not retVal:
                        balanced = False
                else:
                    balanced = False
            index += 1
        if balanced and self.bStack.isEmpty():
            return True
        else:
            return False
    def getString(self):
        return self.str
    def setString(self, s):
        self.str = s

if __name__ == "__main__":
    tester = BracketChecker("")
    while True:
        s = input()
        tester.setString(s)
        print(tester.bracketCheck())

