list[]:
When we go for list data type ?
if you want to represent a group of objects as a single entity where 
insertion orser is preserved and 
duplicates are allowd 
hetogeneous objects are allowd 
dynamic in nature ..!!Based on our requirement we can increase and decrease the element
List is mutable 

Any type of value like init,str,float No problem at all , if you want represent we need to use squre bracket 
[]  ====> list
()  ====> tuple
{}  ====> set 
{k:v,k:v} ===> dict 

Ex:

l=[10,20,'senthil',10,30,True]
print(l[0])
print(l[1])
print(l[-1])
print(l)


l=[]
l.append(10)
l.append(20)
l.append('senthilveeranan')
l.append(None)
l.append(True)
l.append(10)
l.append('sivasakthithunai')
l.append(123.456)
print(l)
print(id(0))
print(id(5))
print(len(l))
print(id(l))


list is mutable below are the example 

l=[10,20,30]
l[0]=777
print(l)





































