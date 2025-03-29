m = int(input()) # 상자 당 귤 개수
n = int(input()) # 총 귤의 개수
arr = []
price = []
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
if n // m == 1:
    print(m * arr[m-1])
else:
    for i in range(n // m):
        price.append(m * arr[i*m - 1])
    print(sum(price))