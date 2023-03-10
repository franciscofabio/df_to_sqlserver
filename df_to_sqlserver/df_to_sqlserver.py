# Author: Francisco Fabio
# Função para converter o dataframe em script sql
# df -> nome do dataframe, tb_name -> nome da tabela do banco sql
# name_script -> nome do arquivo
import pandas as pd
import numpy as np


# Função para converter o dataframe em script sql
# df -> nome do dataframe, tb_name -> nome da tabela do banco sql
# name_script -> nome do arquivo

def converter_df_in_sql(df, tb_name, name_script):
    import os
    try:
        os.mkdir('SCRIPTS')
    except FileExistsError:
        pass
    
    # Completando o nome do Script
    name_script = name_script+"_SQL"
    
    #Adicionar as aspas simples nas categoricas (strings)
    data = df.copy()
    for c in data.columns:
        if data[c].dtype == object:
            data[c] = "'"+data[c]+"'"    
    
    #Adiciona a primeira linha com nome da tabela
    txt1 = f"INSERT INTO [dbo].[{tb_name}]"
    with open(f"SCRIPTS/{name_script}.sql","a",encoding="utf-8") as arquivo:
        arquivo.writelines(txt1+"\n")
    
    # Adiciona linhas com os nomes das colunas
    cols = data.columns.tolist()
    for c in range(data.shape[1]):
        if c == 0:
            s = f"\t\t\t([{cols[c]}]"
        elif c == data.shape[1]-1:
            s = f"\t\t\t,[{cols[c]}])"
        else:
            s = f"\t\t\t,[{cols[c]}]"

        with open(f"SCRIPTS/{name_script}.sql","a",encoding="utf-8") as arquivo:
                arquivo.writelines(s+"\n")

    with open(f"SCRIPTS/{name_script}.sql","a",encoding="utf-8") as arquivo:
        arquivo.writelines("\tVALUES"+"\n")
    
    # Adiciona linhas com os valores (registros a serem inseridos)
    for i in range(data.shape[0]):
        s = [data[c][i] for c in data.columns]
        s = str(s).replace("[","(")
        s = str(s).replace("]",")")
        s = str(s).replace("\"","")

        if i == data.shape[0]-1:
            s = s
        else:
            s = s+","

        with open(f"SCRIPTS/{name_script}.sql","a",encoding="utf-8") as arquivo:
            arquivo.writelines("\t\t\t"+s+"\n")
