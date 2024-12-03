def main():
    with open('input.txt','r') as f:
        left=[]
        right=[]
        sum=0
        lineCount=0
        print("Start File")
        for line in f:
            l,r=line.split()
            lineCount+=1
            left.append(int(l))
            right.append(int(r))
            print(lineCount,l,r)
        print("End File")
        left.sort()
        right.sort()
        print(left,right)
        for i in range(lineCount):
            print(left[i],right[i])
            sum+=abs(left[i]-right[i])
        print(sum)
        f.close()

if __name__=='__main__':
    main()