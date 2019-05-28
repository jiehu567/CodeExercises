class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.minStack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if len(self.minStack) == 0:
            self.minStack.append(number)
        else:
            self.minStack.append(min(number, self.minStack[-1]))

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        tmp = self.stack[-1]
        del(self.stack[-1], self.minStack[-1])
        return tmp
    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.minStack[-1]