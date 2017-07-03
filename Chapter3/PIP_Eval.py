from pythonds.basic.stack import Stack

class InfixToPostfix:
    PREC = {
        "*" : 2,
        "/" : 2,
        "+" : 1,
        "-" : 1,
        "(" : 0
    }
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUM = "0123456789"
    def __init__(self, e = ""):
        self.tokenList = e.split()
        self.opStack = Stack()

    def convert(self):
        finalList = ""
        for token in self.tokenList:
            if token in InfixToPostfix.ALPHA or token in InfixToPostfix.NUM:
                finalList += token
            elif token == "(":
                self.opStack.push(token)
            elif token == ")":
                while self.opStack.peek() !=  "(":
                    finalList += self.opStack.pop()
                self.opStack.pop()
            elif token in InfixToPostfix.PREC.keys():
                while not self.opStack.isEmpty() and InfixToPostfix.PREC[token] < InfixToPostfix.PREC[self.opStack.peek()]:
                    finalList += self.opStack.pop()
                self.opStack.push(token)
        while not self.opStack.isEmpty():
            finalList += self.opStack.pop()
        return " ".join(finalList)
    def setExpress(self, e):
        self.tokenList = e.split()
    def retrieveExpress(self):
        return " ".join(self)
if __name__ == "__main__":
    tester = InfixToPostfix("")
    while True:
        s = input()
        tester.setExpress(s)
        print(tester.convert())


