#!/usr/bin/env python3
## Collect input from the user
hostname = input("Please enter a hostname:")
## Print out the input collected from the user
print("You told me your hostname is:"  + hostname)
if hostname.lower() == 'mtg':
	print('The hostname matches expected config')
print("Exiting the script")



