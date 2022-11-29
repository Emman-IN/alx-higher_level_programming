#!/usr/bin/python3
for i in range(97, 123):
    if ord(i) != 105 and ord(i) != 101:
      print('{}'.format(chr(i)), end='')
