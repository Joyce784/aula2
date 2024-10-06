nota1 = float(input('Qual sua 1ª nota:'))
nota2 = float(input('Qual sua 2ª nota:'))

if nota1 > 6 and nota2 > 6:
    print(f'A nota {nota1} e nota{nota2} são maiores que 6')  


elif nota1 == 6 and nota2 == 6:
    print(f'A nota {nota1} e a nota {nota2} são iguais a 6')

elif nota1 <= 6 and nota2 <= 6:
    print(f'A nota {nota1} e a nota {nota2} são menores a 6')    

elif nota1 >= 6 and nota2 <= 6:
    print(f'A nota {nota1} e maior que 6 {nota2} é menor que 6')  

elif nota1 <= 6 and nota2 >= 6:
    print(f'A nota {nota1} e menor que 6 {nota2} é maior que 6')        
