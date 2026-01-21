def calcular_desconto(valor_produto, percentagem_desconto):
    desconto = valor_produto * (percentagem_desconto / 100)
    valor_final = valor_produto - desconto 
    return valor_final

valor = float(input("Digite o valor do produto: R$ "))
porcentagem = float(input("Digite a porcentagem de desconto: "))

desconto = calcular_desconto(valor, porcentagem)

print(f"O valor final com desconto é: R${desconto:.2f}")