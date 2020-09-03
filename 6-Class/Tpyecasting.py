# Type casing: 
if you want to convert from one type to another we can use some functions like the below(type coersion) 

int() -- > if you want to convert anytype to int we can use int function 
float()
complex()
str()
bool()

init():

int(123.987)===change float to init here 
int(10+20j)=== change complex to int ...not possible  
int(True)  == pssible internally True mans 1 False means 0 
int('10')  == We can convert str to int ...string to int is possible only string contains integral 
value and shuld be base 10 
int('10')
int('0B10')
int('21')
int('1234')
int('True')
int("10.5")
int(10.5)
We can converty any type of int type except complex type 
we can convert to str type to int type str should be integral literal should be base-10

float():

We can convert any type to float except complex type 
when we convert str to float value str should be integral value and should be base-10
float('10')
float(True)
float('123.456')
float('0B111')

complex():
complex(x)
With One argument:
here if you specified only one argument x will be treaded as real part and imaginary part will 
be taken by defaul as 0
complex(10)
complex(True)
complex(10.5)
complex('0B111')===invalied 

With Two arguments:
complex(x,y)   -- can you please tell which is real part and which is imaginary part ?
x is real and y is imaginary 
complex(10,20)
complex(True,False)
complex('10120','334324234')
complex(10120,334324234)

bool(): 
Anytype to bool is possible 
we can use bool function to convert other function to bool 
zero means False no-zoro means True is the basic concept 
bool(0)
bool(123)
bool('senthil')
bool('0')
bool(0)
bool(123.456)
bool(000.000)
bool(000.001)  - not-zero mans True 
bool(10+20j)
bool(0+0j)  
bool('')  - if it is empty string the result is always False , non-empty the resule it True
bool('False')


str():
str is universal we can change all to str 
str of anything the result is always same







