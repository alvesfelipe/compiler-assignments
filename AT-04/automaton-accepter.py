#!/usr/bin/python
#Deterministic finite accepter

#some symbols of alphabet
alphabet_symbols = ['+', '-', '/', '*']

def check_symbols(str_input):
	for element_str in str_input:
		if not any(element_str == element_symb for element_symb in alphabet_symbols):
			print "Error, invalid string: ", str_input
			return
	print "String ACCEPTED!"

str = raw_input("Insert the String: ")
list_str = list(str)

# print "list string: ", list_str[0:len(list_str)]
check_symbols(list_str)