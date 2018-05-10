def main():
	#function to obtain the smallest base in which the number is palindrome from 1 to n 
	n_input=input('Enter the last number to analize : ')
	try:
		n = int(n_input)
		print('number','|','smallest base in which the number is a palindrome')
		for number in range(1,n+1):
			count = 2
			nume = change_basis(number,count)
			while not palindrome(nume):
				count += 1
				nume = change_basis(number,count)
				width = len('number')
				print("{0:{width}{type}} |{1:{width}{type}}".format(number,count,width=width,type='d'))
	except ValueError:
		print('Not integer value')

if __name__ == "__main__":
	main()
