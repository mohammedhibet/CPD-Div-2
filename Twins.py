n = int(input())
nums = list(map(int,input().split()))
sum_nums = 0
num_no = 0
for i in range(n):
    sum_nums += max(nums)
    nums.remove(max(nums))
    num_no += 1
    total = sum(nums)
    if sum_nums > total:
        break
print(num_no)
