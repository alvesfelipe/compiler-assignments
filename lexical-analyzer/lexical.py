#!/usr/bin/env python
#Lexical Analyzer implementation
__author__ = "Felipe Alves"
__email__ = "felipealves@lavid.ufpb.br"

import sys

#token arrays
key_words = ['program', 'var', 'integer', 'real',
			 'boolean', 'procedure', 'begin', 'end',
			 'if', 'then', 'else', 'while', 'do', 'not']
delimiters = [';', '.', ':', '(', ')', ',']
assignment = [':=']
relational_operators = ['=', '<', '>', '<=', '>=', '<>']
aditive_operators = ['+', '-', 'or']
multiplicative_operators = ['*', '/', 'and']
#end token arrays

token_type = {'Key Word': key_words,
		  'Deimiter': delimiters,
		  'Assignment': assignment,
		  'Relational Operator': relational_operators,
		  'Aditive Operator': aditive_operators,
		  'Multiplicative Operator': multiplicative_operators
		 }

number_test = '10.0'
token_test = '+'

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
	if(aux_check(str, token_type['Key Word'])):
		return True
	else:
		return False

#check if the token is a key word
def isToken(token):
	for key in token_type:
		if any(token == value for value in token_type[key]):
			return (token, key)
	return None

print "Is Integer: ", isInt(number_test)
print "Is Float: ", isFloat(number_test)
print "Is Key Word: ", isToken(token_test)

#read file, split by line and put in a list
with open(sys.argv[1], 'r') as my_file: list_file = my_file.read().splitlines()

#removing unused elements
list_file = [s.replace('\t', '') for s in list_file]
#get the number of lines
print "Lines: ", len(list_file)


print list_file