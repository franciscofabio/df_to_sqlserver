# Project: Package to Convert Dataframes to SQL Server, MYSQL, PostgreSQL, Oracle e SQLite Script
## Project Author: Francisco Fadio
[(click here to see my profile on the platform)](https://github.com/franciscofabio)
#### Technology: Python | SQL
#### Date: 22/01/2023
-----------------------------------------
### Description
The "df_to_sqlserver" package is used for:

- "Convert" module:
  - has the function converter_df_in_sql that with os.mkdir('SCRIPTS')
  - the function receives 3 variables as a parameter:
    - df -> dataframe name.
    - tb_name -> name of the sql database table.
    - name_script -> file name
  - creates the output folder for sql scripts
  - Through for adds '' in columns of type object 'categories'

The "df_to_mysql" package is used for:

- "Convert" module:
  - has the function converter_df_in_mysql that with os.mkdir('SCRIPTS')
  - the function receives 4 variables as a parameter:
    - df -> dataframe name.
    - db_name -> mysql database name.
    - tb_name -> name of the sql database table.
    - name_script -> file name
  - creates the output folder for mysqlsql scripts
  - Through for adds '' in columns of type object 'categories

The "df_to_postgresql" package is used for:

- "Convert" module:
  - has the function converter_df_in_postgresql that with os.mkdir('SCRIPTS')
  - the function receives 4 variables as a parameter:
    - df -> dataframe name.
    - tb_name -> name of the postgresql database table.
    - name_script -> file name.
    - schema_name -> postgresql schema name which by default receives the value as 'public'.
  - creates the output folder for postgresqlsql scripts
  - Through for adds '' in columns of type object 'categories

The "df_to_oracle" package is used for:

- "Convert" module:
  - has the function converter_df_in_oracle that with os.mkdir('SCRIPTS')
  - the function receives 4 variables as a parameter:
    - df -> dataframe name.
    - tb_name -> name of the oracle database table.
    - name_script -> file name.
  - creates the output folder for oracle scripts
  - Through for adds '' in columns of type object 'categories

The "df_to_sqlite" package is used for:

- "Convert" module:
  - has the function converter_df_in_sqlite that with os.mkdir('SCRIPTS')
  - the function receives 4 variables as a parameter:
    - df -> dataframe name.
    - tb_name -> name of the sqlite database table.
    - name_script -> file name.
  - creates the output folder for sqlite scripts
  - Through for adds '' in columns of type object 'categories
---------------------------------------------

### Here the goal is to provide a simple code package but it solved a real problem for me and I believe it can solve problems with other dataframes. If you need, you can collect the data in csv, treat them and after that, to insert the records in a sql server database, just use the df_to_sqlserver package to generate the scripts and then run these scripts in your DBMS or batch.
----------------------------------------------------
## How to install the package
```bash
pip install df_to_sqlserver
```
-------------------------------------------------
## How to use in any project

```python
from df_to_sqlserver.df_to_sqlserver import *
from df_to_sqlserver.df_to_mysql import *
from df_to_sqlserver.df_to_postgresql import *
from df_to_sqlserver.df_to_oracle import *
from df_to_sqlserver.df_to_sqlite import *

converter_df_in_sql(df="",tb_name="",name_script="")
converter_df_in_mysql(df="",db_name="",tb_name="",name_script="")
converter_df_in_postgresql(df="",tb_name="",name_script="",schema_name="public")
converter_df_in_oracle(df="",tb_name="",name_script="")
converter_df_in_sqlite(df="",tb_name="",name_script="")

```


## Author:
Francisco Fabio de Almeida Ferreira <br>
Systems Analyst and Data Science Specialist

