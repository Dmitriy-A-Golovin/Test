import statistics
nums = []

with open("файл4.txt") as f:
    for line in f:
        nums.append(int(line))
med = int(statistics.median(nums))
otvet = 0
for i in range(len(nums)):
    otvet += abs(nums[i] - med)
print(otvet)
