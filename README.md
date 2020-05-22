# Binary2Decimal
Ever wanted to convert a string of 10010010 to decimal 146. If you managed to miss the millions of other tools that do the same thing and landed here, I welcome you <br>
make sure you edit the shebang with your python2 path<br>

Usage: ./b2d.py [option] [string] <br>
Options:<br>
  -b ; convert binary to decimal<br>
  -d ; convert decimal to binary<br>
  -l ; convert multiple values seperated by commas<br>
Example: ./b2d -b 0010 -> returns 2<br>
Example: ./b2d -d 24 -> returns 11000<br>
Note: binary assumes the bit to the right is the lowest<br>
decimal will return highest bit to the left<br>
