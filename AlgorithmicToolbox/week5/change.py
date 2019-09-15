import sys

def DPchange(money, coins):
    MinNumCoins = [0] * (money+1)
    for m in range(1, money+1):
        MinNumCoins[m] = sys.maxsize
        for coin in coins:
            if m >= coin:
                change = MinNumCoins[m-coin] + 1
                if change < MinNumCoins[m]:
                    MinNumCoins[m] = change
    return MinNumCoins[money]



def RecursiveMinNumCoins(m, coins):
    if m == 0:
        return 0
    minNum = sys.maxsize
    for coin in coins:
        if m >= coin:
            change = RecursiveMinNumCoins(m-coin, coins)
            if change+1 < minNum: 
                minNum = change+1
    return minNum




if __name__ == "__main__":
    m = int(sys.stdin.read())
    coins = [1,3,4]
    print(DPchange(m, coins))
    