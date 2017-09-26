==================
   mixed_cipher
==================

Made By: Israel Felhandler

This is a small program which takes a filename as a command-line argument and ten performs substitution on the file contents with a mixed alphabet. Once the program beings, a mixed alphabet is created by prompting the user for a "keyword", removing repeated letters in the keyword, and then writing the remaining letters of the alphabet in the usual order. Note: capitalization and punctuation are kept as is in the encrypted text.
For example, if the keyword is “computer”, then the mixed alphabet is the following:
      Plaintext: ABCDEFGHIJKLMNOPQRSTUVWXYZ
      Ciphertext: COMPUTERABDFGHIJKLNQSVWXYZ
      
The file test.txt has the following contents:
     This is a file. This file has some WORDS in it.
     
SAMPLE RUN:

$ python mixed_cipher.py test.txt
Please enter a keyword for the mixed cipher: Motherboard
Plaintext: abcdefghijklmnopqrstuvwxyz 
Ciphertext: motherbadcfgijklnpqsuvwxyz 
Sadq dq m rdge. Sadq rdge amq qkie WKPHQ dj ds.
