
# Always slice will give begin:end-1 is the concept

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
# the default value of step value is 1