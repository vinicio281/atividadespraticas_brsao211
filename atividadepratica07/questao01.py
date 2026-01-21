import pandas as pd
import os

def processar_logs_treinamentos(arquivo_Log):

    try:
       
        pasta_script = os.path.dirname(os.path.abspath(__file__))
        caminho_completo = os.path.join(pasta_script, arquivo_Log)
        leitor = pd.read_csv(caminho_completo)
        media = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return f"Média: {media:.2f}, Desvio Padrão: {desvio_padrao:.2f}"


    


    except FileNotFoundError:
        return "Arquivo não encontrado."
    

arquivo = input("Digite o nome do arquivo de log: ")
print(processar_logs_treinamentos(arquivo))