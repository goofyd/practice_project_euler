def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    for s in set(ar):
        pairs+=ar.count(s)//2
    return pairs

if __name__ == '__main__':
    arr = "4 5 5 5 6 6 4 1 4 4 3 6 6 3 6 1 4 5 5 5"
    nn = len(arr)

    n = int(nn)

    ar = list(map(int, arr.rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)