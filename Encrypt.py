#Name : Matheus Figueroa 

def main():
	'''open the file and ask user for  a value for s 
	if no value is given, an exception occurs'''

	f = open('thetestfile.txt','r')
	lines = f.readlines()
	f.close()
	done = False
	while(not(done)):
		try:
			s = int(input("Please enter the number of characters you would like to shift > "))
			done = True
		except:
			print("Sorry, input must be an integer")
	encrypt_char(lines,s)
	decrypt_file('encryptfile.txt',s)



def encrypt_char(lines,s):
	'''This fucntion converts the chars to acsii,
	later the ascii value is added with the s variable then converted back
	to a char type'''
	encrypt_lines = []
	for element in lines:
		string = ''
		for char in range(len(element)):
			if element[char] >= 'A' and element[char] <= 'Z':
				new_ascii = ord(element[char])+s
				while 1:
					if new_ascii > 90:
						x = new_ascii - 90
						new_ascii = 64 + x
					else:
						break
				string += chr(new_ascii)
				
			elif element[char] >= 'a' and element[char] <= 'z':
				new_ascii = ord(element[char])-s
				while 1:
					if new_ascii < 97:
						x = 97 - new_ascii
						new_ascii = 123 - x
					else:
						break
				string += chr(new_ascii)
				
			elif element[char] >= '0' and element[char] <= '9':
				new_ascii = ord(element[char])-s
				while 1:
					if new_ascii < 48:
						x = 48 - new_ascii
						new_ascii = 58 - x
					else:
						break
				string += chr(new_ascii)

			else:
				string += element[char]
				
		encrypt_lines.append(string)


	f = open('encryptfile.txt','w') #write to a new file
	for i in encrypt_lines:
		f.write(i)
	f.close()

	line = 1
	for i in encrypt_lines:
		print('Line [',line,'] encrypted is : ',i,end='')
		line +=1
	print('\n')



def decrypt_file(file,s):
	'''The concept of this function is very similar to 
	the previous one, just reversed to so we can decrypt the message'''
	f = open(file,'r')
	lines = f.readlines()
	decrypt_lines = []
	for element in lines:
		string = ''
		for char in range(len(element)):
			if element[char] >= 'A' and element[char] <= 'Z':
				new_ascii = ord(element[char])-s
				while 1:
					if new_ascii < 65:
						x = 65 - new_ascii
						new_ascii = 91 - x
					else:
						break
				string += chr(new_ascii)
				
			elif element[char] >= 'a' and element[char] <= 'z':
				new_ascii = ord(element[char])+s
				while 1:
					if new_ascii > 122:
						x = new_ascii - 122
						new_ascii = 96 + x
					else:
						break
				string += chr(new_ascii)
				
			elif element[char] >= '0' and element[char] <= '9':
				new_ascii = ord(element[char])+s
				while 1:
					if new_ascii > 57:
						x = new_ascii - 57
						new_ascii = 47 + x
					else:
						break
				string += chr(new_ascii)

			else:
				string += element[char]
				
		decrypt_lines.append(string)

	line = 1
	for i in decrypt_lines:
		print('Line [',line,'] decrypted is :', i, end='')
		line +=1
	


main()