def partition(array, p, r):
    mid = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= mid:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    print(array)
    return i + 1

def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


array = [2, 8, 7, 1, 3, 5, 6, 4]

if __name__=='__main__':
    quick_sort(array, 0, len(array) - 1)
    print(array)