Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def call_tel (kod,vremya):
	if kod==343:
		return vremya*15
	elif kod==381:
		return vremya*13
	elif kod==473:
		return vremya*18
	elif kod==485:
		return vremya*11
	else:
		print('Неизвестный код')

		
>>> call_tel(434,2)
Неизвестный код
>>> caii_tel(343,2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    caii_tel(343,2)
NameError: name 'caii_tel' is not defined
>>> call_tel(343,2)
30
>>> 