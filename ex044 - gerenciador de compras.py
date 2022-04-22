# Programa para gerenciamento de compras com menu de interação
# Simulador básico para estudo

print('{:=^40}'.format(' LOJA '))
preco = float(input('Preço da compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista DINHEIRO / CHEQUE
[ 2 ] à vista CARTÃO DÉBITO / PIX
[ 3 ] prazo 2x CARTÃO CRÉDITO
[ 4 ] prazo 3x ou mais CARTÃO CRÉDITO''')
opcao = int(input('Digite a opção de pagamento: '))
if opcao == 1:
    total = preco - (preco *10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao ==3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totapac = int(input('Quantas parcelas? '))
    parcela = total / totapac
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totapac, parcela))
else:
    total = preco
    print('Opção de pagamento invalida. Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))


