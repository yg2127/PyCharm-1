a = int(input())
arr = []
for i in range(a):
    arr.append(int(input()))
# arr = [5,3,10]일 때
for i in range(1,a):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] > key: # 반복문을 통해 i번째 값을 작은값보다 뒤로 보내는 중이다.
        arr[j+1] = arr[j] # 한칸씩 앞으로 땡기기 (뒤로 미는게 아니라 앞으로 땡긴다고?)
        j -= 1 #ㅇㅇ j--니까
    arr[j+1] = key # 젤 뒤에는 원래 갖고있던 arr[i]값이 들어간다.

print(arr)