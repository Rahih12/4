1
x, y = 1, 2
print(x)
print(y)
1
name, age, company = ("Илья", 18, "НГТУ")
print(name)
print(age)
print(company)

people = ["Андрей", "Екатерина", "Сергей"]
first, second, third = people
print(first)
print(second)
print(third)

dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
r, b, g = dictionary
print(r)
print(b)
print(g)
# получаем значение по ключу
print(dictionary[g])

people = [
    ("Андрей", 17, "НГТУ"),
    ("Екатерина", 17, "НГУ"),
    ("Сергей", 19, "НГУЭУ")
]

for name, age, company in people:
    print(f"Name: {name}, Age: {age}, Company: {company}")

people = ["Андрей", "Екатерина", "Сергей"]
for index, name in enumerate(people):
    print(f"{index}.{name}")

person =("Илья", 18, "НГТУ")
name, _, company = person
print(name)
print(company)

name, _, company = person
print(_)

num1=1
num2=2
num3=3
*numbers,=num1,num2,num3
print(numbers)

head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]

print(head)
print(tail)

head, *middle, tail = [1, 2, 3, 4, 5]

print(head)
print(middle)
print(tail)

first, second, *other = [1, 2, 3, 4, 5]

print(first)
print(second)
print(other)

first, _, third, *_, last = [1, 2, 3, 4, 5, 6, 7, 8]

print(first)
print(third)
print(last)

red, *other, green = {"red":"красный", "blue":"синий", "yellow":"желтый", "green":"зеленый"}

print(red)
print(green)
print(other)

nums1 = [1, 2, 3]
nums2 = (4, 5, 6)

# распаковываем список nums1 и кортеж nums2
nums3 = [*nums1, *nums2]
print(nums3)

dictionary1 = {"red":"красный", "blue":"синий"}
dictionary2 = {"green":"зеленый", "yellow":"желтый"}

# распаковываем словари
dictionary3 = {**dictionary1, **dictionary2}
print(dictionary3)
