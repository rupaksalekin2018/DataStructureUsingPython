class Stack(object):
    # to hold all the elements in the list
    # filo first-in-last-out
    def __init__(self):
        self.stackList = []
    def isEmpty(self):
        if(self.stackList == []):
            return True
        else:
            return False
    def push(self, element=""):
        self.stackList.append(element)
        pass

    def pop(self):
        if self.stackList:
            self.stackList.pop()
            pass
        else:
            return None

    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return None

    def allElements(self):
        return self.stackList

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.allElements())
    stack.pop()
    print(stack.allElements())
    print(stack.peek())
    # stack.pop()
    print(stack.isEmpty())
