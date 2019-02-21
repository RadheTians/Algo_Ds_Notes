# Function for Activity Selection
def print_activities(start, finish):
	print("Following activities are selected")
	i = 0
	print(i, end = "  ")
	for j in range(1, len(start)-1):
		if (start[j] >= finish[i]):
			print(j, end = "  ")
			i = j

start = [1, 3, 1, 5, 8, 6]
finish = [2, 6, 6, 7, 10, 8]

print_activities(start, finish)

# Output
# Following activities are selected
# 0  1  4