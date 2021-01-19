def outerfunc(a,b):
    
    def innerfunc():
        sum=a+b
        return sum
    moresum = innerfunc()+8   
    return moresum
result = outerfunc(5,10)
print(result)