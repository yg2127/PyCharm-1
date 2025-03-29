def Merge_sort(A,p,r): #p는 시작하는 인덱스 r은 끝 인덱스 맨 처음에는 0, len(A)-1
    if p >= r:
        return
    q = (p+r)//2
    Merge_sort(A,p,q)
    Merge_sort(A,q+1,r)
    Merge(A,p,q,r)
# MergeSort에서는 계속 나눠서 p와r을 1차이가 날 때까지 나눈다.(1개단위까지)
# 그리고 1개단위가 되었을 때 이제 Merge, 병합과정을 시작한다!
# 그럼 밑의 Merge함수는 1단위의 함수들을 병합하기 시작한다!

#아 진짜 존나어렵네 내가 지금 피곤해서 그러는거 아니지? ㅈㄴ어려운거 맞지?
def Merge(A,p,q,r):
    nl = q-p+1
    nr = r-q
    L = [0]*nl
    R = [0]*nr
    for i in range(0,nl):
        L[i] = A[p+i]
    for i in range(0,nr):
        R[i] = A[q+i+1]
    i = 0
    j = 0
    k = p

    while i < nl and j < nr:
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k+=1
    while i < nl:
        A[k] = L[i]
        i+=1
        k+=1
    while j < nr:
        A[k] = R[j]
        j+=1
        k+=1

arr = list(map(int, input().split()))
Merge_sort(arr,0,len(arr)-1)
print(arr)