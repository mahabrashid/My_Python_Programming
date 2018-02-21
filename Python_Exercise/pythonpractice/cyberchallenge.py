'''
Created on 24 Jan 2018

@author: marashid
'''

def CaesarGenerator(mode, message, key):
    if mode[0] == 'd':
        key = -key

    translated = []

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
        if symbol.isupper():
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
        elif symbol.islower():
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26

            translated.append(chr(num))
        
        else:
            translated.append(symbol)

    return "".join(translated)

def CodeInjector(code):
    data =  CaesarGenerator('d','myyux://bbb.huhdgjwhmfqqjslj.htr/UwtizhyntsQnsj/YfpjTajwYmjUwtizhynts.umu',code)
    
    print(data)
    
    if data[0:5] == "https":
        print ("[+] You Have Successfully Injected The Code To The Production Line, Visit:\n\n",data,"\n\nCongratulations!")
    else:
        print ("[-] something Wrong, Try Again.")
        
CodeInjector(5)