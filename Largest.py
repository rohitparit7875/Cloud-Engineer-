numbers = [10, 45, 3, 99, 23]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
