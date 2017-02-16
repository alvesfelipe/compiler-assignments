#!/usr/bin/python
#Deterministic finite accepter

#symbols
symbols = ['+', '-', '/', '*']

def check_symbols(str_input):
	if any(element == str_input for element in symbols):
		print str_input
		return;

str = raw_input("Insert the String: ")
check_symbols(str)