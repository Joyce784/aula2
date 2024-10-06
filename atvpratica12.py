peso = int(input('digite seu peso:'))
altura = float(input('digite sua altura:'))
imc = peso/altura**2

if imc < 18.49:
  print('abaixo do peso')
elif imc >= 18.50 and imc <= 24.99:
  print('peso normal')
elif imc >= 25 and imc <= 29.99:
  print('sobrepeso')
elif imc >= 30 and imc <= 34.99:
  print('obesidade I')
elif imc >= 35 and imc <= 39.99:
  print('obesidade II') 
else:
  print('obesidade III')

