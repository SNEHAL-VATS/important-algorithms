def count_change(money, coins):
    # your implementation here
    w=[1]+[0]*money
    
    w[0]=1
    for i in coins:
        for j in range(i,money+1):
            w[j]+=w[j-i]
    return (w[money])
