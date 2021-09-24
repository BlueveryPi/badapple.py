import sys, time, os
import zipfile
from colorama import init
init()

if os.path.exists((os.path.dirname(__file__)).replace("\\", "/")+"/badapple copy.txt"):
    f=open((os.path.dirname(__file__)).replace("\\", "/")+"/badapple copy.txt", "r+", encoding='utf-8')
else:
    with zipfile.ZipFile((os.path.dirname(__file__)).replace("\\", "/")+"/badapple copy.zip", 'r') as zip_ref:
        zip_ref.extractall((os.path.dirname(__file__)).replace("\\", "/"))
    f=open((os.path.dirname(__file__)).replace("\\", "/")+"/badapple copy.txt", "r+", encoding='utf-8')
    print("Files are ready. Please restart the program.")
    sys.exit()

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