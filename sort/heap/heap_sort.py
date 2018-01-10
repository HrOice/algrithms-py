def max_heapify(array, i):
    left = 2 * i
    right = 2 * i + 1

    if left - 1 <= len(array) and array[i - 1] < array[left - 1]:
        largest = left
    else:
        largest = i

    if right <= len(array) and array[largest - 1] < array[right - 1]:
        largest = right

    if largest != i:
        array[largest - 1], array[i - 1] = array[i - 1], array[largest - 1]
        max_heapify(array, largest)

if __name__=='__main__':
    array = [16,4,10,14,7,9,3,2,8,1]
    max_heapify(array, 2)
    print(array)
