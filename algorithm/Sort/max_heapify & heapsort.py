def left(i):
    return 2 * i + 1

def right(i):
    return 2*i + 2

def max_heapify(arr,i,n):
    if left(i) < n and arr[left(i)] > arr[i]:
        largest = left(i)
    else:
        largest = i
    if right(i) < n and arr[right(i)] > arr[largest]:
        largest = right(i)
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr,largest,n)
def Build_max_heap(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        max_heapify(arr,i,n)
def heapsort(arr):
    n = len(arr)
    Build_max_heap(arr)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        n-=1
        max_heapify(arr,0,n)


arr = [5, 2, 7, 6, 0, 8, 3, 4, 9, 1]

Build_max_heap(arr)
print(arr)
heapsort(arr)
print(arr)