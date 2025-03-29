n = int(input("enter the number of arrays"))
arr = []

for i in range(n):
    arr.append(int(input()))

c = int(input("select your algorithm\n1 = Selection\n2 = Insertion\n3 = Merge\n4 = Heap\n"))



def selection_rsort(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def insertion_rsort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while(j >= 0 and a[j] < key):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            j += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def merge_rsort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_rsort(left_half)
        merge_rsort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

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


def Build_max_heap(arr):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)

def heapify1(arr, n, i):
    smallest = i
    l = left(i)
    r = right(i)

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify1(arr, n, smallest)


def Build_min_heap(arr):
    for i in range(n // 2 - 1, -1, -1):
        heapify1(arr, len(arr), i)

c2 = int(input("enter the sorting array is ascending or discending\n1 = ascending\n0 = discending"))

if c2 == 0:
    if c == 1:
        selection_rsort(arr)
        print(arr)
    elif c == 2:
        insertion_rsort(arr)
        print(arr)
    elif c == 3:
        merge_rsort(arr)
        print(arr)
    elif c == 4:
        Build_max_heap(arr)
        print(arr)
elif c2 == 1:
    if c == 1:
        selection_sort(arr)
        print(arr)
    elif c == 2:
        insertion_sort(arr)
        print(arr)
    elif c == 3:
        merge_sort(arr)
        print(arr)
    elif c == 4:
        Build_min_heap(arr)
        print(arr)

import time
import matplotlib.pyplot as plt

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

sel_t = measure_time(selection_sort,arr)
ins_t = measure_time(insertion_sort,arr)
mer_t = measure_time(merge_sort,arr)
hea_t = measure_time(Build_max_heap,arr)

algorithms = ['Selection Sort', 'Insertion Sort', 'Merge Sort', 'Heap Sort']
times = [sel_t, ins_t, mer_t, hea_t]

# 그래프 그리기
plt.figure(figsize=(8, 6))
plt.bar(algorithms, times, color='skyblue')  # 막대 그래프 생성
plt.xlabel('Sorting Algorithms')             # x축 레이블
plt.ylabel('Time (seconds)')                 # y축 레이블
plt.title('Comparison of Sorting Algorithms Execution Time')  # 그래프 제목

# 그래프 보여주기
plt.show()