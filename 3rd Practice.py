Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> while True:
	print("Welcome", i, " times. To stop press [CTRL+C]")
	if i == 5:
		break
	i += 1
	time.sleep(2)

	
Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    print("Welcome", i, " times. To stop press [CTRL+C]")
NameError: name 'i' is not defined
>>> i = 1
>>> while True:
	print("Welcome", i, " times. To stop press [CTRL+C]")
	if i == 5:
		break
	i += 1
	time.sleep(2)

	
Welcome 1  times. To stop press [CTRL+C]
Welcome 2  times. To stop press [CTRL+C]
Welcome 3  times. To stop press [CTRL+C]
Welcome 4  times. To stop press [CTRL+C]
Welcome 5  times. To stop press [CTRL+C]
>>> for k in "sleep":
	print(k)

	
s
l
e
e
p
>>> for k in "sleep":
	print(k, end = ".")

	
s.l.e.e.p.
>>> n = 12
>>> while True:
	print(n, end = ",")
	n = n + 2

	
12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198,200,202,204,206,208,210,212,214,216,218,220,222,224,226,228,230,232,234,236,238,240,242,244,246,248,250,252,254,256,258,260,262,264,266,268,270,272,274,276,278,280,282,284,286,288,290,292,294,296,298,300,302,304,306,308,310,312,314,316,318,320,322,324,326,328,330,332,334,336,338,340,342,344,346,348,350,352,354,356,358,360,362,364,366,368,370,372,374,376,378,380,382,384,386,388,390,392,394,396,398,400,402,404,406,408,410,412,414,416,418,420,422,424,426,428,430,432,434,436,438,440,442,444,446,448,450,452,454,456,458,460,462,464,466,468,470,472,474,476,478,480,482,484,486,488,490,492,494,496,498,500,502,504,506,508,510,512,514,516,518,520,522Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    print(n, end = ",")
  File "C:\Python34\lib\idlelib\PyShell.py", line 1352, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> while True:
	print(n, end = ",")
	n = n + 2
	time.sleep(3)

	
522,524,526,528,530,532,534,536,538,540,Traceback (most recent call last):
  File "<pyshell#25>", line 4, in <module>
    time.sleep(3)
KeyboardInterrupt
>>> 
