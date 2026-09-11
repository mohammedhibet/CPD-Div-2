n = int(input())
tot_solu = 0
for i in range(n):
    solu = 0
    P,V,T = map(int, input().split())
    if P == 1:
        solu += 1
    if V == 1:
        solu += 1
    if T == 1:
        solu += 1
    if solu > 1:
        tot_solu += 1
print(tot_solu)
