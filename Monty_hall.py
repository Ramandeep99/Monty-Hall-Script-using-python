


from collections import defaultdict as dd
from itertools import permutations 
import random

# initialising dictionary for storing the result
d = dd(lambda:0)

n = int(input('Enter number of test cases: '))
for i in range(n):

	# to generate a list of all the permutations of the given list
	x = list(permutations([0,0,1]))

	# to select a random list from all the permutations
	y = random.choice(x)

	# to generate a choice of user
	my_choice = random.randint(0,2)

	# to generate a box number which the owner opens
	for i in range(3):
		if y[i] != 1 and i != my_choice:
			opening_box = i

	# to store the count of wins on the choice of user
	if y[my_choice]:
		d['Same_Choice_Win']+=1

	# to generate the changed choice box number
	for i in range(3):
		if i != my_choice and i != opening_box:
			changed_choice = i

	# to store the count of wins on changed choice
	if y[changed_choice]:
		d['Changed_Choice_Win']+=1

# to print the result
for i,j in d.items():
	print('{} --> {}'.format(i,j))




























###        testing 1

# # x = random.randint(0,1)
# for i in range(2):
# 	x = list(permutations([0,0,1]))
# 	y = random.choice(x)
# 	print(y)
# 	# my_choice = random.choice(y)
# 	# print(my_choice)
# 	# opening_box = random.choice(y)

# 	my_choice = random.randint(0,2)
# 	for i in range(3):
# 		if y[i] != 1 and i != my_choice:
# 			opening_box = i
# 	print(my_choice,opening_box)
# 	if y[my_choice]:
# 		print('Win on same choice')
# 	else:
# 		print('Loss on same choice')
# 	for i in range(3):
# 		if i != my_choice and i != opening_box:
# 			changed_choice = i
# 	if y[changed_choice]:
# 		print('Win on changed choice')
# 	else:
# 		print('Loss on changed choice')

#######            testing 2

# d = dd(lambda:0)
# for i in range(1000):
# 	x = list(permutations([0,0,1]))
# 	y = random.choice(x)
# 	# print(y)

# 	my_choice = random.randint(0,2)
# 	for i in range(3):
# 		if y[i] != 1 and i != my_choice:
# 			opening_box = i

# 	# print(my_choice,opening_box)

# 	if y[my_choice]:
# 		# print('Win on same choice')
# 		d['same_choice_win']+=1
# 	# else:
# 	# 	# print('Loss on same choice')
# 	# 	d['same_choice_loss']+=1
# 	for i in range(3):
# 		if i != my_choice and i != opening_box:
# 			changed_choice = i
# 	if y[changed_choice]:
# 		# print('Win on changed choice')
# 		d['changed_choice_win']+=1
# 	# else:
# 	# 	# print('Loss on changed choice')
# 	# 	d['changed_choice_loss']+=1
# # print(dict(d))
# for i,j in d.items():
# 	print('{} --> {}'.format(i,j))

