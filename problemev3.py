s = input()
count_one = 0
dp = [0] * (len(s)+1)
for i in range(len(s)):
    if s[i] =='0':
        dp[i+1] = min(count_one,dp[i]+1)
    else:
        count_one+=1
        dp 