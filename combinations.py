from pprint import pprint

def find_combinations():

	# this is an example of your potential numbers, yours will vary
	# there will be 5 integers and 7 non-integers (all .5 decimals)
	potential_numbers = [12, 7, 22, 2, 32, 2.5, 5.5, 29.5, 27.5, 34.5, 17.5, 8.5 ]
	
	# only integers are kept
	int_numbers = [x for x in potential_numbers if isinstance(x,int)]

	last_digits = [x % 10 for x in int_numbers]

	# array index of the unique mod-10 value in the potential numbers
	last_num = int_numbers[last_digits.index(find_non_duplicate(last_digits))]

	combinations = []

	# generate all possible first and second number combinations
	first_num = [int((4*i) + (last_num % 4)) for i in range(10)]
	second_num = [int((first_num[i] + 2) % 40) for i in range(10) ]

	# spit out all 80 combinations
	for i in range(10):
		for j in range(10):
			if abs(last_num - (second_num[j]+2) %40) > 2 and \
			abs(last_num - (second_num[j]-2) %40) > 2:
				tmp = [first_num[i], second_num[j], last_num]
				combinations.append(tmp)

	pprint(combinations)

def find_non_duplicate(array):
	result = array[0]
	for i in array[1:]:
		result ^= i
	return result

find_combinations()
