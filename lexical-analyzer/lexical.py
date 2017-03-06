#!/usr/bin/env python
#Lexical Analyzer implementation
__author__ = "Felipe Alves"
__email__ = "felipealves@lavid.ufpb.br"

import sys

#token arrays
key_words = ['program', 'var', 'integer', 'real',
			 'boolean', 'procedure', 'begin', 'end',
			 'if', 'then', 'else', 'while', 'do', 'not']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
delimiters = [';', '.', ':', '(', ')', ',']
assignment = [':=']
relational_operators = ['=', '<', '>', '<=', '>=', '<>']
aditive_operators = ['+', '-', 'or']
multiplicative_operators = ['*', '/', 'and']
#end token arrays

number_test = '10.0'
token_test = 'program'

#auxiliary function, used for check if the specific element of string is contained on a specific symbol list
def aux_check(symbol, list_symbol):
	if any(symbol == element_symb for element_symb in list_symbol):
		return True

#check if the token is an integer
def isInt(str):
    try: 
        int(str)
        return True
    except ValueError:
        return False

#check if the token is a float
def isFloat(str):
	try:
		float(str)
		return True
	except ValueError:
		return False

#check if the token is a key word
def isKeyWord(str):
	if(aux_check(str, key_words)):
		return True
	else:
		return False

print "inteiro? ", isInt(number_test)
print "float? ", isFloat(number_test)
print "is keyword? ", isKeyWord(token_test)

#read file, split by line and put in a list
with open(sys.argv[1], 'r') as my_file: list_file = my_file.read().splitlines()

#get the number of lines
print len(list_file)


print list_file