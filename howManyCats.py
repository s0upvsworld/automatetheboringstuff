def categorize_cats(num_cats):
	try:
		if int(num_cats) >= 4:
			return 'That is a lot of cats'
		else:
			return 'That is not that many cats.'
	except ValueError:
		return 'You did not enter a number'

if __name__ == '__main__':
	print('How many cats do you have?')
	num_cats = input()
	message = categorize_cats(num_cats)
	print(message)
	
	