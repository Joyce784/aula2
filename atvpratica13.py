usuario = input('digite um usuario:')
senha = input('digite uma senha:')

if usuario == 'admin':
    print('Seu login esta correto')
    if senha == '1234':
      print('Sua senha esta correta')
    else:
     print('Sua senha esta incorreto')
else:
  print('Seu login esta incorreto')
