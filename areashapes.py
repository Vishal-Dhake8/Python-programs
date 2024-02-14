#area
while(1):
     print("1.rectangle \n 2.triangle \n 3.circle \n4. exit")
     ch=int(input("enter ur choice:"))

     if ch is 1:
        print("area of rectangle")
        l=float(input("length:"))
        b=float(input("breadth:"))
        a=float(l*b)
        print(a)
     elif ch is 2:
        print("area of trianglr")
        l=float(input("length:"))
        h=float(input("height:"))
        a=float(0.5*l*b)
        print(a)
     elif ch is 3:
        print("area of circle")
        r=float(input("radius:"))
        area=float(3.14*r)
        print(area)
     elif ch is 4:
        exit(0)
     elif (ch>4):
        print("wrong choice")
