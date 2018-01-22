# 最大化某个节点,
# array 堆数组
# size  当前数组有效长度
# i     要最大化的节点编号，不是数组下标
def max_heapify(array, size, i):
    left = 2 * i
    right = left + 1
    if left <= size and array[i - 1] < array[left - 1]:
        largest = left
    else:
        largest = i

    if right <= size and array[largest - 1] < array[right - 1]:
        largest = right

    if largest != i:
        array[largest - 1], array[i - 1] = array[i - 1], array[largest - 1]
        max_heapify(array, size, largest)

# 建立最大堆
# i 最大化堆的节点编号
def build_max_heap(array):
    size = len(array)
    for i in range(size // 2, 0, -1):
        max_heapify(array, size, i)

def heap_sort(array):
    size = len(array)
    build_max_heap(array)
    for i in range(size, 1, -1):
        array[0], array[i - 1] = array[i - 1], array[0]
        size -= 1
        max_heapify(array, size, 1)

if __name__=='__main__':
    array = [16,4,10,14,7,9,3,2,8,1,22,0,-3]
    # max_heapify(array, 2)
    heap_sort(array)
    print(array)