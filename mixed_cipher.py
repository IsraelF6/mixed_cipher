"""Israel Felhandler"""
"""IF12B"""
"""CIS4930 - Python"""
"""Summer 2017"""

import sys

plainText = "abcdefghijklmnopqrstuvwxyz"
plainTextCap = plainText.upper()
plainTextSet = set(plainText)

#Check correct format
try:
    filename = sys.argv[1]
    f = open(filename, 'r')
except (IndexError, IOError):
    print "Please use a VALID filename as a command line argument."
else:
    fileText = f.read()
    f.close()
    print "Please enter a keyword for the mixed cipher: "
    keyword = raw_input()
    keyword = keyword.lower()
    keywordSet = set(keyword)
    keywordList = list(keyword)
    cipherText = str()

    #Create the begining of the cipher
    for i in range(0, len(keyword)):
        duplicate = False
        for j in range(0, len(cipherText)):
            if keyword[i] == cipherText[j]:
                duplicate = True
        if duplicate is False:
            cipherText += keyword[i]

    #Find portion of alphabet to append to ciphered alphabet
    leftOverSet = plainTextSet - keywordSet
    #Convert set to list and sort it alphabetically
    leftOverList = list(leftOverSet)
    leftOverList.sort()
    #Size of remaining alphabet
    size = len(leftOverList)
    #Add remaining alphabet to cipher
    for i in range(0, size):
        cipherText += leftOverList[i]
    print "Plaintext: ", plainText
    print "Ciphertext: ", cipherText

    encryptedText = str()
    for char in fileText:
        #Check if char is not A-Za-z
        if ord(char) < 65 or ord(char) > 122:
            encryptedText += char
        #char is capital letter
        elif ord(char) < 91:
            for i in range(0, 25):
                if char == plainText[i].upper():
                    index = i
            encryptedText += cipherText[index].upper()
        #char is lower case letter
        else:
            for i in range(0, 25):
                if char == plainText[i]:
                    index = i
            encryptedText += cipherText[index]
    print encryptedText