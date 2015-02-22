Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> LetterNum = 1
>>> Y = LetterNum + (LetterNum + 1)
>>> while LetterNum < 10:
	print(Y, "is" , LetterNum, "+" , LetterNum + 1)
	LetterNum += 1

	
3 is 1 + 2
3 is 2 + 3
3 is 3 + 4
3 is 4 + 5
3 is 5 + 6
3 is 6 + 7
3 is 7 + 8
3 is 8 + 9
3 is 9 + 10
>>> LetterNum = 1
>>> while LetterNum < 10:
	print(Y, "is" , LetterNum, "+" , LetterNum + 1)
	Y = letterNum + (LetterNum + 1)
	LetterNum += 1

	
3 is 1 + 2
Traceback (most recent call last):
  File "<pyshell#10>", line 3, in <module>
    Y = letterNum + (LetterNum + 1)
NameError: name 'letterNum' is not defined
>>> LetterNum = 1
>>> while LetterNum < 10:
	print(Y, "is" , LetterNum, "+" , LetterNum + 1)
	Y = LetterNum + (LetterNum + 1)
	LetterNum += 1

	
3 is 1 + 2
3 is 2 + 3
5 is 3 + 4
7 is 4 + 5
9 is 5 + 6
11 is 6 + 7
13 is 7 + 8
15 is 8 + 9
17 is 9 + 10
>>> LetterNum = 1
>>> while LetterNum < 10:
	Y + LetterNum + (LetterNum + 1)
	print(Y, "is" , LetterNum, "+" , LetterNum + 1)
	LetterNum += 1

	
22
19 is 1 + 2
24
19 is 2 + 3
26
19 is 3 + 4
28
19 is 4 + 5
30
19 is 5 + 6
32
19 is 6 + 7
34
19 is 7 + 8
36
19 is 8 + 9
38
19 is 9 + 10
>>> LetterNum = 1
>>> while LetterNum < 10:
	Y = LetterNum + (LetterNum + 1)
	print(Y, "is" , LetterNum, "+" , LetterNum + 1)
	LetterNum += 1

	
3 is 1 + 2
5 is 2 + 3
7 is 3 + 4
9 is 4 + 5
11 is 5 + 6
13 is 6 + 7
15 is 7 + 8
17 is 8 + 9
19 is 9 + 10
>>> T = 1
>>> while T < 10:
	print(T | T*2 , T*3 , T*4 , T*5 , T*6 , T*7 , T*8 , T*9)
	T += 1

	
3 3 4 5 6 7 8 9
6 6 8 10 12 14 16 18
7 9 12 15 18 21 24 27
12 12 16 20 24 28 32 36
15 15 20 25 30 35 40 45
14 18 24 30 36 42 48 54
15 21 28 35 42 49 56 63
24 24 32 40 48 56 64 72
27 27 36 45 54 63 72 81
>>> T = 1
>>> while T < 10:
	print(T | T*1, T*2 , T*3 , T*4 , T*5 , T*6 , T*7 , T*8 , T*9)
	T += 1

	
1 2 3 4 5 6 7 8 9
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81
>>> T = 1
>>> while T < 10:
	print(T , "|" , T*1, T*2 , T*3 , T*4 , T*5 , T*6 , T*7 , T*8 , T*9)
	T += 1

	
1 | 1 2 3 4 5 6 7 8 9
2 | 2 4 6 8 10 12 14 16 18
3 | 3 6 9 12 15 18 21 24 27
4 | 4 8 12 16 20 24 28 32 36
5 | 5 10 15 20 25 30 35 40 45
6 | 6 12 18 24 30 36 42 48 54
7 | 7 14 21 28 35 42 49 56 63
8 | 8 16 24 32 40 48 56 64 72
9 | 9 18 27 36 45 54 63 72 81
>>> Z = 1
>>> 
