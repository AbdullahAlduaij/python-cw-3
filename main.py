

favorite_animals = ["dog", "cat", "monkey", "rabbit"]
print("favorite_animals list:", favorite_animals)
print("Second element:", favorite_animals[1])
favorite_animals.remove("monkey") 
print("Updated favorite_animals list:", favorite_animals)

favorite_animals.append("elephant") 
for animal in favorite_animals:
    print("I love", animal)

numbers = [1, 2, 3, 4, 5]
numbers_sum = 0
for num in numbers:
    numbers_sum += num
print("Sum of numbers:", numbers_sum)
