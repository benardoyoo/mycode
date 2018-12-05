#!/usr/bin/env python3
message = 'mon sub '
print('What command do you want to run?')
command = (input())
if command == ('LTE'):
    message = message + 'IMSI.'
elif command == ('CDMA'):
    message = message + 'username.'
else:
    message = 'Please retake Data 101 Class ASAP!!!'
print(message)