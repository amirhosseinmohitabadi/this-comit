numbers=[]
a =(input("number :"))
numbers=a.split(",")
print(numbers)
max_num=None
min_num=None
for i in numbers:
    if max_num==None or min_num==None:
        max_num=i
        min_num=i
    elif max_num < i :
        max_num=i
    elif min_num > i:
        min_num=i
print("max:",max_num)
print("min:",min_num)