scores = [100,90,80,70]
hap, count = 0,0
for score in scores:
    hap = hap + score
    count = count + 1
    average = hap / count
print(average)
