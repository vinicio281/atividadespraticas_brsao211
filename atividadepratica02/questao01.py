valor_reais = float(input("Digite o valor em reais: "))

cotacao_dolar = 5.37

cotacao_euro = 6.25

valor_dolar = valor_reais / cotacao_dolar

valor_euro = valor_reais / cotacao_euro

print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Valor em dólar: U$ {valor_dolar:.2f}")
print(f"Valor em euros10: € {valor_euro:.2f}")