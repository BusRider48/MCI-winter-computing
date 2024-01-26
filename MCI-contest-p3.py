inp=input()
doubleFlag=False
x=0
total=0
while x<len(inp):
    if doubleFlag==True:
        doubleFlag=False
        x+=1
        continue
    elif inp[x]=="M":
        total+=1000
        x+=1
    elif inp[x]=="D":
        total+=500
        x+=1
    elif inp[x]=="C":
        if x+1 < len(inp) and inp[x+1]=="M":
            total+=900
            doubleFlag=True
            x+=1
        elif x+1 < len(inp) and inp[x+1]=="D":
            total+=400
            doubleFlag=True
            x+=1
        else:
            total+=100
            x+=1
    elif inp[x]=="L":
        total+=50
        x+=1
    elif inp[x]=="X":
        if x+1 < len(inp) and inp[x+1]=="C":
            total+=90
            doubleFlag=True
            x+=1
        elif x+1 < len(inp) and inp[x+1]=="L":
            total+=40
            doubleFlag=True
            x+=1
        else:
            total+=10
            x+=1
    elif inp[x]=="V":
        total+=5
        x+=1
    elif inp[x]=="I":
        if x<len(inp)-1:
            if inp[x+1]=="X":
                total+=9
                doubleFlag=True
                x+=1
            elif inp[x+1]=="V":
                total+=4
                doubleFlag=True
                x+=1
            else:
                total+=1
                x+=1
        else:
            total+=1
            x+=1
print(total)
