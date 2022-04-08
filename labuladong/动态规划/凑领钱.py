'''
给你k种面值的硬币，面值分别为c1, c2 ... ck，每种硬币的数量无限，再给一个总金额amount，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1 。
函数签名如下：

// coins 中是可选硬币面值，amount 是目标金额
int coinChange(int[] coins, int amount);
比如说k = 3，面值分别为 1，2，5，总金额amount = 11。那么最少需要 3 枚硬币凑出，即 11 = 5 + 5 + 1。

'''


def coinChange(coins, amount):
    '''
    状态转移方程为, n为需要凑够的零钱总数
    dp(n) = 0 if n=0
    dp(n) = -1 if n<0
    dp(n) = min(dp(i-coin) + 1)|coin -> coins if n>0
    '''
    dp = [amount + 1] * len(amount + 1)  ##定义dp函数，初始值amount + 1为极大值
    dp[0] = 0  ## base case, 凑够0元只需0个硬币
    for i in range(len(dp)):
        for coin in coins:
            if i - coin < 0: continue  ## 子问题无解，i表示需要凑够的钱数
            dp[i] = min(dp[i], dp[i - coin] + 1)  ## min(dp(10)+1, dp(6)+1, dp(3)+1) 举例，i-coin是dp的不同状态
    return dp[-1] if dp[-1] != amount + 1 else -1 ## 如果还是极大值，表示没找到
