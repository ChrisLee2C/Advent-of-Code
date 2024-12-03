import re

def main():
    with open('input.txt','r') as f:
        sum=0
        count=0
        isDo=True
        for line in f:
            m=re.search("mul\([0-9]+,[0-9]+\)",line)
            while m:
                m=re.search("do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\)",line)
                if m:
                    print(m[0])
                    if m[0]=="do()":
                        isDo=True
                    elif m[0]=="don't()":
                        isDo=False
                    else:
                        if isDo:
                            a,b=m[0].split("mul")[1].replace("(","").replace(")","").split(",")
                            #print(a,b)
                            sum+=int(a)*int(b)
                            count+=1
                            print(sum)
                    line=line[m.span()[1]:]
        print(sum,count)

if __name__=="__main__":
    main()