def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return i // 2


def heapify(arr, n, i):
    if (left(i) < len(arr) and arr[left(i)] > arr[i]):
        largest = left(i)
    else:
        largest = i
    if (right(i) < len(arr) and arr[right(i)] > arr[i]):
        largest = right(i)
        #왜 위의 if문에서 바로 바꾸지 않는걸까?
        #부모 (i)에서 자식(LEFT,RIGHT중 더 작은 아이)로 바꾼 후
        #그 바꾼 자식도 해당 요소의 자식과 비교해야하기 때문에 그 i를 특정해 줘야한다.
        #그 특정하는 변수의 이름을 largest로 해놓은 것이다.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def Build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)


arr = [5, 2, 7, 6, 0, 8, 3, 4, 9, 1]

i = 0
print(arr)
heapify(arr, len(arr), 0)
print(arr)
Build_max_heap(arr)
print(arr)