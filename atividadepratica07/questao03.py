import csv
import os

def ler_arquivo(nome_arquivo):
   
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(diretorio_script, nome_arquivo)
    
    try:
        with open(caminho_completo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)

    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
        print(f"Caminho procurado: {caminho_completo}")

nome_arquivo = input("Digite o nome do arquivo CSV: ")
ler_arquivo(nome_arquivo)