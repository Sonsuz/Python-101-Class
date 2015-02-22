Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> True
True
>>> True or False
True
>>> True and False
False
>>> True if True
SyntaxError: invalid syntax
>>> not True
False
>>> 
>>> 12<12
False
>>> 32>41
False
>>> 12.33<12.331
True
>>> 13>=13
True
>>> (12>10) or (11>=14)
True
>>> "Said" = "said"
SyntaxError: can't assign to literal
>>> "Said" > "said"
False
>>> "Said" == "said"
False
>>> if "a" == "a"
SyntaxError: invalid syntax
>>> if "a" == "a":
	print("yes they are equal")

	
yes they are equal
>>> 3 == 3
True
>>> 3 == 3
True
>>> if "a" == "a":
	print("yes they are equal")
"a" == "a"
SyntaxError: invalid syntax
>>> x = 3
>>> if x < 0:
	print(" It is negative ")
elif x = 0:
	
SyntaxError: invalid syntax
>>> if x < 0:
	print(" It is negative ")
elif x == 0:
	print(" It is zero ")
else x > 0:
	
SyntaxError: invalid syntax
>>> if x < 0:
	print(" It is negative ")
elif x == 0:
	print(" It is zero ")
else :
	print(" It is positive ")

	
 It is positive 
>>> n = 10 # n bir numara
>>> if type(n) == int:
	if n < 0:
		print("Negatif Tamsayi")
	elif n == 0:
		print("N sifir")
	else:
		print("Pozitif Tamsayi")
elif type(n) == float:
	if n < 0:
		print("Negatif Rasyonel Sayi")
	else:
		print("Pozitif Rasyonel Sayi")
else:
	print("N sayisi Rasyonel Degil!")

	
Pozitif Tamsayi
>>> n = 8.2
>>> if type(n) == int:
	if n < 0:
		print("Negatif Tamsayi")
	elif n == 0:
		print("N sifir")
	else:
		print("Pozitif Tamsayi")
elif type(n) == float:
	if n < 0:
		print("Negatif Rasyonel Sayi")
	else:
		print("Pozitif Rasyonel Sayi")
else:
	print("N sayisi Rasyonel Degil!")

	
Pozitif Rasyonel Sayi
>>> n = 1+4j
>>> if type(n) == int:
	if n < 0:
		print("Negatif Tamsayi")
	elif n == 0:
		print("N sifir")
	else:
		print("Pozitif Tamsayi")
elif type(n) == float:
	if n < 0:
		print("Negatif Rasyonel Sayi")
	else:
		print("Pozitif Rasyonel Sayi")
else:
	print("N sayisi Rasyonel Degil!")

	
N sayisi Rasyonel Degil!
>>> 
