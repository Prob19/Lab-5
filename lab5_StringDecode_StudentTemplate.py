"""
Patrick Robinson
9/23/22
This code fixes a computer problem that involves keys being assigned to the wrong letters. This code decodes the letters and numbers given and produces the correct letters.


"""



def main():


	
	#encodedWord = "tx33dom"
	#encodedWord = "t3xb3f"
	#encodedWord = "koxb3zpond3nk3"
	#encodedWord = "fako fim3"
	#encodedWord = "zom3 xafz bun"	
	#encodedWord = "txiday tun tob tx3nkh tbi3z"
	#encodedWord = "kafz kan kafkh kakfuz3z wifh klawz"
	
	
	
	#encodedWord = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	print(DecodeWord(encodedWord))
	




#Your code goes here.
def DecodeWord(encodedWord): #This code reassigns the keys to the correct letters 
	decodedWord = ""
	for letter in encodedWord:
		if letter == "t":
			decodedWord += "f"
		elif letter == "f":
			decodedWord += "t"
		elif letter == "3":
			decodedWord += "e"
		elif letter == "k":
			decodedWord += "c"
		elif letter == "z":
			decodedWord += "s"
		elif letter == "b":
			decodedWord += "r"
		elif letter == "x":
			decodedWord += "r"
			
		else: 
			decodedWord += letter #This code compiles all of the letters together
	return decodedWord










#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()
