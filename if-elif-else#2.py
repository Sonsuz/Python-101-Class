Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> if 8>7:
	print("Yep")

	
Yep
>>> if 6>7:
	print("Yep")
else:
	print("Nope")

	
Nope
>>> var= 'Panda'
>>> if var == "panda":
	print("Cute!")
elif var == "Panda":
	print("Regal!")
else:
	print("Ugly...")

	
Regal!
>>> temp = 120
>>> if temp > 85:
	print("Hot")
elif temp > 100:
	print("REALLY HOT!")
elif temp > 60 :
	print("Comfotable")
else:
	print("Cold")

	
Hot
>>> temp=30
>>> if temp > 85:
	print("Hot")
elif temp > 100:
	print("REALLY HOT!")
elif temp > 60 :
	print("Comfotable")
else:
	print("Cold")

Cold
>>> PH = 12
>>> if 7 > PH >1 :
	print("acidic")
elif PH = 7:
	
SyntaxError: invalid syntax
>>> if 7 > PH >= 1 :
	print("acidic")
elif PH == 7:
	print("neutral")
elif 14 >= PH > 7:
	print("alkaline")
else:
	print(" What is that? ")

	
alkaline
>>> PH = 3
>>>

	
acidic
>>> time = 13:00
SyntaxError: invalid syntax
>>> time = 13.00
>>> if 24.00 > time > 20.00:
	print("night")
elif 20.00 > time > 19.00:
	print("evening")
elif 19.00 > time > 17.00:
	print("dusk")
elif 17.00 > time > 12.00:
	print("afternoon")
elif 12.00 == time:
	print("noon")
elif 12.00 > time > 6.00:
	print("morning")
elif 6.00 > time > 5.00:
	print("dawn")
elif 5.00 > time > 4.00:
	print("twilight")
elif 4.00 > time > 0.00:
	print("night")
else:
	print(" Sorry ")

	
afternoon
>>> if 24.00 > time >= 20.00:
	print("night")
elif 20.00 > time >= 19.00:
	print("evening")
elif 19.00 > time >= 17.00:
	print("dusk")
elif 17.00 > time > 12.00:
	print("afternoon")
elif 12.00 == time:
	print("noon")
elif 12.00 > time >= 6.00:
	print("morning")
elif 6.00 > time >= 5.00:
	print("dawn")
elif 5.00 > time >= 4.00:
	print("twilight")
elif 4.00 > time >= 0.00:
	print("night")
else:
	print(" Sorry ")

	
afternoon
>>> time = 4.00
>>> if 24.00 > time >= 20.00:
	print("night")
elif 20.00 > time >= 19.00:
	print("evening")
elif 19.00 > time >= 17.00:
	print("dusk")
elif 17.00 > time > 12.00:
	print("afternoon")
elif 12.00 == time:
	print("noon")
elif 12.00 > time >= 6.00:
	print("morning")
elif 6.00 > time >= 5.00:
	print("dawn")
elif 5.00 > time >= 4.00:
	print("twilight")
elif 4.00 > time >= 0.00:
	print("night")
else:
	print(" Sorry ")

	
twilight
>>> 
