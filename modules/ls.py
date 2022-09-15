#keywords and its applications

from colorama import Fore, Back, Style, init

myDict = {
	'del <file>': 'removes a file',
	'make <file>' : 'makes a file',
	'ls' : 'list the files and folder in current directory',
	'self' : 'gives current position',
	'Ctrl + Z' : 'exit'
}

def __list():

	for i, j in myDict.items():
		print(f'{Fore.LIGHTRED_EX}{i} {Fore.RESET}->>> {Fore.LIGHTBLUE_EX}{j}')
	print("\n")