#!/usr/bin/env python3

#######################################################################
# a_list is the original list
#######################################################################
a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#######################################################################
# Print out a subset of the list. Start with index 3, go to the end of the list.
# This prints out the list of [ 'd', 'e', 'f', 'g']
#######################################################################
print(a_list[3:])
print("...CHECKING...Did it return... ['d', 'e', 'f', 'g']?")
print()

#######################################################################
# Print out the LAST item in the list
# NOTE: -1 means the last item in the list
#######################################################################
print(a_list[-1])
print("...CHECKING...Did it return g?")
print()

#######################################################################
# Print out the list.
# Start at the beginning of the list, end at index 5.
#######################################################################
print(a_list[:5])
print("...CHECKING...Did it return ['a', 'a', 'b', 'c', 'd', 'e']?")