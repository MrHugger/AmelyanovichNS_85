# This is a sample Python script.

i = 2
j = 2
k = 0
a = [3, 6, 5, 2, 1, 4]
b = [3, 1, 5, 6, 2, 4]
counter = 0
while (k < 100):
    i = a[i]
    j = b[j]
    if (i * i + j * j < 16):
        counter = counter + 1

print(i, j)
print(counter)

print("izmenenie")