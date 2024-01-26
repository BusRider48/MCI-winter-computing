#winter computing contest question 1
#Tyler Wong grade 12
#submitted on:
lock=False
inc=0
solutions=[]
while lock==False:
    n=int(input(print("enter number of pairs of integers")))
    if n<1 or n>pow(10,4):
        print("invalid input")
        lock=True
    while inc<n:
        inp=input(print("enter an integer pair seperated by a space"))
        inp=inp.split(" ")
        a=int(inp[0])
        b=int(inp[1])
        if abs(a>=pow(10,9)) or abs(b>=pow(10,9)):
            print("invalid input")
            lock=True
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
