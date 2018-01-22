### 如果
class Queue:

    def __init__(self, size) -> None:
        if not isinstance(size, int):
            raise TypeError('size must be int.')
        self.array = [None] * size
        self.head = None
        self.tail = 0

    def enqueue(self, ele):
        head, tail, array = self.head, self.tail, self.array
        if tail == head:
            raise IndexError('queue overflow')
        array[tail] = ele

        if head == None:
            self.head = tail

        if tail == len(array) - 1:
            self.tail = 0
        else:
            self.tail += 1
        return self.size()

    def dequeue(self):
        head, tail, array = self.head, self.tail, self.array
        if head == None:
            raise IndexError('queue underflow')

        ele = array[head]
        if head == len(array) - 1:
            self.head = 0
        else:
            self.head += 1

        if self.head == tail:
            self.head = None

        return ele

    def size(self):
        head, tail, array = self.head, self.tail, self.array
        return len(array) - head  + tail if tail <= head else tail - head

if __name__=='__main__':
    print("start")
    queue = Queue(10)
    [print('size: %s'%queue.enqueue(x)) for x in range(1, 11)]
    try:
        queue.enqueue(11)
    except IndexError as e:
        print(e)

    [print('dequeue: %s'%queue.dequeue()) for x in range(queue.size(), 0, -1)]
    print(queue.head, queue.tail)
    try:
        queue.dequeue()
    except IndexError as e:
        print(e)