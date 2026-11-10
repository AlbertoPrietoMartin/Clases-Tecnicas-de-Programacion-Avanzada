import copy

print("Numeros")
a = 1
b = 1

print(f"id:{id(a)}, value: {a}")
print(f"id:{id(b)}, value: {b}")

print (f"{a is b}")

a = 2

print(f"id:{id(a)}, value: {a}")
print(f"id:{id(b)}, value: {b}")

print (f"{a is b}")

print("Listas")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print(f"id:{id(lista1)}, value: {lista1}")
print(f"id:{id(lista2)}, value: {lista2}")

print (f"{lista1 is lista2}")


lista3 = lista1.copy(lista1)
print(lista3)
lista3.append(5)
print(lista3)
print(lista1)

lista3 = copy.deepcopy(lista1)
lista3[1].append("new 2")

