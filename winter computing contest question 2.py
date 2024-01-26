#winter computing contest question 2
#Tyler Wong grade 12
#submitted on:
inc=2
inp=int(input(print()))
isPrime=True
if inp==1:
    isPrime=False
while inc<inp:
    if inp%inc==0:
        isPrime=False
    inc+=1
print(isPrime)
