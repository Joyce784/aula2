idade1 = int(input("Qual sua idade:"))
idade2 = int(input("Qual sua idade:"))

if idade1 > idade2:
    print(f"A idade {idade1} é maior qua a {idade2}")
elif idade1 < idade2:
    print(f'A idade {idade1} é menor que a {idade2}')
else:
    print('As idades são iguais.')
