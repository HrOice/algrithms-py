from stackandqueue.stack import Stack

class DoubleStackQueue:
    def __init__(self) -> None:
        self.s1 = Stack(100)
        self.buffer = Stack(100)

    def enqueue(self, ele):
        self.s1.push(ele)

    def dequeue(self):
        if self.buffer.isEmpty():
            while self.s1.size() > 0:
                self.buffer.push(self.s1.pop())
        if self.s1.isEmpty() and self.buffer.isEmpty():
            raise IndexError("overflow")
        return self.buffer.pop()

    def size(self):
        return self.buffer.size() + self.s1.size()


if __name__=='__main__':
    dsq = DoubleStackQueue()
    [dsq.enqueue(x) for x in range(1, 51)]
    [print(dsq.dequeue()) for x in range(dsq.size(), 0, -1)]