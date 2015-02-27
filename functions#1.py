Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def convert_to_celcius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9

>>> convert_to_celcius(75)
23.88888888888889
>>> convert_to_celcius(0)
-17.77777777777778
>>> def convert_to_fahrenheit:
	
SyntaxError: invalid syntax
>>> def convert_to_fahrenheit(celcius):
	return (celcius * 9 /5) + 32

>>> convert_to_fahrenheit(23.88888888889)
75.000000000002
>>> convert_to_fahrenheit(0)
32.0
>>> def quadratic(a, b, c, x):
	first = a * x ** 2
	second = b * x
	third = c
	return first + second + third

>>> quadratic(2,3,4,0.5)
6.0
>>> def a(x, y, z):
	if x:
		return y
	else:
		return z

	
>>> def b(q, r):
	return a(q > r, q ,r)

>>> a(False, 2, 3)
3
>>> b(3,2)
3
>>> a(3>2, a, b)
<function a at 0x023D7A50>
>>> b(a, b)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    b(a, b)
  File "<pyshell#25>", line 2, in b
    return a(q > r, q ,r)
TypeError: unorderable types: function() > function()
>>> def square (x):
	return x * x

>>> square(3)
9
>>> square(4)
16
>>> 
