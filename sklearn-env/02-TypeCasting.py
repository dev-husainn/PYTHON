# ------------------------------------- - ------------------------------------ #

# typecasting - the conversion of one data type into the other datatype is know as type casting in python .

# int() , float() , str(), ord() , hex() , oct() , tuple() , set() , list() , dict() , etc for type casting.


# ------------------------------------- - ------------------------------------ #

#1.Explicit conversion = the conversion of data type from one to another done by the developers is explicit conversion.
a = "1"
b = "2"
print(a+b) #here the output will be 12 bcoz here two strings are concateneted.
print (int(a) + int(b)) # here int() typecast the string to the integer so the output wil be 3.

# ------------------------------------- - ------------------------------------ #

# c = "1husain"
# d = "ahmad"
# print(int(c) + int(d)) #here it will be error coz we neither have proper int or string in the  c.


# ------------------------------------- - ------------------------------------ #

#2.Implicit conversion == when one data type converted into other by the python interpreter itself this is called implicit conversion.
num = 1.9
num2 = 9
print(num + num2) #this is implicit conversion here O/P will be 10.9 (automatically a float value) here we did'nt have passed any method.

