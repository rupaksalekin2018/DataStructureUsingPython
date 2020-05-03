class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items:
            return False
        else:
            return True

    def insert(self,element):
        self.items.append(element)

    def out(self):
        if(self.isEmpty() == False):
            return self.items.pop()
        else:
            pass

    def peek(self):
        #returns the last element from the Stack
        if self.isEmpty() == False:
            return self.items[-1]
        else:
            pass

    def allItems(self):
        if self.isEmpty() == False:
            return self.items
        else:
            pass

def checkBalance(str):

    openers = ['(','{','[']
    bracketPairs = {
        "(":")",
        "{":"}",
        "[":"]",
    }
    stack = Stack()
    i = 0
    while i<len(str):
        symbol = str[i]
        if symbol in openers:
            stack.insert(symbol)
        else:
            if stack.isEmpty():
                return False
            else:
                top_item = stack.out()
                if symbol == bracketPairs[top_item]:
                    pass
                else:
                    return False
        i=i+1
    if(stack.isEmpty()):
        return True

str = '([{{}}])'
str2 = '((([)))'
value = checkBalance(str)
value2 = checkBalance(str2)
print(value)
print(value2)
