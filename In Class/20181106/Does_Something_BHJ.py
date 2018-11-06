import random

RandomNumber = random.randint(1,25)
Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s', \
		  't','u','v','w','x','y','z']
NotAlphabet = [' ', '.',',']
Text = "test_file.txt"
Read = "r"
fw = "processed.txt"
e = "utf-8"
Encrypted = ""

OpenText = open(Text,Read)
MyText = OpenText.read()

def Encrytion(ReadText): 

    EncryptedText = ""

    for i in range(len(ReadText)):     
	    if ReadText[i] in NotAlphabet:     # If character is not alphabet, don't change
		    EncryptedText += ReadText[i]
	    else:
		    AlphabetIndex = Alphabet.index(ReadText[i].lower()) # Character is alphabet, find the index in alphabet list
			
		    Remainder = (AlphabetIndex + RandomNumber) % 26  # Adding index and randomnumber devided by 26, give me remainder
															# Because Alphabet have 26 numbers 
			
		    if ReadText[i].upper() == ReadText[i]:          # If Character is upper, go to the alphabet index of remainder
															# and change it
			    EncryptedText += Alphabet[Remainder].upper()    # Upper character should be upper character 
		    else:
			    EncryptedText += Alphabet[Remainder]            # If character is lower, character should be lower  

    return(EncryptedText)


def Decryption(EncryptedText):

	OriginalText = ""

	for i in range(len(EncryptedText)):     
		if EncryptedText[i] in NotAlphabet:     # If character is not alphabet, don't change
			OriginalText += EncryptedText[i]
		else:
			AlphabetIndex = Alphabet.index(EncryptedText[i].lower()) # Character is alphabet, find the index in alphabet list
			
			Remainder = (AlphabetIndex - RandomNumber) % 26  # Adding index and randomnumber devided by 26, give me remainder
															# Because Alphabet have 26 numbers 
			
			if EncryptedText[i].upper() == EncryptedText[i]:          # If Character is upper, go to the alphabet index of remainder
															        # and change it
				OriginalText += Alphabet[Remainder].upper()    # Upper character should be upper character 
			else:
				OriginalText += Alphabet[Remainder]            # If character is lower, character should be lower 

	return(OriginalText)

Encrypted = Encrytion(MyText)
Decrypted = Decryption(Encrypted)

print(Encrypted)
print(Decrypted)

