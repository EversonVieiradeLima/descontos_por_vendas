# Identificador Pessoal
identificador_pessoal = 'Éverson Vieira de Lima'
print('Bem vindo a Loja do {}'.format(identificador_pessoal))

valor_unitario = float(input('Digite o valor do produto: '))
quantidade_produto = int(input('Digite a quantidade do produto: '))

desconto_produto = 0
desconto_porcentagem = 0

# Cálculo do valor total sem desconto
total_sem_desconto = valor_unitario * quantidade_produto
print('O valor sem desconto foi: R${:.2f}'.format(total_sem_desconto))

# Teste condicional em cima da variável quantidade_produto
if quantidade_produto <= 9: # Outra maneira if quantidade_produto < 10
    desconto_produto = 0
    desconto_porcentagem = 0

elif 10 <= quantidade_produto <= 99: # Outra maneira elif quantidade_produto >= 10 and quantidade_produto < 100
    desconto_produto = 0.05 # 5% = 0.05
    desconto_porcentagem = 5

elif 100 <= quantidade_produto <= 999: # Outra maneira elif quantidade_produto >= 100 and quantidade_produto < 1000
    desconto_produto = 0.1 # 10% = 0.1
    desconto_porcentagem = 10

else:
    desconto_produto = 0.15 # 15% = 0.15
    desconto_porcentagem = 15

# Cálculo do valor total com desconto
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor com desconto foi: R${:.2f} (desconto {}%)'.format(total_com_desconto,desconto_porcentagem))