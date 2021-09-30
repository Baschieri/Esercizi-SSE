#calculator.py


def sum(m,n):
    if n>0:
        for count in range(n): 
            m=m+1
    else:
        for count in range(n):
            m=m-1  
    return m

def divide(m,n):
    i=0

    if(n==0): 
        raise ValueError("Diviso per 0")

    if(n>0):
        while m>=n:
            m=m-n
            i=i+1
    else:
        while m<=n:
            m=m+n
            i=i+1

    return i




    