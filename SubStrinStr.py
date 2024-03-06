#usin if else
String = "A geek in need is a geek indeed"
Substring ="kjs"
if Substring in String:
	print("Yes it is present in the string")
else:
	print("No it is not present")

# Take input from users
String = input("enter string")
Substring = input("Enter substring")
if Substring in String:
	print("Yes it is present in the string")
else:
	print("No it is not present")
 
 
 
 
 
 # Using contains
 #__contains__
a=['we','shall','eradicate','all','humanity']
i="eradicate"
#for i in a:
if a .__contains__  (i):
        print( "present")
else:
        print ("not present")
        
        
        
 
 #regular expression
import re
mystr1 ="we are se stud"
if  re.search("SE",mystr1):
 print("present")
else:
    print ("not found")