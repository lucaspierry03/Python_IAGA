a = [int(item) for item in input().split(" ")]

print()
item = int(input("Item a ser preocurado: "))

print()

print(a)
print("Soma  =", sum(a))
print("Média =", sum(a))
print("Menor =", min(a))
print("Maior =", max(a))

print()
print(f"O item {item} existe {a.count(item)} vezes na lista")