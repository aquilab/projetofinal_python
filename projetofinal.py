"""
Programa: Faz o download do arquivo do TCE-RS, salva em um arquivo .csv, depois transforma o csv em um xlsx usando o pandas e salva no hd, e depois novamente converte em um xlsx e salva no hd usando openpyxl.
Requisitos: Baixar dados html, transformar em csv, converter para xlsx e salvar no hd.
Ator: Áquila Ferreira.
Versão: 0.0.9
Data: 20/09/2022.
"""


import requests
import pandas as pd
import openpyxl

#função que lê a pagina html
def page_reader(endereco: str) -> requests.models.Response:
    r = requests.get(endereco)
    return r

#função que grava os dados da pagina em um arquivo html
def grava_pagina_web(resposta: requests.models.Response) -> None:
    arquivo = open('balancete.csv', 'wb')
    for texto in resposta.iter_content():
        arquivo.write(texto)
    arquivo.close()
    return arquivo

#Usando o Pandas para: balancete.csv para balancete e depois para balancete.xlsx.
#(busca e cria o arquivo no mesmo diretorio em que o programa roda).
def panda_xlsx():
    balancete = pd.read_csv('balancete.csv')
    balancete.to_excel('balancete.xlsx', sheet_name='balancete', index=False)
    
#Usando o OpenPyXL: ler balancete.xlsx para a variável "novo_balancete" e depois gravar em "novo_balancete.xlsx"
#(busca e cria o arquivo no mesmo diretorio em que o programa roda).
def openpyxl_xlxs():
    novo_balancete = load_workbook('balancete.xlsx')
    novo_balancete.save('novo_balancete.xlsx')

    

def main():
    endereco = 'http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv'
    dados = page_reader(endereco)
    grava_pagina_web(dados)
    panda_xlsx()
    openpyxl_xlxs()
    
    
if __name__ == "__main__":
    main()

