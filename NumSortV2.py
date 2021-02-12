numbers = []
print(numbers)
numLen = int(input("Number of Elements: "))
for a in range (0, numLen):
    v = int(input(f"Element number {a+1}: "))
    numbers.append(v)
print(numbers)
for i in range (0, numLen):
    for j in range (i+1, numLen):
        if numbers[i] > numbers[j]:
            x = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = x

            #print(numbers) #Check each step
print("Final: ", numbers)