# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 10:50:45 2018

@author: sashank
"""
import base64
import telnetlib
import string
import timeit
import sys
"""
defining variables
"""
latestDecryptedMsg=""
lengthOfDecryptedText=75
hostname="crime.cse545.rev.fish"
port=30925
hackerhandle = "sas"
encrArr=[]
asciiChars=string.printable
hackerHandleQuery=b"Your hacker handle:"
giveMessageQuery=b"Now give me your message:"
hereIsEncrpyted=b'Here is the encrypted message:'
nextInputQuery=b"If you want, you can give me another message, and I will encrypt it for you:"
extraOutput="If you want, you can give me another message, and I will encrypt it for you:"

"""
establish a connection to the host
"""
class crime:
    def makeConnection(self,msg):
        encrMsg=""
        tn = telnetlib.Telnet(hostname  , port , timeout =10)
        print("establishing connection...")
        tn.read_until(hackerHandleQuery)
        tn.write((hackerhandle+ "\n").encode('ascii'))
        tn.read_until(giveMessageQuery)
        print("Providing input to service --> " , msg);
        if(msg=="\n"):
            return " "
        tn.write((msg + "\n").encode('ascii'))
        tn.read_until(hereIsEncrpyted)
        mg=tn.read_until(nextInputQuery)
        encrMsg=mg.decode('ascii')
        replacIngVal=extraOutput
        encrMsg= encrMsg.replace(replacIngVal , "").rstrip('')
        return encrMsg
    
    """
    generate the encrypted array holding all outputs from telnet connection
    """
    def generateEncrArr(self,decryptMsg):
        arr=[]
        for i in range(len(asciiChars)):
            msg=self.makeConnection(decryptMsg+asciiChars[i])
            arr.append(msg)
            print("inside loop..", i)
        return arr
    
    """
    get character by finding the index with least length
    """
    def getLeastLength(self,arr):
        print("inside checkLeast...")
        minLength = sys.maxsize
        minIndex=0
        for i in range(len(arr)):
            encr = arr[i]
            print(encr)
            if(encr!=" "):
                decoded = base64.b64decode(encr);
                s = str(decoded)
                s=''.join('%02x' % ord(c) for c in s)
                print("length of encrypted text with value at index ---> "  , len(s) ,i)
                if(len(s)<minLength):
                    minLength=len(s)
                    minIndex=i
                    print("min value-->" , i)
        return asciiChars[minIndex]
    
    """
    get the decrypted message iterating over the length of decrypted text given
    """
    def getDecryptedMessage(self):
        decryptedMsg=""
        startTime=timeit.default_timer() 
        for i in range(lengthOfDecryptedText):
            print("Inside getDecryptedMessage  --> loop :" , i)
            encrArr=self.generateEncrArr(decryptedMsg)
            characterAppend=self.getLeastLength(encrArr)
            decryptedMsg+=characterAppend
            endTime=timeit.default_timer()
            print("Current decrypted message --> " ,decryptedMsg)
            print("Total time taken --> " ,endTime-startTime)
        return decryptedMsg

def main():
    cr = crime()
    resultMessage=cr.getDecryptedMessage()
    file = open("message.txt","w") 
    file.write(resultMessage)
    print("------------End of main-------------")

    
if __name__== "__main__":
    main()
