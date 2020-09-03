#int==> Without having decimal point is called "int" type , how large it is no worries
#float==> Noumber with decimal point is consider as float(doller,desiel price)
#bool==>True / False are only allowd values
#complex==> 10+20j is complex numbers
#str==> Any sequance of charector with in single or doucble quote is called "str"
#driple quotes are allowd where-> to define multiline leterals
#to use single qoutes and double quotes as symbol then we can use triple quotes

#in python how you can access of the charector of the string?
#python supports 
#+ve index--0,1,2,3, 
#-ve index ---1,-2,-3

#slice operator:
#slice operator is applicable only in python 
#slice means pice 
#slice always going to consider bgin and end-1 
#slice operator never through error

# Always slice will give begin:end-1 is the concept
# slice never gives error always 
s='abcdefghij'
print(s[2:6])
# slice operator never gives error if you put 100 always consider begin to last vlaue give as aswer
# in java substring method is there for the same
print(s[2:100])
# suppose if you want to display total value we can use the below 
print(s[:])

# if i dont want begin 
print (s[:6])

#s[begin:end:step]
# begin alsways starts from 0(zero) end value always (end-1)
# the default value of step value is 1  
# example:
s2='abcedfghijklmnopqrtuvwxyz'
s2[2:15]
#Here 2 means c and 8 means 7 , 7 is h so the answer would be cdefgh
s2[2:15:2]
s2[2:15:3]
s2[::1]

# can you please reverse the sting ,,,very very important in interview.

s2[::-1]

# long data type:
# python 2 not in python 3 

# char data type is not available in python 
ch='a'
type(ch)
chat data type is availble in java and c langauge 


