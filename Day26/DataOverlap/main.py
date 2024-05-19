with open("file1.txt") as f1, open("file2.txt") as f2:
    numbers1 = f1.readlines()
    numbers2 = f2.readlines()

result = [int(n) for n in numbers1 if n in numbers2]

# Write your code above 👆
print(result)