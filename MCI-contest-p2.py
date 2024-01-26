inc=2
inp=int(input())
isPrime=True
if inp==1:
    isPrime=False
while inc<inp:
    if inp%inc==0:
        isPrime=False
    inc+=1
print(isPrime)
