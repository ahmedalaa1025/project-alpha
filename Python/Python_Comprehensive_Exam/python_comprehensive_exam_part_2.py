# Question (2)

numbers = list(map(int , input("Enter 5 numbers:").split()))

print("Numbers:" , numbers)

print()

even_numbers = []
odd_numbers = []
even_count = 0
odd_count = 0

for number in numbers:
  if (number % 2 == 0):
    even_numbers.append(number)
    even_count += 1
  else:
    odd_numbers.append(number)
    odd_count += 1

print("Even Numbers:" , even_numbers)
print("Odd Numbers:" , odd_numbers)

print()

total = 0
count = len(numbers)

for number in numbers:
  total += number

print("Sum:" , total)

maximum = max(numbers)

print("Maximum:" , maximum)

minimum = min(numbers)

print("Minimum:" , minimum)

average = total / count

print("Average:" , average)

print()

print("Even Count:" , even_count)
print("Odd Count:" , odd_count)
