def calcular_gorjeta(valor_conta, percentual_gorjeta):
    gorjeta = valor_conta * (percentual_gorjeta / 100) 
    return gorjeta

valor = float(input("Digite o valor da conta: R$ "))
percentual = float(input("Digite o percentual da gorjeta: "))

gorjeta = calcular_gorjeta(valor, percentual)

print(f"O valor da gorjeta é de: R${gorjeta:.2f}")