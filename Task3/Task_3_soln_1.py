def odd_sum(L):
    L,Sum=list(L),0
    for num in L:
        if num%2!=0:
            Sum+=num
    return Sum
