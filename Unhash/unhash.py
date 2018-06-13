import sys

characters = "acdegilmnoprstuw"

def unhash(hashed):
	""" 
		Method which unhashes a given integer.

		The provided hash function converts from base 37 to base 10.
		For unhasing we convert from base 10 to base 37.
		Taking care of edge cases as well.
 	"""
	if hashed > 7:
		rem = hashed%37
		hashed = hashed//37
		return unhash(hashed) + characters[rem]
	if hashed == 7:
		return ""		
	if hashed < 7:
		print("Invalid hash number")
		sys.exit()		


if len(sys.argv) == 2:
	if(not(sys.argv[1].isdigit())):
		print("Please enter hash as a number.")
	else:
		print(unhash(int(sys.argv[1])))
else:
	print("Please run the code using one of the below:\n  --> python unhash.py <hash>")
	

