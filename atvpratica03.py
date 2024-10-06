idade1 = int(input('Digite sua idade:'))
habilitação = input('Você tem habilitação? Sim | Não:')

if idade1 >= 18 and habilitação.lower() == 'sim':
    print('Você é maior de idade e pode dirigir')

else:
    if idade1 < 18:
     print(f'Você não pode dirigir se é  menor de idade:')
    else:
       print(f'Você não pode dirigir porque não possui habilitação:')


    
