lock=False
inc=0
solutions=[]
while lock==False:
    n=int(input())
    while inc<n:
        inp=input()
        inp=inp.split(" ")
        a=int(inp[0])
        b=int(inp[1])
        if a>b:
            solutions.append(int(a/b))
        elif b>a:
            solutions.append(int(b/a))
        elif a==b:
            solutions.append(1)
        inc+=1
    for x in solutions:
        print(x)
        lock=True
