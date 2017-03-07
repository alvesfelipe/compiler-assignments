#!/usr/bin/env python
#Lexical Analyzer implementation
__author__ = "Felipe Alves"
__email__ = "felipealves@lavid.ufpb.br"

import sys
import re

#token lists
key_words = ['program', 'var', 'integer', 'real',
			 'boolean', 'procedure', 'begin', 'end',
			 'if', 'then', 'else', 'while', 'do', 'not']
delimiters = [';', '.', ':', '(', ')', ',']
assignment = [':=']
relational_operators = ['=', '<', '>']
relational_operators_2 = ['<=', '>=', '<>']
aditive_operators = ['+', '-']
multiplicative_operators = ['*', '/']
special_operators = ['or', 'and']
#end token lists

#defining dictionary with toke type (key) and token list (value)
token_type = {'Key Word': key_words,
		  'Delimiter': delimiters,
		  'Assignment': assignment,
		  'Operator': relational_operators + relational_operators_2 + 
		  			  aditive_operators + multiplicative_operators + special_operators
		  # 'Relational Operator': relational_operators,
		  # 'Aditive Operator': aditive_operators,
		  # 'Multiplicative Operator': multiplicative_operators,
		  # 'Special Operator': special_operators
		 }
#end dictionary

number_test = 'aasdf123sd'
token_test = 'v <=1;v <=1; valor1: integer;'
ident_test = 'AAa066_'

def removeTrash(str):
	removed = str.replace('\t', '')
	removed = re.sub(r'\{.*?\}', '', removed)

	return removed

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

#check if the string is a token
def isToken(token):
	for key in token_type:
		if any(token == value for value in token_type[key]):
			return (token, key)
	if isInt(token):
		return (token, "Integer")
	if isFloat(token):
		return (token, "Float")
	if isIdentifier(token):
		return (token, "Identifier")
	return None

def spaceSimpleOperator(str, token_list):
	print "STRING:", str
	for i in token_list:
		for ap in range(str.count(i)):
			print ap
			indices = [ind for ind, x in enumerate(str) if x == i]
			print "Indices:", indices
			if indices:
				aux = indices[ap]
				str = str[:aux] + ' ' + str[aux:]
				str = str[:aux+2] + ' ' + str[aux+2:]
				print "RES:", str.split()

# print "Is Token: ", isToken(number_test)

#read file, split by line and put in a string
with open(sys.argv[1], 'r') as my_file:
	file = my_file.read()

#removing unused elements
file = removeTrash(file)

#split file by lines
list_file = file.splitlines()
print list_file
spaceSimpleOperator(token_test, delimiters)
# insertRelationalSpace(token_test)
#get the number of lines
print "-------------->Lines:", len(list_file)

# print list_file
# for line in list_file:
	# print line.split()