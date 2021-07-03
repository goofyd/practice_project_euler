def jumpingOnClouds(c):
    jump = 0
    i=0
    while(i<len(c)-2):
        if c[i]==0 and c[i+2]==0:
            jump+=1
            i+=2
        elif c[i]==0 and c[i+1] == 1:
            jump+=1
            i+=2
        elif c[i]==0 and c[i+2] == 1:
            jump+=1
            i+=1
        else:
            i+=1

    return jump


if __name__ == '__main__':

    cc = "0 0 0 0 1 0"

    nn = len(cc)

    n = int(nn)

    c = list(map(int, cc.rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result))
