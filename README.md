# Image file check

The application opens a binary file and prints its first three bytes 
in decimal and hexadecimal format. It checks the signature of the file,
whether it is jpeg type or not and returns the result.

- The signature of a file is consisted by the first bytes, which are
  specific for each kind of file.

- In a jpeg file, the signature is consisted by the first three digits,
  which are 255, 216, 255 (dec) or FF, D8, FF (hex).
