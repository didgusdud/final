def m(i):
    pi=0
    tmp=1
    minus=-1
    k=1
    
    while k<(i+1):
        minus*=-1
        pi+=(minus*1.0)/tmp
        tmp+=2
        k+=1
        
    return 4*pi
    


def main():
    print("{0:s}          {1:s}".format('i','m(i)'))
    print("{0:d}          {1:.4f}".format(1,m(1)))

    for x in range(101,902,100):
        print("{0:d}        {1:.4f}".format(x,m(x)))

if __name__ == "__main__":
    main()
