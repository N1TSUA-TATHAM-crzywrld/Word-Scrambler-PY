import random

txt = input("Enter any word you would like to scramble. ")
arr = list(txt)
n = len(arr)

for i in range(n):
    j = random.randint(0, n-1)
    element = arr.pop(j)
    arr.append(element)
output = ("|".join(arr))

print(output)
