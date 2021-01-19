def palinedrome(value):
    invalue= value[::-1]
    if value==invalue:
        return True
    else:
        return False

value= input()
print(palinedrome(value))