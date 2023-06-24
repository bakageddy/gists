COUNT = 10
observations = []

sum = 0
for i in range(COUNT):
    temp = int(input("Enter observation: "))
    sum += temp
    observations.append(temp)

mean = sum / COUNT

index = COUNT // 2
if COUNT % 2 == 0:
    # -1 because arrays are zero-indexed
    median = (observations[index] + observations[index - 1]) / 2
else:
    median = observations[index]

# mode = most frequent observation
max = [0, 0]
for i in set(observations):
    if max[0] < observations.count(i):
        max[0] = observations.count(i)
        max[1] = i

mode = max[1]
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
