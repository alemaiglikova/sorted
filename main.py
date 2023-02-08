sort1 = "Hello world"
sorted_sort1 = ''.join(sorted(sort1))
print(sorted_sort1)

sort = "Hello world"
sort2 = list(sort)
n = len(sort2)
for i in range(n):
    for j in range(0, n - i - 1):
        if ord(sort2[j]) > ord(sort2[j + 1]):
            sort2[j], sort2[j + 1] = sort2[j + 1], sort2[j]

sorted_sort2 = ''.join(sort2)
print(sorted_sort2)