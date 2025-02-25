def nomreh(m):
    dic={}
    for i in range(m):
        x = input("name:")
        y= input("nomreh:")
        i+=1
        dic.update({x:y})
    return dic


def khoob(max):
    list=[]
    for j in max.valeus():
        list.append(j)
        
        return list   



m=int(input("chand nafar?"))
max=nomreh(m)
print(max)
print(khoob(max))
