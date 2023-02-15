from df_to_sqlserver.df_to_sqlserver import *
from df_to_sqlserver.df_to_mysql import *
from df_to_sqlserver.df_to_postgresql import *
from df_to_sqlserver.df_to_oracle import *
from df_to_sqlserver.df_to_sqlite import *

converter_df_in_sql(df="", tb_name="", name_script="")
converter_df_in_mysql(df="", db_name="", tb_name="", name_script="")
converter_df_in_postgresql(
    df="", tb_name="", name_script="", schema_name="public")
converter_df_in_oracle(df="", tb_name="", name_script="")
converter_df_in_sqlite(df="", tb_name="", name_script="")
