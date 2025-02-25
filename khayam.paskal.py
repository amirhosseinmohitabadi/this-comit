n = int(input("enter a number:"))

for i in range(n+1):
    s=n-i
    k=2*i-1
    print(" "*s,end="")
    print("*"*k)
print()