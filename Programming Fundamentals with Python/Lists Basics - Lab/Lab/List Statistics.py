n = int(input())
positive = []
negative = []
counter = 0
sum_negatives = 0
for _ in range(n):
    nums = int(input())
    if nums >= 0:
        positive.append(nums)
        counter += 1
    else:
        negative.append(nums)
        sum_negatives += nums
print(positive)
print(negative)
print(f"Count of positives: {counter}")
print(f"Sum of negatives: {sum_negatives}")
