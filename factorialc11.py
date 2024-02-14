print("enter no to print factorial:")
num=int(input("number:"))
if num is 1:
    print("factorial of one is 1")
elif num < 0:
    print(" no fact for negative no")

else:
    fact=1
    for i in range(1,num+1):
        fact=int(fact*i)
    print("fact is:",+fact)
    
