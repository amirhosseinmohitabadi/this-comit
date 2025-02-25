list = []                  
x=int(input("tedade nomreh :"))

for i in range(x):
    nomarats=(input("nomarat :"))
    list.append(nomarats)
print("nomarat:",list)
list.sort()
print("nomarat_bad",list[:3])
list.sort(reverse=True)
print("nomarat_khoob:",list[:3])