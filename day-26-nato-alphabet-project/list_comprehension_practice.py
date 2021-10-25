# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers = [n for n in numbers if n % 2 == 0]
# print(even_numbers)

with open("file1.txt") as f:
    numbers1 = f.readlines()

with open("file2.txt") as f:
    numbers2 = f.readlines()

result = [int(num.strip()) for num in numbers1 if num in numbers2]

print(result)