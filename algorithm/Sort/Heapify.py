def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(arr, n, i):
    largest = i
    l = left(i)
    r = right(i)

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def Build_max_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


arr = [5, 2, 7, 6, 0, 8, 3, 4, 9, 1]
print("초기 배열:", arr)

# 최대 힙 생성
Build_max_heap(arr, len(arr))
print("최대 힙:", arr)