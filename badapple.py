import sys, time, os
from colorama import init
init()

f=open((os.path.dirname(__file__)).replace("\\", "/")+"/badapple copy.txt", "r+", encoding='utf-8') 
l=f.readlines()

for i in range(len(l)):
    a=l[i]
    a=a[:len(a)-3]
    a=a.split("\\n")
    t=""
    for k in range(len(a)-1):
        t+=a[k]+"\n"
    t+=a[k+1]+"\n"
    print(t, end="")
    #sys.stdout.write(t)
    time.sleep(1/30)
    if i!=len(l)-1:
        for k in range(len(a)):
            sys.stdout.write('\033[A')