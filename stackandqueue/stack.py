class Stack:

    def __init__(self, size) -> None:
        self.array = [None] * size
        self.top = -1

    def isEmpty(self):
        if self.top < 0:
            return True
        else:
            return False

    def push(self, ele):
        if self.top >= len(self.array) - 1:
            raise IndexError("stack overflow.")

        self.top += 1
        self.array[self.top] = ele

    def pop(self):
        if self.top < 0:
            raise IndexError("stack underflow.")

        self.top -= 1
        return self.array[self.top + 1]

    def size(self):
        return self.top + 1

    def maxSize(self):
        return len(self.array)


if __name__=='__main__':
    stack = Stack(10)
    [stack.push(x) for x in range(1, 11)]
    try:
        stack.push(20)
    except IndexError as e:
        print(e)

    try:
        [print('pop: %s' % stack.pop()) for x in range(stack.top, -1, -1)]
    except BaseException as e:
        print(e)

    try:
        stack.pop()
    except IndexError as e:
        print(e)
