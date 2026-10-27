def primedetector(x):
        isprime = x >= 2
        for i in range(2,x):          
            if x%i == 0:
                isprime=False
                break
        return isprime

        
            
for x in range(0,1001):
    if primedetector(x) == True:
        print(x)



    