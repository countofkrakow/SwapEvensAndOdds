#!/usr/bin/python



def swapEvensAndOdds(myList, value=None):
	length = len(myList)
	if length % 2 != 0:
		return 'List length is not even. Try again.'
	odds = 1
	evens = 0
	reachedEnd = False
	while not reachedEnd and length > evens and length > odds - 1:
		if myList[odds] % 2 == 0: 
			if myList[evens] % 2 == 1:
				temp = myList[odds]
				myList[odds] = myList[evens]
				myList[evens] = temp
				if length == odds or length - 1 == evens:
					reachedEnd = True
			else:
				evens += 2
		else:
			odds += 2
	return myList

def main():
	array = raw_input('Give an array of even length to swap evens and odds separated by commas:') 
	array = array.split(',')
	array = map(int, array)
	while len(array) % 2 != 0:
		array = raw_input('Give an array of even length to swap evens and odds separated by commas:') 
		array = array.split(',')
		array = map(int, array)
	sortedArray = swapEvensAndOdds(array)
	print sortedArray

if __name__ == "__main__":
	main()
