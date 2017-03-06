#!/usr/bin/env python
#Lexical Analyzer implementation
__author__ = "Felipe Alves"
__email__ = "felipealves@lavid.ufpb.br"

import sys
import re

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

#defining dictionary with toke type (key) and token array (value)
token_type = {'Key Word': key_words,
		  'Deimiter': delimiters,
		  'Assignment': assignment,
		  'Relational Operator': relational_operators,
		  'Aditive Operator': aditive_operators,
		  'Multiplicative Operator': multiplicative_operators
		 }
#end dictionary

number_test = 'aasdf123sd'
token_test = 'procedureasdf'
ident_test = 'AAa066_'

#check if the toen is an identifier
def isIdentifier(str):
	identifiers = re.compile('^[a-zA-Z][a-zA-Z0-9_]*$')
	result = identifiers.match(str)

	if result:
		return True
	else:
		return False

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
def isToken(token):
	for key in token_type:
		if any(token == value for value in token_type[key]):
			return (token, key)
	return None

print "Is Token: ", isToken(number_test)

#read file, split by line and put in a list
with open(sys.argv[1], 'r') as my_file: list_file = my_file.read().splitlines()
#removing unused elements
list_file = [s.replace('\t', '') for s in list_file]
#get the number of lines
print "Lines: ", len(list_file)


print list_file