Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input("enter a number="))
enter a number=10
>>> print("{} {}".format(num,type(num)))
10 <class 'int'>
>>> balance=float(input("enter a number="))
enter a number=12.7
>>> print("{} {}.format(balance,type(balance)))
...       
SyntaxError: incomplete input
>>> print("{} {}".format(balance,type (balance)))
...       
12.7 <class 'float'>
>>> value = complex(input("enter a number="))
...       
enter a number=4+4j
>>> print("{} {}".format(value,type(value)))
...       
(4+4j) <class 'complex'>
>>> name = str(input("enter a name="))
...       
enter a name=navya
>>> print("{} {}".format(name,type(name)))
...       
navya <class 'str'>
>>> num=bool(input("enter a number="))
...       
enter a number=0
>>> print("{} {}".format(num,type(num)))
...       
True <class 'bool'>
>>> num = bool(input("enter a number="))
...       
enter a number=''
>>> 
>>> print("{} {}".format(num,(type(num)))
... 
