Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1 = list()
>>> list2 = list([2,3,4])
>>> list3 = list(["red" , "green", "blue"])
>>> list4 = list(range(3,6))
>>> list5 = list("abcd")
>>> list1
[]
>>> list1 = []
>>> list2
[2, 3, 4]
>>> list2 = [2,3,4]
>>> list1 = [2,3,4,22,23,42,56,61]
>>> len(list)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    len(list)
TypeError: object of type 'type' has no len()
>>> len(list1)
8
>>> max(list1)
61
>>> min(list1)
2
>>> sum(list1)
213
>>> import random
>>> random.shuffle(list1)
>>> list1
[61, 4, 3, 2, 22, 56, 42, 23]
>>> for i in range(len(myList) - 1):
	myList[i] = i

	
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    for i in range(len(myList) - 1):
NameError: name 'myList' is not defined
>>> for i in range(len(list1) - 1):
	myList[i] = i

	
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    myList[i] = i
NameError: name 'myList' is not defined
>>> for i in range(len(list1) - 1):
	list1[i] = i

	
>>> i = 0
>>> while i < len(list1):
	print(list1[i])
	i += 1

	
0
1
2
3
4
5
6
23
>>> list1
[0, 1, 2, 3, 4, 5, 6, 23]
>>> list1[2:5]
[2, 3, 4]
>>> list1[2:-2]
[2, 3, 4, 5]
>>> list1[::2]
[0, 2, 4, 6]
>>> list1 = [1,2,3,4]
>>> list2 = [3,4,5,6]
>>> list3 = list1 + list2
>>> list3
[1, 2, 3, 4, 3, 4, 5, 6]
>>> 2 in list1
True
>>> 2 in list2
False
>>> range(5)
range(0, 5)
>>> range(0,5)
range(0, 5)
>>> range (2,10,2)
range(2, 10, 2)
>>> print(range(2,10,2))
range(2, 10, 2)
>>> range(5)
range(0, 5)
>>> list(range(2,5))
[2, 3, 4]
>>> for i in list3:
	print(i)

	
1
2
3
4
3
4
5
6
>>> for i in range(0,len(list3),2):
	print(list3[i])

	
1
3
3
5
>>> list1 = [x for x in range(5)]
>>> list1
[0, 1, 2, 3, 4]
>>> list2 = [0.5 * x for x in list1]
>>> list2
[0.0, 0.5, 1.0, 1.5, 2.0]
>>> list3 = [x for x in list 2 if x<1.5]
SyntaxError: invalid syntax
>>> list3 = [x for x in list2 if x<1.5]
>>> list3
[0.0, 0.5, 1.0]
>>> list4 = [x for x in list1 x**x]
SyntaxError: invalid syntax
>>> list4 = [x**x for x in list1]
>>> list4
[1, 1, 4, 27, 256]
>>> list4.append(12)
list4
>>> list4
[1, 1, 4, 27, 256, 12]
>>> list4.count(4)
1
>>> list1.extend(list2)
>>> list1
[0, 1, 2, 3, 4, 0.0, 0.5, 1.0, 1.5, 2.0]
>>> list1.index(4)
4
>>> list1.insert(3,11)
>>> list1
[0, 1, 2, 11, 3, 4, 0.0, 0.5, 1.0, 1.5, 2.0]
>>> ###Insert 11 at position index3
>>> list1.pop(3)
11
>>> list1
[0, 1, 2, 3, 4, 0.0, 0.5, 1.0, 1.5, 2.0]
>>> ###pop removes the element in the index 3
>>> list1.pop()
2.0
>>> list1.remove(3)
>>> list1
[0, 1, 2, 4, 0.0, 0.5, 1.0, 1.5]
>>> ### Remove number 3
>>> list1.reverse()
>>> list1
[1.5, 1.0, 0.5, 0.0, 4, 2, 1, 0]
>>> list1.sort()
>>> list1
[0.0, 0, 0.5, 1.0, 1, 1.5, 2, 4]
>>> "Jane John Peter Susan".split()
['Jane', 'John', 'Peter', 'Susan']
>>> items="02/08/15".split(/)
SyntaxError: invalid syntax
>>> items="02/08/15".split("/")
>>> items
['02', '08', '15']
>>> list99 = []
>>> print("Enter 10 numbers: ")
Enter 10 numbers: 
>>> for i in range(10):
	list99.append(eval(input()))

	
for i in range(10):
	list99.append(eval(input()))
Traceback (most recent call last):
  File "<pyshell#91>", line 2, in <module>
    list99.append(eval(input()))
  File "<string>", line 1
    for i in range(10):
      ^
SyntaxError: invalid syntax
>>> for i in range(10):
	list99.append(eval(input()))

	

Traceback (most recent call last):
  File "<pyshell#93>", line 2, in <module>
    list99.append(eval(input()))
  File "<string>", line 1, in <module>
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
>>> 
