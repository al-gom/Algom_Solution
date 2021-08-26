import sys

sys.stdin = open("input.txt", "rt")
n = int(input())
dp = [0] * (n + 1)
arr = [0] + list(map(int, input().split()))
dp[1] = arr[1]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        if dp[i] < dp[i - j] + arr[j]:
            dp[i] = dp[i - j] + arr[j]
print(dp[n])
