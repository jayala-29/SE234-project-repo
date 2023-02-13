import random
arr = []
for k in range(int(random.randint(1,10))):
	arr.append(int(random.randint(0,100)))
print("Here's an array: " + str(arr))
i = input("Which index would you like printed out? ")
print("Okay, the value at the index you requested is: " + str(arr[int(i)]))
