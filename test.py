scores = [88, 92, 76, 61, 59, 95, 83, 70, 45, 100]
total = 0
for score in scores:
    total += score

mean = total / len(scores)
#计算方差和
variance_sum = 0
for score in scores:
    variance_sum += (score - mean) ** 2
#计算方差
variance = variance_sum / len(scores)

print("mean:", mean)
print("variance:", variance)
print("max:", max(scores))
print("min:", min(scores))