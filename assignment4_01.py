def calculator(a,b,sign):
    if(sign=="+"):
        return a+b
    elif(sign=="-"):
        return a-b
    elif(sign == "*"):
        return a*b
    elif(sign =="/"):
        return a/b

print(calculator(3,5,"+"))