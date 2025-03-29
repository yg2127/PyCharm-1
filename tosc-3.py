n, m, l = map(int, input().split())
n_pac = 1
m_pac = 1
l_pac = 1

for i in range(1, n+1):
    n_pac *= i
for i in range(1, m+1):
    m_pac *= i
for i in range(1, l+1):
    l_pac *= i

pac = 6*5*4*3*2*1

count = pac // n_pac // m_pac // l_pac
print(count)

