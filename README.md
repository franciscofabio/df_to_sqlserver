# Project: Package to Convert Dataframes to SQL Server Script
## Project Author: Francisco Fadio
[(click here to see my profile on the platform)](https://github.com/franciscofabio)
#### Technology: Python | SQL
#### Date: 22/01/2023
-----------------------------------------
### Description
The "df_to_sql" package is used for:

- "Convert" module:
  - has the function converter_df_in_sql that with os.mkdir('SCRIPTS')
  - the function receives 3 variables as a parameter:
    - df -> dataframe name.
    - tb_name -> name of the sql database table.
    - name_script -> file name
  - creates the output folder for sql scripts
  - Through for adds '' in columns of type object 'categories'

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
from df_to_sqlserver.df_to_sqlserver import converter_df_in_sql
converter_df_in_sql(df,"Tablename","name_Script_SQL")
```


## Author:
Francisco Fabio de Almeida Ferreira <br>
Systems Analyst and Data Science Specialist

