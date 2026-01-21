import csv

def escrever_csv(nome_arquivo, dados):
    
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
            return f"Dados escritos com sucesso em {nome_arquivo}"

    except Exception as e:
        print(f"Erro ao escrever o arquivo: {e}")



dados = [
    ['João', 26, 'São Paulo'],
    ['Maria', 38, 'Rio de Janeiro'],
    ['Pedro', 22, 'Belo Horizonte']
]

nome_arquivo = input("Digite o nome do arquivo CSV: ")
print(escrever_csv(nome_arquivo, dados))