# Author: Francisco Fabio
# Função para converter o dataframe em script oracle
# df -> nome do dataframe
# tb_name -> nome da tabela do banco postgresql
# name_script -> nome do arquivo

def converter_df_in_oracle(df, tb_name, name_script):
    
    import os
    try:
        os.mkdir('SCRIPTS')
    except FileExistsError:
        pass
    
    # Completando o nome do Script
    name_script = name_script+"_ORACLE"
    
    #Adicionar as aspas simples nas categoricas (strings)
    data = df.copy()
    for c in data.columns:
        if data[c].dtype == object:
            data[c] = "'"+data[c]+"'"    
    
    #Adiciona a primeira linha com nome da tabela
    txt1 = f"INSERT ALL"
    with open(f"SCRIPTS/{name_script}.sql","a",encoding="utf-8") as arquivo:
        arquivo.writelines(txt1+"\n")
    
    # Adiciona parte com os nomes das colunas
    columns_ = ", ".join(data.columns)
    columns_ = "("+columns_+")"
        
    # Adiciona linhas com os valores (registros a serem inseridos)
    for i in range(data.shape[0]):
        s = [data[c][i] for c in data.columns]
        s = str(s).replace("[","(")
        s = str(s).replace("]",")")
        s = str(s).replace("\"","")

        with open(f"SCRIPTS/{name_script}.sql","a",encoding="utf-8") as arquivo:
            arquivo.writelines(f"\tINTO {tb_name} {columns_} VALUES "+s+"\n")
    
    #Adicionar o Select final.
    with open(f"SCRIPTS/{name_script}.sql","a",encoding="utf-8") as arquivo:
        arquivo.writelines(f"SELECT * FROM dual;")