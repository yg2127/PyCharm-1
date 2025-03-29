# MAX 힙구조 = 부모노드값이 자식노드값보다 무조건 큰 구조!!

def parent(i):
    return i//2
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2

# 어떤 배열을 MAX 힙구조로 만드는 함수 (A는 배열, i는 힙구조하는 부모노드)
def Max_heapify(A,i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        Max_heapify(A,largest) #부모노드값과 자식노드값을 바꿨다
        # 그럼 자식노드는 힙구조를 만족하는지 또 검사해야하므로 재귀적이므로 heapify!!
def Build_Max_heap(A,n):
    n =len(A)
    for i in range(n//2-1,-1,-1):
        Max_heapify(A,i)
def Heapsort(A,n):
    Build_Max_heap(A,n)
    for i in range(n-1,0, -1):
        A[i],A[0] = A[0],A[i]
        n -= 1
        Max_heapify(A,0,i)

arr = list(map(int, input().split()))
Build_Max_heap(arr,len(arr))
print(arr)
Heapsort(arr,len(arr))
print(arr)