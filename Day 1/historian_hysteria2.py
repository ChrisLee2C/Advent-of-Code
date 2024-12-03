def main():
    with open('input.txt','r') as f:
        left=[]
        right={}
        sum=0
        lineCount=0
        print("Start File")
        for line in f:
            l,r=line.split()
            lineCount+=1
            left.append(int(l))
            if int(r) not in right:
                right[int(r)]=1
            else:
                right[int(r)]+=1
            print(lineCount,l,r)
        print("End File")
        print(left,right)
        for i in range(lineCount):
            if left[i] in right:
                print(left[i],right[left[i]])
                sum+=left[i]*right[left[i]]
        print(sum)
        f.close()

if __name__=='__main__':
    main()