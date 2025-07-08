def catalan_recursive(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_recursive(i) * catalan_recursive(n-i-1)
    return res