import re

def main():
    with open('input.txt','r') as f:
        sum=0
        count=0
        for line in f:
            m=re.findall("mul\([0-9]+,[0-9]+\)",line)
            print(m)
            for mul in m:
                print(mul)
                a,b=mul.split("mul")[1].replace("(","").replace(")","").split(",")
                print(a,b)
                sum+=int(a)*int(b)
                count+=1
                print(sum)
        print(sum,count)

if __name__=="__main__":
    main()