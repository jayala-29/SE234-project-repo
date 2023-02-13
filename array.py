import random
arr = []
# generate a random array of length k
for k in range(int(random.randint(1,10))):
	# give the array random values
	arr.append(int(random.randint(0,100)))
print("Here's an array: " + str(arr))
# ask for index value
i = input("Which index would you like printed out? ")
print("Okay, the value at the index you requested is: " + str(arr[int(i)]))
