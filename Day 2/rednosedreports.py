def isDecreasing(level):
    prev=level[0]
    for i in range(1,len(level)):
        diff=prev-level[i]
        print(diff)
        if prev<=level[i] or diff<=0 or diff>3:
            return False
        prev=level[i]
    return True

def isIncreasing(level):
    prev=level[0]
    for i in range(1,len(level)):
        diff=level[i]-prev
        print(diff)
        if prev>=level[i] or diff<=0 or diff>3:
            return False
        prev=level[i]
    return True

def isSafe(level):
    isIncrease=False
    isDecrease=False
    print("isIncrease")
    isIncrease=isIncreasing(level)
    print(isIncrease)
    print("isDecrease")
    isDecrease=isDecreasing(level)
    print(isDecrease)
    if isIncrease or isDecrease:
        global safe
        safe+=1
        return True
    else:
        return False

def main():
    with open('input.txt','r') as f:
        global safe
        safe=0
        for line in f:
            level=list(map(int,line.split()))
            isSafe(level)
        f.close()
    print(safe)

if __name__=="__main__":
    main()