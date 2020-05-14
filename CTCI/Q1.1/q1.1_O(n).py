def isUnique(str):
    arr=[False]*128
    #Bonus pts...converts it to const time.
    if(len(str)>128):
        return False
    for char in str:
        if(arr[ord(char)]):
            return False
        arr[ord(char)] = True
    return True

print(isUnique("yolo")== False)
print(isUnique("rad")== True)
print(isUnique("yolO")== True)
