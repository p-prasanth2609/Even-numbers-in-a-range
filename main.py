A = list(map(int, input().split()))
q = int(input())
B = []
output=[]

for i in range(q):
    l, r = map(int, input().split())
    B.append([l, r])
p = [0] * len(A)
p[0] = 1 if A[0] % 2 == 0 else 0

for i in range(1, len(A)):
    p[i] = p[i - 1] + (1 if A[i] % 2 == 0 else 0)

for query in B:
    l, r = query
    if l == 0:
        output.append(p[r])
    else:
        output.append(p[r] - p[l - 1])

print(output)
