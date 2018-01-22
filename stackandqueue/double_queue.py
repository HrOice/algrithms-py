class DoubleQueue:
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.array = [None] * maxSize
        self.left = maxSize // 2
        self.right = maxSize //2 + 1
        self.size = 0

    def left_push(self, ele):
        if self.size == self.maxSize:
            raise IndexError("stack overflow")
        self.array[self.left - 1] = ele
        if self.left == 1:
            self.left = self.maxSize
        else:
            self.left -= 1
        self.size += 1
        return True
    def left_pop(self):
        if self.size == 0:
            raise IndexError("stack underflow")
        ele = self.array[self.left]
        if self.left == self.maxSize:
            self.left = 1
        else:
            self.left += 1
        self.size -= 1
        return ele

    def right_push(self, ele):
        if self.size == self.maxSize:
            raise IndexError("stack underflow")
        self.array[self.right - 1] = ele
        if self.right == self.maxSize:
            self.right = 1
        else:
            self.right += 1
        self.size += 1
        return True


    def right_pop(self):
        if self.size == 0:
            raise IndexError("stack underflow")
        ele = self.array[self.right - 2]
        if self.right == 0:
            self.right = self.maxSize
        else:
            self.right -= 1
        self.size -= 1
        return ele

    def __size__(self):
        return self.size

if __name__ == '__main__':
    doubleQueue = DoubleQueue(10)
    [print(doubleQueue.left_push(x)) for x in range(1,8)]
    [print(doubleQueue.right_push(x)) for x in range(8,11)]
    try:
        doubleQueue.left_push(55)
    except IndexError as e:
        print(e)

    [print('rightPop: %s'%doubleQueue.right_pop()) for x in range(1, 11)]
    try:
        print(doubleQueue.left_pop())
    except IndexError as e:
        print(e)