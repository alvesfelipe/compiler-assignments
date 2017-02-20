#!/usr/bin/python
#Deterministic finite state machine implementation

import sys

#some symbols of alphabet
alphabet_symbols = ['+', '-', '/', '*']
alphabet_float = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

def aux_check(symbol, str_input, list_symbol):
	if not any(symbol == element_symb for element_symb in list_symbol):
		print "Error, invalid string: ", str_input
		return True

def check_symbols(str_input):
	for element_str in str_input:
		if aux_check(element_str, str_input, alphabet_symbols): return
	print "String ACCEPTED!"

def check_is_float(str_input):
	for element_str in str_input:
		if aux_check(element_str, str_input, alphabet_float): return
	if aux_check(str_input[0], str_input, alphabet_float[0:9]): return
	if not str_input.count('.') == 1:
		print "Error, invalid string: ", str_input
		return
	if aux_check(str_input[-1], str_input, alphabet_float[0:9]): return
	print "String ACCEPTED!"		

str = raw_input("Insert the String: ")
list_str = list(str)

# print "list string: ", list_str[0:len(list_str)]
if any(list_str[0] == element_symb for element_symb in alphabet_symbols):
	check_symbols(list_str)
else:
	check_is_float(list_str)

