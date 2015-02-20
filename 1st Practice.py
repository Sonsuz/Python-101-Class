Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def square(x):
	return x * x

>>> square(6)
36
>>> square(8)
64
>>> def power(y,t)
SyntaxError: invalid syntax
>>> def power(y,t):
	return y ** t

>>> power(2,4)
16
>>> power(3,4)
81
>>> # "//" bolme isleminde bolum kismini veriyor
>>> 10//2
5
>>> 13//3
4
>>> # "%" bolme isleminde kalan kismini veriyor
>>> 14%4
2
>>> 17%6
5
>>> type(13.0)
<class 'float'>
>>> type(13)
<class 'int'>
>>> type(13j)
<class 'complex'>
>>> # j karmasik sayilardaki i gorevini goruyor
>>> abs(-22)
22
>>> abs(-4)
4
>>> import math
>>> math.sin(0)
0.0
>>> math.sin(180)
-0.8011526357338304
>>> math.sin(math.radians(270))
-1.0
>>> math.trunc(22.30)
22
>>> math.ceil(21.15)
22
>>> math.floor(22.129)
22
>>> math.sqrt(9)
3.0
>>> s1 = berry
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s1 = berry
NameError: name 'berry' is not defined
>>> s1 = "berry"
>>> s2 = "straw"
>>> se = "blue"
>>> s3 = s2 + s1
>>> s3
'strawberry'
>>> s4 = se + s1
>>> s4
'blueberry'
>>> s4[4]
'b'
>>> s4[1:5]
'lueb'
>>> s3[4:8]
'wber'
>>> s4[::3]
'ber'
>>> s3[-4:}
SyntaxError: invalid syntax
>>> s3[-4:]
'erry'
>>> s4.ca
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s4.ca
AttributeError: 'str' object has no attribute 'ca'
>>> s4.capitalize()
'Blueberry'
>>> s4.capitelize(e)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s4.capitelize(e)
AttributeError: 'str' object has no attribute 'capitelize'
>>> s4.capitalize(e)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s4.capitalize(e)
NameError: name 'e' is not defined
>>> s4.capitalize(3)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s4.capitalize(3)
TypeError: capitalize() takes no arguments (1 given)
>>> s4[4]
'b'
>>> 
>>> s5 = s4 + "paste"
>>> s5
'blueberrypaste'
>>> 
